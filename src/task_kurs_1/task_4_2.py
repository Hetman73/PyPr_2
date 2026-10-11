# Вам предоставлен список словарей, в котором перечислены товары.
#
# Напишите функцию calculate_total_cost(), которая принимает список продуктов
# и возвращает общую стоимость всех товаров (цена * количество).
# Если у продукта не указаны цена и/или количество, это не должно приводить к ошибке.

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



def calculate_total_cost(*fruits):

    total = 0 ## здесь будем складывать наши затраты "цена" * "количество"

    find_products = set() ## создаем множиство (что бы не было повторений) где будем складывать продукты которые мы нашли


    for product in products:
            if product['name'] in fruits:
                cost = product.get("price", 0) * product.get("quantity", 0) ## применяем метод "get" что бы в случаи отсутствия
                                                                            ## цены или количества иметь значение по умолчанию "0".
                total += cost
                find_products.add(product['name'])


     ##  определяем реакцию на ввод товара которога нет в каталогах.

    for unknown_fruit in fruits:
        if unknown_fruit not in find_products:
            print(f"{unknown_fruit} - данного товара нет в каталоге")


    return  total

result = calculate_total_cost('Apple', 'Orange')

print(result)





