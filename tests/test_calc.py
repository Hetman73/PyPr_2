
from cals import add, subtract, multiply, divide
from cals import reverse_string
import pytest


# Тест функции сложения
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0

# Тест функции вычитания
def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2, 3) == -5
    assert subtract(0, 0) == 0

# Тест функции умножения
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 0) == 0

# Тест функции деления
def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


@pytest.mark.parametrize("string, expected_result", [
    ("hello", "olleh"),
    ("world", "dlrow"),
    ("12345", "54321"),
    ("", ""),
])
def test_reverse_string(string, expected_result):
    assert reverse_string(string) == expected_result