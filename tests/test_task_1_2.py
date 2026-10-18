from src.task_test.task_1_2 import numbers_sort
#import pytest


def test_numbers_sort():
    assert numbers_sort([1, 2, 3, 4, 5]) == [1, 2]
