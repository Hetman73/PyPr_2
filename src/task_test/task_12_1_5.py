"""Напишите функцию, которая принимает список дат в формате списка строк, например
["2022.12.31", "2023.1.7"]
, и возвращает список дат в формате строк через одну неделю, например
["January 7, 2023", "January 14, 2023"]
."""

from datetime import datetime, timedelta


def get_dates_plus_week(dates_list: list[str]) -> list[str]:
    """
    Принимает список дат в формате 'YYYY.MM.DD',
    прибавляет к каждой 7 дней и возвращает в формате 'Месяц День, Год'.
    """
    result = []

    for date_str in dates_list:
        # 1. Превращаем строку в объект datetime
        # Формат "%Y.%m.%d" означает: Год.Месяц.День
        try:
            dt = datetime.strptime(date_str, "%Y.%m.%d")

            # 2. Прибавляем одну неделю (7 дней)
            dt_plus_week = dt + timedelta(days=7)

            # 3. Форматируем в нужный вид: "January 7, 2023"
            # В Python формат "%B" — это полное название месяца на английском
            formatted_date = dt_plus_week.strftime("%B %d, %Y")

            # Убираем ведущий ноль у дня, если он есть (например, "07" -> "7")
            # В Windows метод strftime для %d может выдавать "07".
            # Заменим " 0" на " ", чтобы было как в примере "January 7"
            formatted_date = formatted_date.replace(" 0", " ")

            result.append(formatted_date)

        except ValueError:
            print(f"Ошибка: '{date_str}' не является корректной датой в формате YYYY.MM.DD")

    return result

dates = ["2022.12.31", "2023.1.7"]
print(get_dates_plus_week(dates))


"""Тесты"""

def test_get_dates_plus_week():
    assert get_dates_plus_week(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]
    assert get_dates_plus_week([]) == []