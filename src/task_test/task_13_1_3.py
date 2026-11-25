""" Напишите функцию, которая вычислит среднюю стоимость билета на пассажира для каждого класса.
Функция принимает датафрейм и должна вернуть результат в виде словаря в формате
JSON. """

import csv
import json

def avg_ticket_fare(path='data/titanic.csv'):
    ticket_fare_pclass1 = []
    ticket_fare_pclass2 = []
    ticket_fare_pclass3 = []
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Pclass'] == '1':
                ticket_fare_pclass1.append(float(row['Fare']))
            elif row['Pclass'] == '2':
                ticket_fare_pclass2.append(float(row['Fare']))
            elif row['Pclass'] == '3':
                ticket_fare_pclass3.append(float(row['Fare']))

    avg_ticket_fare_pclass1 = (sum(ticket_fare_pclass1) / len(ticket_fare_pclass1))
    avg_ticket_fare_pclass2 = (sum(ticket_fare_pclass2) / len(ticket_fare_pclass2))
    avg_ticket_fare_pclass3 = (sum(ticket_fare_pclass3) / len(ticket_fare_pclass3))

    return {'avg_ticket_fare_pclass1': round(avg_ticket_fare_pclass1, 2),
            'avg_ticket_fare_pclass2': round(avg_ticket_fare_pclass2, 2),
            'avg_ticket_fare_pclass3': round(avg_ticket_fare_pclass3, 2)}







if __name__ == '__main__':
 data = avg_ticket_fare()
 print(json.dumps(data, ensure_ascii=False, indent=2))

