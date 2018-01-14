import requests
import datetime


def get_trending_repositories(top_size=500):
    date = (datetime.datetime.today() - datetime.timedelta(7)).strftime(
        "%Y-%m-%d"
    )
    repositories = requests.get(
        'https://api.github.com/search/repositories',
        {
            "q": "size:<={} created:{}".format(top_size, date),
            "sort": "stars",
            "per_page": "20"
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
    if int(issues.status_code) == 200:
        return len(issues.json())
    else:
        return "неизвестно ({})".format(issues.json()['message'])


if __name__ == '__main__':

    repositories = get_trending_repositories()

    print("Популярные проекты за последнюю неделю:")
    for repository in repositories:
        issues_amount = get_open_issues_amount(
            repository['owner']['login'],
            repository['name']
        )
        print(
            '{owner}/{repo}\n{link}\nОткрытых задач: {issues_amount}\n'.format(
                owner=repository['owner']['login'],
                repo=repository['name'],
                link=repository['url'],
                issues_amount=issues_amount
            )
        )
