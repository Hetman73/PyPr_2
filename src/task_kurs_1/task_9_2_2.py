# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию average_price_per_category(), которая принимает на вход список
# продуктов и возвращает новый словарь, где ключи — категории, а значения — средняя цена
# продуктов в каждой категории.
# Округлите результат вычисления до 1 знака после запятой.
# Если у продукта отсутствует категория, это не должно привести к ошибке.
#
# Пример вывода:
#
# {'fruit': 136.7, 'veggie': 166.7}

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

from itertools import groupby ## импортируем функцию "groupby" из модуля "intertools", понадобится для группировки.
from collections import OrderedDict ## данная функция нужна что бы изменить порядок вывода данных в словаре, иначе задача не принимается.

def average_price_per_category(products):



    sort_products = sorted(products, key=lambda product: product.get('category', '')) ## сортируем список по позиции "category", нужно для "groupby"

    new_dict = {} ## создаем пустой словарь куда все и сложим
    ## my_ordered_dict = OrderedDict()

    ## применяем функцию "groupby", т.е. отделяем в отдельный "item_list" группу по одинаковому значению в ключе "category"

    for category, items in groupby(sort_products, key=lambda product: product.get('category', '')):

                total = 0 ## пустой счетчик куда положу сумму по 'price' для расчета

                item_list = list(items)

                count_products = len(item_list) ## здесь определяем количество товара в единицах

                for i in item_list: ## цикл для подсчета суммы по ключу "price"

                    price = i.get('price')

                    if isinstance(price, (int, float)): ## проверяем что price это именно число


                         total += i.get('price')

                    if count_products > 0 and total > 0: ## защита деления на "0"



                        average_price = round(total / count_products, 1) ## вычесляем среднюю цену

                       ## [category] = average_price ## заносим данные в виде словаря в new_dict

                        new_dict[category] = average_price



    ## return (sorted(new_dict.items()))
    return new_dict

print(average_price_per_category(products))

### Предыдущий код скорее всего верен и я попытался создать универсальную функцию
### тесты все сошлись, но я не смог избавиться от вывода в алфовитном порядке,
### поэтому 2-а теста не проходили и задача в целом не защитывалась.
### В task_9_1 создана функции применима только к конкретному списку продуктов.