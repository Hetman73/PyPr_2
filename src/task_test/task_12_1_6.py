"""Напишите функцию, которая принимает JSON-строку с данными о различных событиях,
включающих даты начала и окончания, и возвращает список длительностей каждого события в днях.

Пример входных данных:

[
  {
    "name": "Event 1",
    "start_date": "2022-01-01",
    "end_date": "2022-01-05"
  },
  {
    "name": "Event 2",
    "start_date": "2022-02-15",
    "end_date": "2022-02-18"
  },
  {
    "name": "Event 3",
    "start_date": "2022-03-10",
    "end_date": "2022-03-20"
  }
]
Пример выходных данных:

[5, 4, 11]"""

import json
import datetime
from datetime import datetime


def dates_filter_day(json_data):
    """принимает JSON-строку с данными о различных событиях,
    включающих даты начала и окончания,
    и возвращает два списка: даты начала и даты окончания"""

    list_start_date = []
    list_end_date = []

    # 1. Превращаем JSON-строку в список словарей
    json_data = json.loads(json_data)

    # 2. Проходимся по каждому событию
    for day in json_data:
        # Просто берем даты по ключам. Если ключа нет, Python сам выдаст ошибку,
        # поэтому проверка "in day" здесь не нужна.
        list_start_date.append(day["start_date"])
        list_end_date.append(day["end_date"])



    # 3. Возвращаем кортеж из двух списков
    return list_start_date, list_end_date


if __name__ == '__main__':
    json_data = json.dumps([
        {"name": "Event 1", "start_date": "2022-01-01", "end_date": "2022-01-05"},
        {"name": "Event 2", "start_date": "2022-02-15", "end_date": "2022-02-18"},
        {"name": "Event 3", "start_date": "2022-03-10", "end_date": "2022-03-20"}
    ])

    # Получаем два списка
    start_dates, end_dates = dates_filter_day(json_data)

    print("Даты начала:", start_dates)
    print("Даты окончания:", end_dates)


def get_hours_difference(start_str: str, end_str: str) -> float:
    """Разница в днях между start_dates и end_dates"""
    # Формат: Год-Месяц-День Часы:Минуты:Секунды
    date_format = "%Y-%m-%d %H:%M:%S"
    # Превращаем строки в объекты datetime
    start = datetime.strptime(start_str, date_format)
    end = datetime.strptime(end_str, date_format)
    return abs((end - start).total_seconds() / 3600)

if __name__ == '__main__':
    # Пример 1: Разница в 1 день и 2 часа
    start = "2022-01-01 10:00:00"
    end = "2022-01-02 12:00:00"
    print(f"Часов между {start} и {end}: {get_hours_difference(start, end)}")
    # Вывод: 26.0

    # Пример 2: Разница в полтора часа
    start2 = "2023-05-10 15:30:00"
    end2 = "2023-05-10 17:00:00"
    print(f"Часов между {start2} и {end2}: {get_hours_difference(start2, end2)}")
    # Вывод: 1.5