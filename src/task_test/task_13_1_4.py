""" Напишите функцию, которая принимает на вход
DataFrame
 из датасета
titanic.csv
. Функция должна отфильтровать пассажиров, у которых цена билета больше 50 и возраст меньше 30 лет.
Затем функция должна отсортировать отфильтрованный
DataFrame
 по имени пассажира в алфавитном порядке и вернуть результат.
Ожидаемый результат — отфильтрованный и отсортированный
DataFrame. """

import pandas as pd


def filter_passengers(path='data/titanic.csv'):
    df = pd.read_csv(path)
    filter_age = df.loc[((df.Fare > 50) & (df.Age < 30))]

    return filter_age




if __name__ == '__main__':
 data = filter_passengers()
 print(data.shape)

 #print(data.to_json(orient='records', force_ascii=False, indent=2)) # вывод в терминал
 # Записать прямо в файл (аналог json.dump)
 data.to_json('data/result.json', orient='records', force_ascii=False, indent=2)

