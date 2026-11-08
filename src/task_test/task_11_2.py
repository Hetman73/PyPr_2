from email.mime import text
from unittest import result


def integers(func):
    """Декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
    являются целыми, и округляет их до целых, если это не так."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in result]
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result

    return wrapper


@integers
def list_numbers_in(*n):
    return n


y = list_numbers_in(10.9, 'asd', 5)
print(y)

import time
from datetime import datetime


def repeating_function(func):
    """Декоратор, который повторно вызывает декорируемую функцию три раза.
    Каждый раз через три секунды, если произошла ошибка."""

    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Попытка 1...")
        try:
            result = func(*args, **kwargs)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Успех!")
            return result
        except Exception:
            for attempt in range(2, 4):  # попытки 2 и 3
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Ошибка. Ждём 3 секунды...")
                if attempt < 3:
                    time.sleep(3)

                print(f"[{datetime.now().strftime('%H:%M:%S')}] Попытка {attempt}...")
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass  # ошибка, пойдём на следующую итерацию
            raise

    return wrapper


@repeating_function
def buggy_function(n):
    print(f"Вызов функции с аргументом {n}...")
    raise ValueError("Тестовая ошибка!")  # Всегда падает
    # return n


# Вызов
try:
    buggy_function(10.9)
except ValueError:
    print("Программа поймала финальную ошибку.")


def extract_elements_list_or_tuple(func):
    """Декоратор, который позволяет возвращать элементы декорируемой функции по одному через yield,
       если эта функция возвращает список или кортеж."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) in (list, tuple):
            for element in result:
                yield element
        else:
            yield result

    return wrapper


@extract_elements_list_or_tuple
def number_list(n):
    # Функция просто формирует и ВОЗВРАЩАЕТ список
    # (или кортеж, декоратор сам разберется)
    my_list = [1, 2, 3, 4, 5] # этот список нужен что бы декоратору было что возвращать, демонстрационные данные
    print(f"Вызов функции с аргументом n={n}... Сформирован список: {my_list}")

    return my_list  #ВОЗВРАЩАЕМ СПИСОК


# --- РАБОТА С ГЕНЕРАТОРОМ (СНАРУЖИ) ---

# 1. Создаем генератор
p = number_list(10)

# 2. Достаем элементы по одному
print("--- Начинаем доставать элементы ---")
print(next(p))  # Выведет: 1
print(next(p))  # Выведет: 2
print(next(p))  # Выведет: 3




from functools import wraps


def truncate_words(length=8, sign="…"):
    """Декоратор: сокращает слова длиннее `length` символов,
    добавляя в конец сокращённого слова `sign`."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            if not isinstance(text, str):
                return text                  # не строка — не трогаем
            result = []
            for word in text.split():
                if len(word) > length:
                    result.append(word[:length] + sign)
                else:
                    result.append(word)
            return " ".join(result)
        return wrapper
    return decorator


@truncate_words(length=8, sign=".")
def get_text():
    return ("Напишите декоратор, который берет результат декорируемой функции "
            "(текст) и возвращает текст, в котором каждое слово сокращено до "
            "определенной длины. Если слово было сокращено, в конце слова ставится "
            "переданный символ. Количество символов в слове и знак в конце сокращенного "
            "слова — параметры декоратора, причем символ обязательно должен передаваться "
            "как именованный аргумент.")


print(get_text())
