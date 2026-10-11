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


def average_price_per_category(products):
    new_dict = {}  ## создаем пустой словарь куда все и сложим
    value_fruit = []
    value_veggie = []
    value_sweets = []
    fruit_price_total = 0
    veggie_price_total = 0
    sweets_price_total = 0

    for product in products:
        if not product or 'category' not in product:  ## защита от пустого списка
            continue
        category_name = product['category']
        price = product.get('price', 0)

        if not isinstance(price, (int, float)):  # Проверяем, что цена — это число
            continue

        if category_name == 'fruit':
            value_fruit.append(product)
            fruit_price_total += price

        elif category_name == 'veggie':
            value_veggie.append(product)
            veggie_price_total += price

        elif category_name == 'sweets':
            value_sweets.append(product)
            sweets_price_total += price

    if value_fruit:
        new_dict['fruit'] = round(fruit_price_total / len(value_fruit), 1)
    if value_veggie:
        new_dict['veggie'] = round(veggie_price_total / len(value_veggie), 1)
    if value_sweets:
        new_dict['sweets'] = round(sweets_price_total / len(value_sweets), 1)

    return new_dict

print(average_price_per_category(products))