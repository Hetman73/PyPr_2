"""Напишите функцию
generate_users(first_names, last_names, cities)
, которая будет генерировать случайных пользователей. Функция должна возвращать генератор, который будет выдавать каждого пользователя по одному в виде словаря.

Каждый пользователь должен иметь следующие данные:

first_name
 — имя из списка
first_names
;
last_name
 — фамилия из списка
last_names
;
age
 — возраст от 18 до 65 лет;
city
 — город из списка
cities
.
Сгенерируйте группу пользователей и выведите ее списком в консоль в формате JSON.

Пример формата данных JSON:

[
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 34,
        "city": "New York"
    },
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "age": 45,
        "city": "Los Angeles"
    },
    ...
]
Чтобы выбрать случайный элемент списка, можно воспользоваться методом
choice
 из библиотеки
random
."""
from pathlib import Path
import json
import random


def generate_users(first_names=None, last_names=None, cities=None):
    # Находим корень проекта (поднимаемся на 3 уровня вверх от текущего файла)
    # task_12_1.py -> task_test -> src -> PythonProject_2
    base_dir = Path(__file__).resolve().parent.parent.parent
    file_path = base_dir / 'data' / 'users_rus.json'

    with open(file_path, 'r', encoding='utf-8') as file:
        users = json.load(file)

    # Фильтруем пользователей, если переданы аргументы
    filtered_users = users
    if first_names:
        filtered_users = [u for u in filtered_users if u['first_name'] in first_names]
    if last_names:
        filtered_users = [u for u in filtered_users if u['last_name'] in last_names]
    if cities:
        filtered_users = [u for u in filtered_users if u['city'] in cities]

    # Если после фильтрации список пуст, используем всех
    if not filtered_users:
        filtered_users = users

    # Бесконечный генератор
    while True:
        random_user = random.choice(filtered_users)
        yield json.dumps(random_user, ensure_ascii=False) # если латиница то ensure_ascii=False не нужно

if __name__ == "__main__":
    # Пример 1: Передаем аргументы (например, хотим только из Москвы и Питера)
    p1 = generate_users(cities=["Москва", "Санкт-Петербург"])
    print("Случайный из Москвы/Питера:")
    print(next(p1))
    print(next(p1))


    # Пример 2: Вызываем без аргументов (берет любого из файла)
    p2 = generate_users()
    print("Случайный из всех:")
    print(next(p2))





"""Напишите программу, которая будет принимать на вход JSON-файл с данными о финансовых транзакциях, 
фильтровать транзакции, совершенные в определенной валюте, и сохранять отфильтрованные данные в 
новый JSON-файл.

Также напишите декоратор, который будет выводить в консоль статистику по количеству отфильтрованных 
транзакций. Статистика должна включать в себя количество отфильтрованных транзакций и их суммарную стоимость."""

from pathlib import Path


def filter_transactions_by_currency(input_file, output_file, currency):
    # Вычисляем путь к корню проекта (поднимаемся на 3 уровня от текущего файла)
    # task_12_1.py -> task_test -> src -> PythonProject_2
    base_dir = Path(__file__).resolve().parent.parent.parent

    # Формируем полный путь к файлам
    input_path = base_dir / 'data' / input_file
    output_path = base_dir / 'data' / output_file

    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Предполагаем, что data - это список словарей (транзакций)
        filtered_data = list(filter(lambda transaction: transaction['currency'] == currency, data))


    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
 filter_transactions_by_currency('transactions.json', 'filtered.json', 'USD')








import json
from pathlib import Path
from functools import wraps


# 1.Декоратор, адаптированный под запись в файл
def stat_decorator(func):
    """Декоратор для вывода статистики по отфильтрованным транзакциям в лог-файл."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Вызываем оригинальную функцию и получаем отфильтрованные данные
        filtered_transactions = func(*args, **kwargs)

        # Считаем статистику
        total_amount = sum([transaction['amount'] for transaction in filtered_transactions])
        stats_message = f"Отфильтровано {len(filtered_transactions)} транзакций на сумму {total_amount}\n"

        # Формируем путь к папке doks и файлу stats.log
        # __file__ - это путь к текущему файлу скрипта
        base_dir = Path(__file__).resolve().parent.parent.parent
        log_dir = base_dir / 'data'

        # Создаем папку data, если её еще нет (exist_ok=True предотвращает ошибку, если папка уже есть)
        log_dir.mkdir(parents=True, exist_ok=True)

        log_file_path = log_dir / 'stats.log'

        # Записываем статистику в файл (режим 'a' - добавление в конец файла)
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(stats_message)

        return filtered_transactions

    return wrapper


# 2. Объявляем функцию ОДИН РАЗ и вешаем на неё декоратор
@stat_decorator
def filter_transactions_by_currency(input_file, output_file, currency):
    base_dir = Path(__file__).resolve().parent.parent.parent
    input_path = base_dir / 'data' / input_file
    output_path = base_dir / 'data' / output_file

    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        filtered_data = list(filter(lambda transaction: transaction['currency'] == currency, data))

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)

    return filtered_data  # Это нужно декоратору!


# 3. Вызов
if __name__ == "__main__":
    filter_transactions_by_currency('transactions.json', 'filtered.json', 'USD')


"""def stat_decorator(func):
    ""Каркас декоратор для вывода статистики по отфильтрованным транзакциям.
    для использования в качестве шаблона к написанию декораторов""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # --- ЛОГИКА СТАТИСТИКИ (то, что должно произойти ДО) ---
        print("--- Начинаем подсчет статистики ---")

        # Вызов оригинальной функции с переданными аргументами
        result = func(*args, **kwargs)

        # --- ЛОГИКА СТАТИСТИКИ (то, что должно произойти ПОСЛЕ) ---
        print("--- Статистика выведена ---")

        # Возвращаем результат работы оригинальной функции
        return result

        # Возвращаем саму функцию-обертку

    return wrapper

"""