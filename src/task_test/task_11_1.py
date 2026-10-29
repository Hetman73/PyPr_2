"""Напишите генераторное выражение, которое возвращает
 кубы четных чисел от 0 до 10."""
from os.path import join

cubes_numbers = (x**3 for x in range(11) if x % 2 == 0)
print(list(cubes_numbers))


"""Напишите функцию, которая принимает список чисел и возвращает сумму квадратов
положительных чисел в этом списке. Используйте для этого генераторное выражение."""


def sum_squares_numbers(numbers: list) -> int:

    return sum(number**2 for number in numbers if number > 0)


if __name__ == '__main__':
    print(sum_squares_numbers([1, 2, -2, -5, -4]))


"""Напишите генераторное выражение, которое возвращает буквы строки 
"hello" , но только если они являются гласными."""

vowels = "aeiouyAEIOUY"
text = "hello"

filter_vowels = (letter for letter in text if letter in vowels)
print ("".join(list(filter_vowels)))


"""Найдите среднее арифметическое всех чисел, кратных 3 или 5,
 в диапазоне от 1 до 100 включительно."""

numbers = [x for x in range(1,101) if x % 3 == 0 and x % 5 == 0]
avr = sum(numbers)/len(numbers)

print(avr)


"""Объедините несколько списков в один список, учитывая возможные дубликаты элементов."""

from itertools import chain

list_1 = ['a', 'b', 'c', 1, 2, 3]
list_2 = ['b', 'c', 'd', 3, 4, 5]

combined_list = list(chain(list_1, list_2))
combined_set = set(chain(list_1, list_2))
print(combined_list)
print(combined_set)


"""Дан список словарей. Отфильтруйте его по ключу 
age и значению 30.
 people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]"""

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]


filter_dic = list(filter(lambda x: x['age'] == 30, people))
print(filter_dic)



"""Напишите генератор, который принимает на вход последовательность чисел
и генерирует квадраты этих чисел."""


def square_generator(nums):
    for num in nums:
        yield num ** 2



"""Напишите генератор, который генерирует случайные числа в заданном диапазоне."""

import random
#from collections.abc import Generator

def random_number_generator(a: int, b: int): #-> Generator[int, None, None]:
    while True:
        yield random.randint(a, b)


if __name__ == "__main__":
    gen_random = random_number_generator(1, 10)
    print(next(gen_random))


"""Напишите генератор, который генерирует последовательность чисел по заданной формуле."""

def sequence_generator(start, formula):
    num = start
    while True:
        yield num
        num = formula(num)


if __name__ == "__main__":
    # Формула: каждое следующее число = предыдущее + 2
    gen = sequence_generator(1, lambda x: x + 2)
    for _ in range(10): # буквально повтори 10 раз.
        print(next(gen))


"""Напишите генератор, который принимает на вход два списка и генерирует элементы, 
которые есть в обоих списках."""

def duplicate_generator(a, b):
    b_set = set(b)
    for item in a:
        if item in b_set:
            yield item

if __name__ == "__main__":

    gen_dupl = duplicate_generator([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
    for _ in range(5): # буквально повтори 5 раз, т.е. результат [4, 5] покажит 5  ряз
        print(next(gen_dupl))


## другой вариант решения без использования готового метода (set(a) & set(b))

# def intersection_generator(lst1, lst2):
#     seen = set()
#     for item in lst1:
#         if item in lst2 and item not in seen:
#             seen.add(item)
#             yield item



