"""Написать функцию, которая получает на вход список словарей,
содержащих информацию о фильмах (например, название,
жанр, режиссер и т. д.), и возвращает новый список,
содержащий только те фильмы, которые относятся к заданному жанру.
Пример ввода:
[{title: 'The Shawshank Redemption', genre: 'Drama',
director: 'Frank Darabont'}, {title: 'The Godfather',
genre: 'Crime', director: 'Francis Ford Coppola'},
 {title: 'The Dark Knight', genre: 'Action', director:
'Christopher Nolan'}], 'Drama'

Пример вывода:
[{title: 'The Shawshank Redemption', genre:
'Drama', director: 'Frank Darabont'}]"""


def Sort_movies(dict_list, arg):
    new_list = []
    for movie in dict_list:
        if movie.get("genre") == arg:
            new_list.append(movie)
    return new_list


dict_list = [
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "director": "Frank Darabont",
    },
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
]

result = Sort_movies(dict_list, "Drama")
print(result)
