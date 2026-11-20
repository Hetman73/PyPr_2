"""Напишите программу, которая получает информацию о репозиториях пользователей GitHub.

Программа должна иметь следующую функциональность:

Принимает на вход список пользователей GitHub.
Для каждого пользователя получает его информацию и список его репозиториев.
Составляет список результатов в формате JSON, в котором для каждого пользователя указаны его логин,
количество публичных репозиториев и список его репозиториев.
Для получения информации о пользователе и его репозиториях должны использоваться открытые API GitHub.

Пример использования программы:

users = ['user1', 'user2', 'user3']
result = get_github_users(users)
print(result)"""
import task_test

"""GitHub предоставляет открытое API (без ключа, но с лимитом запросов):

https://api.github.com/users/{username} — информация о пользователе (там есть поле public_repos).

https://api.github.com/users/{username}/repos — список репозиториев."""

import requests
import json
import time
from typing import List, Dict, Any


def get_github_users(users: List[str]) -> str:
    """
    Получает информацию о пользователях GitHub и их репозиториях.
    Возвращает отформатированную JSON-строку с результатами.
    """
    results = []

    # Базовый URL для API GitHub
    base_url = "https://api.github.com"

    for username in users:
        print(f"Обработка пользователя: {username}...")

        user_data = {
            "login": username,
            "public_repos": 0,
            "repositories": [],
            "error": None
        }

        try:
            # 1. Получаем информацию о пользователе
            user_url = f"{base_url}/users/{username}"
            user_response = requests.get(user_url, timeout=10)

            if user_response.status_code == 404:
                user_data["error"] = "Пользователь не найден"
                results.append(user_data)
                continue

            user_response.raise_for_status()  # Вызовет ошибку, если статус не 200
            user_info = user_response.json()

            user_data["public_repos"] = user_info.get("public_repos", 0)

            # 2. Получаем список репозиториев
            repos_url = f"{base_url}/users/{username}/repos"
            # Параметр per_page=100 позволяет получить больше репозиториев за раз
            repos_response = requests.get(f"{repos_url}?per_page=100", timeout=10)
            repos_response.raise_for_status()

            repos_info = repos_response.json()

            # Извлекаем названия репозиториев (можно добавить и другие поля)
            user_data["repositories"] = [repo["name"] for repo in repos_info]

        except requests.exceptions.RequestException as e:
            user_data["error"] = f"Ошибка сети или API: {str(e)}"
        except Exception as e:
            user_data["error"] = f"Неизвестная ошибка: {str(e)}"

        results.append(user_data)

        # Небольшая пауза, чтобы не превысить лимит запросов (60 в час для анонимов)
        time.sleep(1)

    # Превращаем список словарей в красивую JSON-строку
    # ensure_ascii=False - Это нужно для того, чтобы русские символы в описаниях
    # репозиториев отображались нормально, а не как \u041f\u0440\u0438...
    return json.dumps(results, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    users = ['Hetman73', 'nemo', 'torvalds']
    result = get_github_users(users)
    print(result)


"""Тестирование функции с использованием Mock и patch"""

import unittest
import json
from unittest.mock import patch, MagicMock



class TestGitHubUsers(unittest.TestCase):

    # ТЕСТ 1: Успешное получение данных
    @patch('src.task_test.task_12_1_2.time.sleep')  # Отключаем паузу, чтобы тест был быстрым
    @patch('src.task_test.task_12_1_2.requests.get')
    def test_success(self, mock_get, mock_sleep):
        # 1. Создаем фейковый ответ для пользователя
        fake_user = MagicMock()
        fake_user.status_code = 200
        fake_user.json.return_value = {"login": "testuser", "public_repos": 2}

        # 2. Создаем фейковый ответ для репозиториев
        fake_repos = MagicMock()
        fake_repos.status_code = 200
        fake_repos.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        # 3. Говорим mock_get возвращать сначала fake_user, потом fake_repos
        mock_get.side_effect = [fake_user, fake_repos]

        # Вызываем функцию
        result_json = get_github_users(['testuser'])
        result = json.loads(result_json)

        # Проверяем результаты
        self.assertEqual(result[0]["login"], "testuser")
        self.assertEqual(result[0]["public_repos"], 2)
        self.assertEqual(result[0]["repositories"], ["repo1", "repo2"])
        self.assertIsNone(result[0]["error"])

    # ТЕСТ 2: Пользователь не найден (404)
    @patch('src.task_test.task_12_1_2.time.sleep')
    @patch('src.task_test.task_12_1_2.requests.get')
    def test_user_not_found(self, mock_get, mock_sleep):
        # 1. Создаем фейковый ответ с кодом 404
        fake_response = MagicMock()
        fake_response.status_code = 404
        mock_get.return_value = fake_response

        # Вызываем функцию (она должна быть доступна в этом файле)
        result_json = get_github_users(['unknown_user'])
        result = json.loads(result_json)

        # Проверяем, что функция не упала, а записала ошибку в JSON
        self.assertEqual(result[0]["login"], "unknown_user")
        self.assertEqual(result[0]["public_repos"], 0)
        self.assertEqual(result[0]["repositories"], [])
        self.assertEqual(result[0]["error"], "Пользователь не найден")


if __name__ == '__main__':
    unittest.main()