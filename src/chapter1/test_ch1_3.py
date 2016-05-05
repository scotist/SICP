"""Test squares and sum of squares module."""
import pytest
from ch1_3 import square, sum_of_squares, square_of_largest


SQUARES = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25),
           (-1, 1), (-2, 4), (-3, 9)]

SQUARE_SUMS = [(0, 0, 0), (1, 1, 2), (1, 2, 5), (2, 3, 13),
               (-1, -2, 5), (5, 6, 61)]

LARGER_SQUARE_SUMS = [(0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 1, 2), (1, 2, 3, 13),
                      (2, 3, 4, 25), (-2, -1, 5, 26), (2, -14, 0, 4),
                      (4, 3, 1, 25), (2, 5, 3, 34), (-3, 15, 2, 229)]


@pytest.mark.parametrize('num', SQUARES)
def test_squares(num):
    """Test squares function on a series of integers."""
    assert square(num[0]) == num[1]


@pytest.mark.parametrize('nums', SQUARE_SUMS)
def test_sum_of_squares(nums):
    """Test sum of squares function on a series of inputs."""
    assert sum_of_squares(nums[0], nums[1]) == nums[2]


@pytest.mark.parametrize('nums', LARGER_SQUARE_SUMS)
def test_square_of_largest(nums):
    """Test square of largest function on a series of inputs."""
    assert square_of_largest(nums[0], nums[1], nums[2]) == nums[3]
