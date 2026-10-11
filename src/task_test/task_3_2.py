# Написать функцию, которая получает на вход список кортежей,
# содержащих информацию о товарах (например, название, цена,
# количество и т. д.), и возвращает новый список,
# отсортированный по убыванию цены.
# Пример ввода:
# [(apple, 2.5), (banana, 3.5), (orange, 1.5)]
#
# Пример вывода:
# [(banana, 3.5), (apple, 2.5), (orange, 1.5)]


def products_sort(products_list):
    return sorted(products_list, key=lambda x: x[1], reverse=True)


resultat = products_sort([("apple", 2.5), ("banana", 3.5), ("orange", 1.5)])
print(resultat)
