""" Напишите функцию, которая получает список пользователей из API, сохраняет его в JSON-файл и добавляет в
файл логов дату и время запроса.
Ссылка на API: https://jsonplaceholder.typicode.com/users.

Пример содержимого файла
log.txt
:

INFO:root:Request time: 2022-10-22 14:30:05
INFO:root:Request time: 2022-10-22 14:45:12 """
import json
import logging
import requests
from datetime import datetime
from src.config import BASE_URL_JP

# Получаем логгер
logger = logging.getLogger(__name__)


def get_list_user_api() -> list:
    """
    Получает список пользователей из API и логирует время запроса в файл.
    """
    logger.info(f"Отправлен запрос: '{BASE_URL_JP}'")

    try:
        # 1. Засекаем время запроса
        request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 2. Отправляем GET-запрос
        response = requests.get(BASE_URL_JP, timeout=30)

        print("Статус-код от сервера:", response.status_code) # <--- ВЫВОДИТ 200
        response.raise_for_status() # <--- проверяет 200, Если 400+, он бросает исключение, и код перескакивает в блок except.
        data = response.json()
        # результаты записываем в файл user.json
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Данные успешно записаны в users.json")

        # 3. Извлекаем username
        users = [user.get("username") for user in data if "username" in user]

        # 4. Пишем в лог именно то, что в задании
        # Обратите внимание: мы используем root логгер (logging.info),
        # чтобы имя было "root", как в вашем примере.
        logging.info(f"Request time: {request_time}")

        return users

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка сети или API: {e}")
        return []


if __name__ == '__main__':
    # --- НАСТРОЙКА ЛОГИРОВАНИЯ В ФАЙЛ ---
    # filename: имя файла (создастся в корне проекта)
    # format: "%(levelname)s:%(name)s:%(message)s" даст "INFO:root:..."
    # level: чтобы писать INFO и выше
    logging.basicConfig(
        filename='log.txt',
        filemode='a',  # 'a' - дописывать в конец, 'w' - перезаписывать каждый раз
        format='%(levelname)s:%(name)s:%(message)s',
        level=logging.INFO,
        encoding='utf-8'
    )

    result = get_list_user_api()
    print(f'При отработке запроса получено: {len(result)} пользователей')
    print(result)



