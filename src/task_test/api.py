import requests

"""Образец запроса для конвертации валюты, сработает если будет платный аккаунт на apilayer"""

url = "https://api.apilayer.com/exchangerates_data/convert"
params = {
    "to": "RUB",
    "from": "USD",
    "amount": 100
}
headers = {
    "apikey": "rK0FmJXJPdXedni176N4rGDN4R1yLult"  # Вставьте сюда ключ из Dashboard
}

response = requests.get(url, headers=headers, params=params)
print(response.json())


"""Образец запроса для конвертации валюты, сработает при бесплатном аакаунте на apilayer
{'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 100}, 'info': {'timestamp': 1795096986, 'rate': 81.828126}, 'date': '2026-11-19', 'result': 8182.812564}
100 USD = 8182.81 RUB (по курсу 81.828126)"""

# Запрос курса USD к RUB
url = "https://api.apilayer.com/exchangerates_data/latest"
params = {
    "base": "USD",
    "symbols": "RUB"
}
headers = {
    "apikey": "rK0FmJXJPdXedni176N4rGDN4R1yLult"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

# Проверяем, что запрос успешен
if data.get('success'):
    rate = data['rates']['RUB']  # Получаем курс
    amount = 100
    result = amount * rate
    print(f"{amount} USD = {result:.2f} RUB (по курсу {rate})")
else:
    print("Ошибка:", data)


"""{'success': True, 'timestamp': 1795096986, 'base': 'EUR', 'date': '2026-11-19', 'rates': {'AED': 4.038813, 
'AFN': 70.935835, при таком запросе видим курс к базовому евро"""
import requests

url = "https://api.apilayer.com/exchangerates_data/latest"
headers = {"apikey": "rK0FmJXJPdXedni176N4rGDN4R1yLult"}
# Без base и symbols — запрашиваем всё относительно EUR
resp = requests.get(url, headers=headers)
print(resp.json())



"""Применение запроса на ресурсе https://meteotrust.ru, запрашиваем температуру в Мостовском Краснодарского"""

import requests

url = "https://meteotrust.ru/v1/current"

# Параметры запроса с координатами Мостовского
params = {
    "lat": 44.413611,
    "lon": 40.789722,
    # Можно указать, какие поля нужны (например, temperature_c)
    # "fields": "temperature_c"
}

# Ваш ключ из личного кабинета MeteoTrust
api_key = "mt_live_7dasMmRzFouTkySomgwxE0lZ15cApNiyW7v7IMufWlE".strip()
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    # Обычно температура находится в поле temperature_c
    # Структура ответа может отличаться, проверьте документацию
    print(data)
else:
    print(f"Ошибка: {response.status_code} - {response.text}")