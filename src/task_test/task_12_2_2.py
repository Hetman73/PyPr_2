""" У вас есть API: https://jsonplaceholder.typicode.com/photos.
Напишите приложение, которое скачивает картинки заданного альбома и сохраняет в директории
photos
. Все шаги должны логироваться: от старта приложения до вывода текущего состояния и информации о завершении
приложения и общем количестве скачанных картинок.

Требования:

Все шаги приложения должны выводиться в консоль, для этого нужно использовать
logging
.
Приложение должно принимать аргументы:
album_id
 (обязательный) и
limit
 (необязательный, по умолчанию 100).
Приложение должно скачивать картинки по одной и выводить каждую в консоль с указанием имени файла и номера текущей картинки.
В конце работы приложения должна выводиться информация о завершении работы и общем количестве скачанных картинок.
Пример вывода логов в консоль:

INFO:root:Starting app...
INFO:root:Downloading album 1 images...
INFO:root:Saving image 1 to photos/1-1.jpg
INFO:root:Saving image 2 to photos/1-2.jpg
INFO:root:Saving image 3 to photos/1-3.jpg
INFO:root:Saving image 4 to photos/1-4.jpg
INFO:root:Saving image 5 to photos/1-5.jpg
INFO:root:Finished downloading images. Total images downloaded: 5 """


import os
import logging
import requests
import time
from datetime import datetime
from typing import Any

from src.config import BASE_URL_PH  # Убедитесь, что путь правильный

# Получаем логгер
logger = logging.getLogger(__name__)


def get_photo_id(album_id: Any, limit: int = 5) -> None:
    """
    Скачивает картинки заданного альбома и сохраняет в директории photo.
    """
    logger.info(f"Отправлен запрос к: {BASE_URL_PH}")

    try:
        # 1. Убедимся, что папка photo существует (если нет — создадим)
        os.makedirs('photo', exist_ok=True)

        # 2. Формируем параметры и отправляем GET-запрос за списком фото (JSON)
        params = {"albumId": album_id, "_limit": limit}
        response = requests.get(BASE_URL_PH, params=params, timeout=30)

        # 3. Проверяем статус ответа
        logger.info(f"Статус-код от сервера: {response.status_code}")
        response.raise_for_status()

        # 4. Получаем данные (список словарей)
        data = response.json()

        # 5. Проходимся по каждому фото
        for photo in data:
            photo_url = f"https://via.placeholder.com/600/92c952"  # Ссылка на саму картинку
            photo_id = photo.get("id")

            if not photo_url:
                logger.warning(f"У фото {photo_id} нет ссылки. Пропускаем.")
                continue

            logger.info(f"Скачиваем картинку ID: {photo_id}")

            # --- ДОБАВЛЯЕМ ЗАГОЛОВКИ (ВАРИАНТ 1) ---
            # Представляемся как обычный браузер, чтобы сервер не блокировал нас
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }

            # 6. Делаем ВТОРОЙ запрос, чтобы скачать саму картинку (с заголовками)
            img_response = requests.get(photo_url, headers=headers, timeout=30)
            img_response.raise_for_status()

            # 7. Сохраняем в файл (в бинарном режиме 'wb')
            file_path = os.path.join('photo', f'image_{photo_id}.jpg')
            with open(file_path, 'wb') as file:
                file.write(img_response.content)

            logger.info(f"Сохранено: {file_path}")

            # Небольшая пауза, чтобы не спамить сервер запросами
            time.sleep(0.5)

        print(f"Успешно скачано {len(data)} картинок в папку 'photo/'")

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка сети или API: {e}")
    except Exception as e:
        logger.error(f"Непредвиденная ошибка: {e}")


if __name__ == '__main__':
    # Настраиваем логирование для вывода в консоль (если у вас нет своего logger_config)
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s:%(name)s:%(message)s'
    )

    # Вызываем функцию (например, для 1-го альбома, скачать 3 картинки)
    get_photo_id(album_id=1, limit=3)