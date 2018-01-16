import requests
import datetime


def get_trending_repositories(repositories_count=20):
    days_count = 7
    date_from = (datetime.datetime.today() - datetime.timedelta(
        days_count
    )).strftime("%Y-%m-%d")
    repositories = requests.get(
        'https://api.github.com/search/repositories',
        {
            "q": "created:>{}".format(date_from),
            "sort": "stars",
            "per_page": repositories_count
        }
    )
    return repositories.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    issues = requests.get(
        'https://api.github.com/repos/{owner}/{repo}/issues'.format(
            owner=repo_owner,
            repo=repo_name
        )
    )
    if issues.ok:
        return len(issues.json())
    else:
        return None


if __name__ == '__main__':

    repositories = get_trending_repositories()

    print("Популярные проекты за последнюю неделю:")
    for repository in repositories:
        issues_amount = get_open_issues_amount(
            repository['owner']['login'],
            repository['name']
        )
        if issues_amount is None:
            issues_amount = "неизвестно"
        print(
            '{owner}/{repo}\n{link}\nОткрытых задач: {issues_amount}\n'.format(
                owner=repository['owner']['login'],
                repo=repository['name'],
                link=repository['url'],
                issues_amount=issues_amount
            )
        )
