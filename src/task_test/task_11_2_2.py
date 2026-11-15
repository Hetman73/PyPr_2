"""Создайте декоратор
@positive_integers
, который проверяет, что все аргументы функции — положительные целые числа.
Если аргумент — неположительное число, выбрасывается исключение ValueError с сообщением
All arguments must be positive integers
.
Пример использования:

@positive_integers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

multiply(2, 3, 4) # Вывод: 24
multiply(2, 0, 4) # Выбрасывает исключение ValueError с сообщением
"All arguments must be positive integers" """

from functools import wraps


def positive_numbers(func):
    """Декоратор: проверяет, что все позиционные аргументы — положительные числа."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if isinstance(arg, bool) or not isinstance(arg, (int, float)):
                raise TypeError(f"Аргумент {i} не является числом: {arg!r}")
            if arg <= 0:
                raise ValueError(f"Аргумент {i} должен быть положительным: {arg!r}")
        return func(*args, **kwargs)
    return wrapper


@positive_numbers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(multiply(2, 3, 4))   # 24
print(multiply(2, 0, 4))   # ValueError: Аргумент 1 должен быть положительным: 0
print(multiply(2, "3"))    # TypeError: Аргумент 1 не является числом: '3')


"""Создайте декоратор 
@is_palindrome
, который проверяет, что аргумент функции является палиндромом 
(строкой, которая читается одинаково слева направо и справа налево). 
Если аргумент не является палиндромом, выбрасывается исключение ValueError с сообщением 
Argument must be a palindrome
.
Пример использования:

@is_palindrome
def reverse_string(string):
    return string[::-1]

reverse_string('racecar') # "racecar"
reverse_string('Racecar') # "racecaR"
reverse_string('hello') # Выбрасывает исключение ValueError с сообщением 
"Argument must be a palindrome" """


def is_palindrome(func):
    """Декоратор: проверяет, что все позиционные аргументы — палиндромы."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if not isinstance(arg, str):
                raise TypeError(f"Аргумент {i} должен быть строкой: {arg!r}")
            if arg.lower() != arg.lower()[::-1]:
                raise ValueError(f"Argument must be a palindrome")
        return func(*args, **kwargs)
    return wrapper


@is_palindrome
def reverse_string(string):
    return string[::-1]

print(reverse_string('racecar')) # "racecar"
print(reverse_string('Racecar')) # "racecaR"
print(reverse_string('hello')) # Выбрасывает исключение ValueError с сообщением
"Argument must be a palindrome"


"""Создайте декоратор 
@logging
, который будет логировать вызовы функции и ее результат. Лог должен выводиться на экран.
Пример вывода:

@logging
def multiply(x, y):
    return x * y
multiply(2, 3) 
>>> Function multiply called with args: (2, 3) and kwargs: {}. Result: 6"""

from functools import wraps

def logging(func):
    """Декоратор: логирует вызовы функции и ее результат."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with args: {args}, and kwargs: {kwargs}. Result: {result}")
        return result
    return wrapper



@logging
def multiply(x, y):
    return x * y
multiply(2, 3)


"""Создайте декоратор 
@memoize
, который кеширует результаты функции для определенных аргументов. Если функция вызывается 
с теми же аргументами, что и в предыдущий раз, она должна возвращать результат из кеша, 
а не вычислять его заново.
Также создайте два дополнительных декоратора:

@slowit(n)
 — декоратор с параметрами, которые замедляют работу функции на 
n
 секунд. Без параметров декоратор замедляет функцию на 1 секунду. В декораторе используется функция 
time.sleep(n)
."""


import time
from functools import wraps, reduce


def timeit(func):
    """Замеряет время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__}{args} took {elapsed:.4f} sec -> {result}")
        return result
    return wrapper


def memoize(func):
    """Кеширует результаты функции по аргументам."""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # ключ кеша: позиционные + именованные аргументы
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"[cache hit] {func.__name__}{args}")
            return cache[key]
        print(f"[cache miss] {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    wrapper.cache = cache  # полезно для отладки/очистки
    return wrapper


def slowit(n=1):
    """Замедляет функцию на n секунд. По умолчанию — на 1 секунду.

    Работает как с параметром (@slowit(2)), так и без (@slowit).
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(n)
            return func(*args, **kwargs)
        return wrapper

    # Поддержка использования без параметров: @slowit
    if callable(n):
        func = n
        n = 1
        return decorator(func)

    return decorator


@timeit
@slowit(2)
def product(n):
    return reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else None

product(10)
product(10)