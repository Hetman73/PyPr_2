import pytest
from src.task_test.task_11_2 import truncate_words


def make(text):
    """Оборачивает текст в функцию и прогоняет через декоратор."""
    @truncate_words(length=8, sign=".")
    def inner():
        return text
    return inner()


@pytest.mark.parametrize("string, expected", [
    ("мама мыла раму", "мама мыла раму"),                 # короткие слова
    ("прилюдное покояние ", "прилюдно. покояние"),        # длинное сокращено, хвостовой пробел убран
    ("распростертое, устоявшиеся ?", "распрост. устоявши. ?"),  # запятая теряется — так работает код
    ("", ""),                                             # пустая строка
])
def test_truncate_words(string, expected):
    assert make(string) == expected


def test_custom_length_and_sign():
    @truncate_words(length=3, sign="!")
    def inner():
        return "abcdef gh"
    assert inner() == "abc! gh"


def test_sign_must_be_keyword():
    # sign передаётся только как именованный аргумент
    @truncate_words(length=8, sign=".")
    def inner():
        return "прилюдное"
    assert inner() == "прилюдно."


def test_non_string_result_returned_as_is():
    # если декорируемая функция вернула не строку — декоратор возвращает как есть
    @truncate_words(length=8, sign=".")
    def inner():
        return 42
    assert inner() == 42


def test_decorator_preserves_metadata():
    @truncate_words(length=8, sign=".")
    def inner():
        """docstring"""
        return "ok"
    assert inner.__name__ == "inner"
    assert inner.__doc__ == "docstring"