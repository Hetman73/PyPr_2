# Написать функцию, которая получает на вход список
# строк и возвращает новый список, содержащий только
# уникальные строки.
# Пример ввода:
# ['apple', 'banana', 'orange', 'apple']
#
# Пример вывода:
# ['apple', 'banana', 'orange']


def list_set(list):
    new_list = set(list)
    return new_list


result = list_set(["apple", "banana", "orange", "apple"])
print(result)
