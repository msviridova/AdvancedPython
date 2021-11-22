import pytest

from my_functions import max_two


@pytest.mark.parametrize("a, b, c, expected", [
    (2, 4, 9, 13),
    (7, 12, 25, 37),
    (45, 289, 400, 689),
    (0, 0, 1, 1),
])
def test_max_two(a, b, c, expected):
    assert max_two(a, b, c) == expected


@pytest.mark.parametrize("a, b, c, expected_exception_type", [
    ("param_1", "param_2", "param_3", TypeError),
])
def test_fibonacci_error(a, b, c, expected_exception_type):
    with pytest.raises(expected_exception_type):
        max_two(a, b, c)