# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию update_product_info(), которая обновляет информацию о продукте
# по его имени и возвращает обновленный список продуктов.
#
# Функция принимает следующие аргументы: список продуктов, имя продукта,
# информацию, по которому нужно обновить, и словарь с данными, которые требуется обновить.
# За один вызов функция может обновить только один продукт.
# Если продукт не найден в списке, функция возвращает строку
# «Продукт с таким именем не найден в списке».
# Если у продукта отсутствует имя, это не должно привести к ошибке.

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

def update_product_info(products, product_to_update,
                        new_info):  ## 1. список продуктов, 2. имя продукта, 3. информация по обновлению,

    all_name = []  ## создаем список куда поллжим все имена из "products", для определения ложных имен.

    for product in products:  ## создаем цикл для перебора вложенных словарей, 1 словарь это product.
        product_name = product.get('name')

        if product_name == product_to_update:  ## логическое условие совпадения имени в словаре и имени из аргумента №2
            all_name.append(product_name)
            for key, value in new_info.items():
                product[key] = value

    if not all_name:  ## условие если полученное имя не найдена в products_list.
        return "Продукт с таким именем не найден в списке"

    else:

        return products



product_to_update = "Banana"
new_info = {"quantity": 10, "organic": False}
update_result = update_product_info([{"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
                                     {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5}, ],
                                    product_to_update, new_info)
print(update_result)

