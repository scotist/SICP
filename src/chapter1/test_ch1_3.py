"""Test squares and sum of squares module."""
import pytest
from ch1_3 import square, sum_of_squares


SQUARES = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25),
           (-1, 1), (-2, 4), (-3, 9)]


@pytest.mark.parametrize('num', SQUARES)
def test_squares(num):
    """Test squares function on a series of integers."""
    assert square(num[0]) == num[1]



