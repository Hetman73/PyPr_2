""" Напишите функцию, которая должна отфильтровать
DataFrame
, чтобы в нем остались только мужчины старше 50 лет или женщины младше 30 лет. Функция должна вернуть отфильтрованный
DataFrame
 в формате JSON. """

import csv
import json
import pandas as pd


def filter_passengers(path='data/titanic.csv'):
    df = pd.read_csv(path)
    filter_age = df.loc[((df.Sex == 'male') & (df.Age > 50)) | ((df.Sex == 'female') & (df.Age < 30))]

    return filter_age




if __name__ == '__main__':
 data = filter_passengers()

 #print(data.to_json(orient='records', force_ascii=False, indent=2)) # вывод в терминал
 # Записать прямо в файл (аналог json.dump)
 data.to_json('data/result.json', orient='records', force_ascii=False, indent=2)

