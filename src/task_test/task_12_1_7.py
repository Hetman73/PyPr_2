import json
import datetime
#from datetime import datetime


def dates_filter_day(json_data: str) -> list[int]:
    """
    Принимает JSON-строку с событиями,
    возвращает список длительностей каждого события в днях.
    """
    list_day = []

    # 1. Превращаем JSON-строку в список словарей Python
    events = json.loads(json_data)

    # 2. Проходимся по каждому событию
    for event in events:
        # Берем даты начала и окончания из словаря
        start_str = event["start_date"]
        end_str = event["end_date"]

        # Превращаем строки в объекты date (формат YYYY-MM-DD)
        start_date = datetime.datetime.strptime(start_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_str, "%Y-%m-%d").date()

        # Вычисляем разницу в днях
        duration = (end_date - start_date).days

        list_day.append(duration)

    # ВАЖНО: return находится ПОСЛЕ цикла
    return list_day


if __name__ == '__main__':
    # В задании сказано "принимает JSON-строку",
    # поэтому мы имитируем строку, превращая список в JSON
    raw_events = [
        {"name": "Event 1", "start_date": "2022-01-01", "end_date": "2022-01-05"},
        {"name": "Event 2", "start_date": "2022-02-15", "end_date": "2022-02-18"},
        {"name": "Event 3", "start_date": "2022-03-10", "end_date": "2022-03-20"}
    ]

    # Превращаем список в JSON-строку для теста
    json_string = json.dumps(raw_events)

    result = dates_filter_day(json_string)
    print(result)