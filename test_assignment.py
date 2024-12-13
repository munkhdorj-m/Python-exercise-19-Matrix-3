import pytest
import inspect
from assignment import subtract_matrices, sum_main_diagonal, sum_rows_columns

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("matrix1, matrix2, expected", [
    ([[3, 5, 2], [7, 8, 6], [4, 1, 3]], [[1, 4, 0], [2, 3, 1], [3, 2, 1]], [[2, 1, 2], [5, 5, 5], [1, -1, 2]]),
    ([[10, 8], [6, 4]], [[5, 3], [3, 2]], [[5, 5], [3, 2]]),
    ([[12, 7, 9], [6, 5, 3], [4, 8, 10]], [[3, 5, 6], [2, 1, 3], [7, 2, 4]], [[9, 2, 3], [4, 4, 0], [-3, 6, 6]])
])
def test1(matrix1, matrix2, expected):
    assert subtract_matrices(matrix1, matrix2) == expected
    assert check_contains_loop(subtract_matrices)

@pytest.mark.parametrize("matrix, expected", [
    ([[4, 5, 6], [7, 8, 9], [1, 2, 3]], 15),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
    ([[3, 6, 9], [8, 5, 2], [1, 7, 4]], 12)
])
def test2(matrix, expected):
    assert sum_main_diagonal(matrix) == expected
    assert check_contains_loop(sum_main_diagonal)

@pytest.mark.parametrize("matrix, expected_rows, expected_columns", [
    ([[2, 4, 6], [1, 3, 5], [7, 9, 11]], [12, 9, 27], [10, 16, 22]),
    ([[1, 1, 1], [2, 2, 2], [3, 3, 3]], [3, 6, 9], [6, 6, 6]),
    ([[4, 0, 1], [9, 2, 3], [5, 6, 7]], [5, 14, 18], [18, 8, 11])
])
def test3(matrix, expected_rows, expected_columns):
    rows, columns = sum_rows_columns(matrix)
    assert rows == expected_rows
    assert columns == expected_columns
    assert check_contains_loop(sum_rows_columns)
