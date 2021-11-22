import pytest

from my_functions import fibonacci_func


@pytest.mark.parametrize("num, expected", [
    (1, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    (4, [4, 7, 11, 18, 29, 47, 76, 123, 199, 322]),
    (5, [5, 9, 14, 23, 37, 60, 97, 157, 254, 411]),
    (10, [10, 19, 29, 48, 77, 125, 202, 327, 529, 856]),
    (7, [7, 13, 20, 33, 53, 86, 139, 225, 364, 589]),
    (0, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test_fibonacci_func(num, expected):
    assert fibonacci_func(num) == expected


@pytest.mark.parametrize("num, expected_exception_type", [
    ("param_1", TypeError),
    (1.1, TypeError),
])
def test_fibonacci_error(num, expected_exception_type):
    with pytest.raises(expected_exception_type):
        fibonacci_func(num)
