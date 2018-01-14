# Github Trends

Prints trending [github.com](https://github.com) repositories of the
week and their issues_amounts

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to use

Example:
```bash
$ python github_trending.py
Популярные проекты за последнюю неделю:
speed47/spectre-meltdown-checker
https://api.github.com/repos/speed47/spectre-meltdown-checker
Открытых задач: 5

evilsocket/bettercap-ng
https://api.github.com/repos/evilsocket/bettercap-ng
Открытых задач: 4

...
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
