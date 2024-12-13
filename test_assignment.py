import pytest
import inspect
from assignment import count_negative_numbers, find_row_with_max_sum, find_largest_difference

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("matrix, expected", [
    ([[1, -2, 3], [-4, 5, -6], [7, -8, 9]], 4),
    ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]], 9)
])
def test1(matrix, expected):
    assert count_negative_numbers(matrix) == expected
    assert check_contains_loop(count_negative_numbers)

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2),
    ([[10, 20, 30], [5, 15, 25], [1, 2, 3]], 0),
    ([[4, 5, 6], [7, 8, 9], [10, 11, 12]], 2)
])
def test2(matrix, expected):
    assert find_row_with_max_sum(matrix) == expected
    assert check_contains_loop(find_row_with_max_sum)

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8),
    ([[10, 20], [30, 40]], 30),
    ([[3, -5, 9], [7, 1, -2]], 14)
])
def test3(matrix, expected):
    assert find_largest_difference(matrix) == expected
    assert check_contains_loop(find_largest_difference)
