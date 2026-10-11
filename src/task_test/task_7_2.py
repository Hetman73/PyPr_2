# Написать функцию, которая получает на вход
# два списка чисел и возвращает новый список,
# содержащий только те числа, которые есть только
# в одном из списков.
# Пример ввода:
# [1, 2, 3, 4], [3, 4, 5, 6]
#
# Пример вывода:
# [1, 2, 5, 6]


def list_numbers_ind(arg1: list[int], arg2: list[int]) -> list[int]:
    """Функция создает новый список с индивидуальными данными списка"""
    new_list = []
    for number in arg1:
        if number not in arg2:
            new_list.append(number)
    for num in arg2:
        if num not in arg1:
            new_list.append(num)

    return new_list


if __name__ == "__main__":
    result = list_numbers_ind([1, 2, 3, 4], [3, 4, 5, 6])
    print(result)
