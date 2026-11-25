""" Напишите функцию, которая принимает на вход
DataFrame
 из датасета
titanic.csv
. Функция должна отфильтровать пассажиров, которые выжили в катастрофе, и записать данные об этих пассажирах в
файл в формате JSON. Функция должна вернуть количество выживших пассажиров.
Пример JSON-файла:

[
    {
        "survived": 1,
        "pclass": 1,
        "name": "Allen, Miss. Elisabeth Walton",
        "sex": "female",
        "age": 29.0,
        "sibsp": 0,
        "parch": 0,
        "ticket": "24160",
        "fare": 211.3375,
        "cabin": "B5",
        "embarked": "S"
    },
    {
        "survived": 1,
        "pclass": 1,
        "name": "Allison, Master. Hudson Trevor",
        "sex": "male",
        "age": 0.92,
        "sibsp": 1,
        "parch": 2,
        "ticket": "113781",
        "fare": 151.55,
        "cabin": "C22 C26",
        "embarked": "S"
    },
    ...
]

Оптсание столюцов DF:
{
    'PassengerId': '1',
    'Survived': '0',
    'Pclass': '3',
    'Name': 'Braund, Mr. Owen Ha
    'Sex': 'male',
    'Age': '22',
    'SibSp': '1',
    'Parch': '0',
    'Ticket': 'A/5 21171',
    'Fare': '7.25',
    'Cabin': '',
    'Embarked': 'S'
}"""

import pandas as pd


def filter_survived(path='data/titanic.csv'):
    df = pd.read_csv(path)
    filter_survived = df.loc[(df.Survived == 1)]

    return filter_survived




if __name__ == '__main__':
 data = filter_survived()
 print(data.shape)

 #print(data.to_json(orient='records', force_ascii=False, indent=2)) # вывод в терминал
 # Записать прямо в файл (аналог json.dump)
 data.to_json('data/result.json', orient='records', force_ascii=False, indent=2)






# if __name__ == '__main__':
#     data = get_ticket_stats_by_pclass()
#     print(json.dumps(data, ensure_ascii=False, indent=2))

