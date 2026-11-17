import pytest
import json
import os
from src.task_test.task_12_1 import generate_users


# Фикстура, которая создает временный файл users_rus.json перед тестами
@pytest.fixture
def mock_json_file(tmp_path, monkeypatch):
    # Тестовые данные
    test_data = [
        {"first_name": "Иван", "last_name": "Иванов", "age": 30, "city": "Москва"},
        {"first_name": "Анна", "last_name": "Смирнова", "age": 25, "city": "Санкт-Петербург"},
        {"first_name": "Петр", "last_name": "Петров", "age": 40, "city": "Казань"}
    ]

    # Создаем файл во временной директории (tmp_path)
    file_path = tmp_path / "users_rus.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False)

    # Подменяем текущую рабочую директорию на временную,
    # чтобы функция open('users_rus.json') нашла наш тестовый файл
    monkeypatch.chdir(tmp_path)
    return test_data


def test_generate_users_returns_json_string(mock_json_file):
    # Получаем генератор
    gen = generate_users()

    # Берем один элемент
    result = next(gen)

    # Проверяем, что это строка
    assert isinstance(result, str)

    # Проверяем, что это валидный JSON
    parsed_data = json.loads(result)

    # Проверяем, что в словаре есть все нужные ключи
    assert "first_name" in parsed_data
    assert "last_name" in parsed_data
    assert "age" in parsed_data
    assert "city" in parsed_data


def test_generate_users_filter_by_city(mock_json_file):
    # Передаем только Москву
    gen = generate_users(cities=["Москва"])

    # Генерируем 5 пользователей подряд, чтобы убедиться, что все они из Москвы
    for _ in range(5):
        result_str = next(gen)
        user = json.loads(result_str)
        assert user["city"] == "Москва"


def test_generate_users_is_infinite(mock_json_file):
    gen = generate_users()

    # Вызываем next() 100 раз. Если бы генератор был конечным,
    # на каком-то шаге вылетела бы ошибка StopIteration.
    for _ in range(100):
        user = next(gen)
        assert user is not None


# def test_generate_users_fallback_when_no_match(mock_json_file):
#     # Передаем город, которого нет в тестовых данных
#     gen = generate_users(cities=["Сочи"])
#
#     result_str = next(gen)
#     user = json.loads(result_str)
#
#     # Проверяем, что нам все равно вернули пользователя (так как список не должен быть пустым)
#     assert user is not None
#     # И этот пользователь из наших тестовых данных
#     assert user["city"] in ["Москва", "Санкт-Петербург", "Казань"]