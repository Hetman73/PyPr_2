# Написать функцию, которая получает на вход список чисел и возвращает новый
# список, содержащий только числа, которые меньше среднего значения списка.
# Пример ввода:
# [1, 2, 3, 4, 5]
#
# Пример вывода:
# [1, 2]


def numbers_sort(numbers):
    new_list = []
    len_numbers_sort = len(numbers)
    numbers_sum = sum(numbers)
    avg_numbers = numbers_sum / len_numbers_sort
    for number in numbers:
        if number < avg_numbers:
            new_list.append(number)

    return new_list


resultat = numbers_sort([1, 2, 3, 4, 5])
print(resultat)
