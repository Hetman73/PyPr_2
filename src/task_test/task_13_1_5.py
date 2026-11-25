""" Напишите функцию, которая принимает на вход
DataFrame из датасета titanic.csv
. Функция должна сгруппировать пассажиров по классу и посчитать среднюю стоимость билета и количество
пассажиров в каждом классе. Функция должна вернуть результат в виде словаря в формате JSON.
Пример JSON-файла:

{
    "1st": {
        "average_ticket_price": 84.15,
        "passenger_count": 216
    },
    "2nd": {
        "average_ticket_price": 20.66,
        "passenger_count": 184
    },
    "3rd": {
        "average_ticket_price": 13.68,
        "passenger_count": 491
    }
}

Оптсание столюцов DF:
{
    'PassengerId': '1',
    'Survived': '0',
    'Pclass': '3',
    'Name': 'Braund, Mr. Owen Harris',
    'Sex': 'male',
    'Age': '22',
    'SibSp': '1',
    'Parch': '0',
    'Ticket': 'A/5 21171',
    'Fare': '7.25',
    'Cabin': '',
    'Embarked': 'S'
}"""

import csv
import json


def get_ticket_stats_by_pclass(path='data/titanic.csv'):
    count_pclass_1 = 0
    count_pclass_2 = 0
    count_pclass_3 = 0
    average_ticket_price_1 = []
    average_ticket_price_2 = []
    average_ticket_price_3 = []


    with open(path, newline='') as file:
        reader = csv.DictReader(file)  # доступ по именам колонок
        for row in reader:
            pclass = row['Pclass']
            if not pclass:          # пустой возраст — пропускаем
                continue
            try:
                if pclass == '1':
                    count_pclass_1 += 1
                    average_ticket_price_1.append(float(row['Fare']))
                elif pclass == '2':
                    count_pclass_2 += 1
                    average_ticket_price_2.append(float(row['Fare']))
                elif pclass == '3':
                    count_pclass_3 += 1
                    average_ticket_price_3.append(float(row['Fare']))


            except ValueError:
                continue         # на всякий случай, если там мусор



    price_1_avg = sum(average_ticket_price_1) / len(average_ticket_price_1) if len(average_ticket_price_1) > 0 else 0
    price_2_avg = sum(average_ticket_price_2) / len(average_ticket_price_2) if len(average_ticket_price_2) > 0 else 0
    price_3_avg = sum(average_ticket_price_3) / len(average_ticket_price_3) if len(average_ticket_price_3) > 0 else 0


    return {'1st': {'average_ticket_price': round(price_1_avg, 2), "passenger_count": round(count_pclass_1, 2)},
            '2st': {'average_ticket_price': round(price_2_avg, 2), "passenger_count": round(count_pclass_2, 2)},
            '3st': {'average_ticket_price': round(price_3_avg, 2), "passenger_count": round(count_pclass_3, 2)}}

if __name__ == '__main__':
 data = get_ticket_stats_by_pclass()
 print(json.dumps(data, ensure_ascii=False, indent=2))

