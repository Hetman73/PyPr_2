# Написать функцию, которая получает на вход
# список чисел и возвращает новый список, содержащий
# только числа, которые являются палиндромами.
# Пример ввода:
# [121, 123, 131, 34543]
#
# Пример вывода:
# [121, 131, 34543]


def list_palindrome(numbers: list[int]) -> list[int]:
    """Функция возвращает новый список с палидромами"""
    new_list = []
    for number in numbers:
        str_1 = str(number)
        str_2 = str_1[::-1]
        if str_1 == str_2:
            new_list.append(number)
    return new_list


if __name__ == "__main__":
    result = list_palindrome([121, 123, 131, 34543])
    print(result)
