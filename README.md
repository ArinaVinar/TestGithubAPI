# TestGithubAPI

## Описание

Этот проект позволяет протестировать работу GitHub API: создание, проверку наличия и удаление репозитория.

---

## Установка

1. Установите Python 3.7+
2. Клонируйте проект:

```bash
git clone https://github.com/ArinaVinar/TestGithubAPI.git
cd TestGithubAPI
```

Установите зависимости

```bash
pip install -r requirements.txt
```

Настройка переменных окружения

```bash
GITHUB_USERNAME=your-github-username
GITHUB_TOKEN=your-personal-access-token
REPO_NAME=your-test-repo-name
URL=https://api.github.com
```

## Запуск теста

```bash
pytest test.py -v
```
