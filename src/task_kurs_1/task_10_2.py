# Вам предоставлен список словарей в котором перечислены товары.
#
# Напишите функцию group_products_by_category(products),
# которая принимает на вход список продуктов и возвращает словарь,
# где ключи — категории, а значения — списки продуктов в каждой категории.
# Если у продукта отсутствует категория, это не должно привести к ошибке.
# Такой продукт игнорируется программой.

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


# Пишите свой код ниже

def group_products_by_category(products):


    new_dict = {} ## создаем пустой словарь куда все и сложим
    value_fruit = []
    value_veggie = []
    value_sweets = []

    for product in products:
        if not product or 'category' not in product: ## защита от пустого списка
            continue
        category_name = product['category']
        if category_name == 'fruit':
                value_fruit.append(product)
        elif category_name == 'veggie':
                value_veggie.append(product)
        elif category_name == 'sweets':
                value_sweets.append(product)



    if value_fruit:
        new_dict['fruit'] = value_fruit
    if value_veggie:
        new_dict['veggie'] = value_veggie
    if value_sweets:
        new_dict['sweets'] = value_sweets

    return new_dict


# grouped_by_category = group_products_by_category([{}])
# print(grouped_by_category)

grouped_by_category = group_products_by_category(products)
print(grouped_by_category)

# grouped_by_category = group_products_by_category([{"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
#                                                   {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
#                                                   {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
#                                                   {"name": "Tomato", "category": "veggie", "price": 100,
#                                                    "quantity": 20},
#                                                   {"name": "Broccoli", "category": "veggie", "price": 300,
#                                                    "quantity": 8},
#                                                   {"name": "Carrot", "category": "veggie", "price": 100,
#                                                    "quantity": 25}, ])
# print(grouped_by_category)

