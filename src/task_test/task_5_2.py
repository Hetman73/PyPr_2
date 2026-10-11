# Написать функцию, которая получает на вход
# два списка чисел и возвращает новый список,
# содержащий только те числа,
# которые встречаются в обоих списках.
# Пример ввода:
# [1, 2, 3, 4], [3, 4, 5, 6]
#
# Пример вывода:
# [3, 4]


from typing import Iterable


def master_list(arg1: Iterable[int], arg2: Iterable[int]) -> list[int]:
    """ Функция фильтрует по одинаковым позициям в списках"""
    new_list = []
    my_set1 = set(arg1)
    my_set2 = set(arg2)
    intersection_set = my_set1.intersection(my_set2)
    new_list.extend(list(intersection_set))

    return new_list





if __name__ == '__main__':
    resultat = master_list([1, 2, 3, 4], [3, 4, 5, 6])
    print(resultat)
