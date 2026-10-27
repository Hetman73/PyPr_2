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








