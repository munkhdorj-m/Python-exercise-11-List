import pytest
import inspect
from assignment import find_average, multiply_elements, find_smallest

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5], 3.0),
    ([10, 20, 30], 20.0),
    ([7], 7.0),
    ([2, 4, 6, 8, 10], 6.0),
    ([0, 0, 0], 0.0)
])
def test1(numbers, expected):
    assert find_average(numbers) == expected
    assert check_contains_loop(find_average)

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], 24),
    ([5, 5, 5, 5], 625),
    ([10, 20], 200),
    ([7], 7),
    ([2, 3, -1], -6)
])
def test2(numbers, expected):
    assert multiply_elements(numbers) == expected
    assert check_contains_loop(multiply_elements)

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5], 1),
    ([10, 20, 5, 30], 5),
    ([7, 7, 7, 7], 7),
    ([2, -4, 6, 8], -4),
    ([0, -1, -5, 3], -5)
])
def test3(numbers, expected):
    assert find_smallest(numbers) == expected
    assert check_contains_loop(find_smallest)
