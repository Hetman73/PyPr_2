"""Напишите функцию, которая будет получать курс валюты на текущую дату из API ЦБ РФ и
возвращать его в формате JSON.

Используйте сайт https://www.cbr-xml-daily.ru/daily_json.js.

Пример вызова функции:

rate = get_currency_rate("USD")
print(rate)
Результат:

{
    "currency_code": "USD",
    "rate": 72.7384
}
"""

import requests
import json
import unittest
from unittest.mock import patch, MagicMock


def get_currency_rate(currency_code: str) -> str:
    """
    Получает курс валюты к рублю с API ЦБ РФ и возвращает его в формате JSON.
    """
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        # 1. Получаем данные с сайта
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверяем, что запрос успешен
        data = response.json()

        # 2. Ищем нужную валюту в словаре Valute
        # Переводим код в верхний регистр на случай, если ввели "usd"
        code_upper = currency_code.upper()

        if code_upper in data["Valute"]:
            currency_info = data["Valute"][code_upper]

            # 3. Формируем результат
            # Важно: Value - это стоимость Номинала (Nominal) в рублях.
            # Чтобы получить курс за 1 единицу, делим Value на Nominal.
            nominal = currency_info["Nominal"]
            value = currency_info["Value"]
            rate_per_one = value / nominal

            result = {
                "currency_code": code_upper,
                "rate": rate_per_one
            }
            return json.dumps(result, indent=4, ensure_ascii=False)
        else:
            return json.dumps({"error": f"Валюта {code_upper} не найдена"}, indent=4, ensure_ascii=False)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"Ошибка сети: {str(e)}"}, indent=4, ensure_ascii=False)


# Пример вызова
rate = get_currency_rate("USD")
print(rate)


class TestCurrencyRate(unittest.TestCase):

    # ТЕСТ 1: Успешное получение курса
    @patch('src.task_test.task_12_1_3.requests.get')
    def test_get_currency_rate_success(self, mock_get):
        # 1. Создаем фейковый ответ от API
        fake_response = MagicMock()
        fake_response.status_code = 200

        # Имитируем структуру данных ЦБ РФ (берем USD и JPY, так как у JPY номинал 100)
        fake_response.json.return_value = {
            "Valute": {
                "USD": {"Nominal": 1, "Value": 81.929},
                "JPY": {"Nominal": 100, "Value": 51.3372}
            }
        }
        mock_get.return_value = fake_response

        # 2. Вызываем функцию
        result_json = get_currency_rate("USD")
        result = json.loads(result_json)

        # 3. Проверяем результат
        self.assertEqual(result["currency_code"], "USD")
        self.assertEqual(result["rate"], 81.929)  # Номинал 1, поэтому делим на 1

    # ТЕСТ 2: Проверка учета номинала (самый важный тест!)
    @patch('src.task_test.task_12_1_3.requests.get')
    def test_get_currency_rate_with_nominal(self, mock_get):
        # 1. Создаем фейковый ответ
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.json.return_value = {
            "Valute": {
                "JPY": {"Nominal": 100, "Value": 51.3372}  # Номинал 100!
            }
        }
        mock_get.return_value = fake_response

        # 2. Вызываем функцию
        result_json = get_currency_rate("JPY")
        result = json.loads(result_json)

        # 3. Проверяем, что цена поделилась на номинал (51.3372 / 100 = 0.513372)
        self.assertEqual(result["currency_code"], "JPY")
        self.assertAlmostEqual(result["rate"], 0.513372, places=5)


if __name__ == '__main__':
    unittest.main()