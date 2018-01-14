import requests
import datetime


def get_trending_repositories(top_size=500):
    days_count = 7
    date = (datetime.datetime.today() - datetime.timedelta(
        days_count)
    ).strftime("%Y-%m-%d")
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
    success_status = 200
    issues = requests.get(
        'https://api.github.com/repos/{owner}/{repo}/issues'.format(
            owner=repo_owner,
            repo=repo_name
        )
    )
    if int(issues.status_code) == success_status:
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
