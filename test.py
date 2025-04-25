import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
URL = os.getenv('URL')

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def test_create_repo():
    data = {
        "name" : REPO_NAME,
        "private": False,
        "description" : "I'm creating a repository",
        "is_template": True,
        "homepage" : "https://github.com"
    }
    response = requests.post(
        f"{URL}/user/repos",
        json=data,
        headers=headers
    )
    assert response.status_code == 201, f"Ошибка создания: {response.status_code}, {response.text}"

def test_repo_exists():
    response = requests.get(f"{URL}/users/{USERNAME}/repos", headers=headers)
    assert response.status_code == 200, "Ошибка получения списка репозиториев"
    repo_names = [repo["name"] for repo in response.json()]
    assert REPO_NAME in repo_names, "Репозиторий не найден"

def test_delete_repo():
    response = requests.delete(f"{URL}/repos/{USERNAME}/{REPO_NAME}", headers=headers)
    assert response.status_code == 204, "Ошибка удаления"

test_create_repo()
test_repo_exists()
test_delete_repo()
