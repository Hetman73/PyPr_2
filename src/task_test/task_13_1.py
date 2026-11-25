""" Напишите функцию, которая принимает на вход
DataFrame
 из датасета
titanic.csv
. Функция должна вычислить средний возраст мужчин и женщин отдельно и вернуть результат в виде
словаря в формате JSON. """

import csv
import json


def avg_age_by_sex(path='data/titanic.csv'):
    male_ages = []
    female_ages = []

    with open(path, newline='') as file:
        reader = csv.DictReader(file)  # доступ по именам колонок
        for row in reader:
            age = row['Age']
            if not age:          # пустой возраст — пропускаем
                continue
            try:
                age = float(age)
            except ValueError:
                continue         # на всякий случай, если там мусор

            if row['Sex'] == 'male':
                male_ages.append(age)
            elif row['Sex'] == 'female':
                female_ages.append(age)

    male_avg = sum(male_ages) / len(male_ages) if len(male_ages) > 0 else 0
    female_avg = sum(female_ages) / len(female_ages) if len(female_ages) > 0 else 0

    return {'male_avg_age': round(male_avg, 2), 'female_avg_age': round(female_avg, 2)}

if __name__ == '__main__':
 data = avg_age_by_sex()
 print(json.dumps(data, ensure_ascii=False, indent=2))

