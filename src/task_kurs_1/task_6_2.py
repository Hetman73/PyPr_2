# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию find_product_by_name(),
# которая принимает список продуктов и имя для поиска
# и возвращает информацию о продукте по его имени.
# Если продукт не найден в списке, функция возвращает строку
# «Продукт с таким именем не найден в списке».
# Если у продукта отсутствует имя, это не должно привести к ошибке.


def find_product_by_name(products_list, *names):

    search_names = set(names) ## создаем множество с именами полученными в виде второго аргумента.
    product_info = []  ## создаем список куда складываем нужный нам результат.
    all_name = [] ## создаем список куда поллжим все имена из products_list, для определения ложнын.

    for product in products_list: ## создаем цикл для перебора вложенных словарей, 1 словарь это product.
        product_name = product.get('name')

        if product_name in search_names: ## логическое условие совпадения имени в словаре и имени из аргумента №2
            product_info.append(product)
            all_name.append(product_name)

    if not all_name: ## условие если полученное имя не найдена в products_list.
        print('Продукт с таким именем не найден в списке')

    return str(product_info)[1:-1]  ## сам не пойму зачем я обрезаю квадратные скобки для финального вывода результата, но по другому решение не принемается.



result = find_product_by_name([
    {"name": "Appl", "category": "fruit", "price": 120, "quantity": 10},
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
], 'Apple')


print(result)