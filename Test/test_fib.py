import pytest
from typing import Tuple, List
import sys
import os

root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_directory)

from functions import fibonacci


def test_def():
    assert type(5) is int
    assert 6 == 2
    print(
        """First test should return true;
          Second test should return false"""
    )


# Generate Test Data
def get_test_fibonacci_data() -> List[Tuple[int, int, int]]:
    return [(10_000, -1, 10_946)]


# Fibonacci function tests
@pytest.mark.parametrize("num1, num2, expected", get_test_fibonacci_data())
def test_fibonacci(num1, num2, expected):
    assert fibonacci(num1)[num2] == expected
    assert len(fibonacci(num1)) == 22

    assert type(fibonacci(10)) is list
