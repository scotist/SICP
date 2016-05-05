"""Test square root module."""
import pytest
from ch1_6 import sqrt_iter

SQUARES_AND_ROOTS = [(1, 1, 1), (2, 4, 2), (3, 9, 3), (4, 16, 4), (5, 25, 5),
                     (6, 36, 6), (7, 49, 7), (1, 4, 2), (3, 4, 2), (5, 9, 3),
                     (2, 9, 3), (3, 16, 4), (7, 16, 4), (2, 25, 5),
                     (22, 25, 5), (10, 100, 10), (99, 100, 10)]

TOO_HARD = [(1, 2), (1, 3), (3, 15), (-2, 5), (3, 5), (1, 12), (9, 99)]


@pytest.mark.parametrize('nums', SQUARES_AND_ROOTS)
def test_sqrt_iter(nums):
    """Test square root finder."""
    assert sqrt_iter(nums[0], nums[1]) == nums[2]


@pytest.mark.parametrize('nums', TOO_HARD)
def test_hard_case(nums):
    """Show a number whose root is not an integer raises error."""
    with pytest.raises(RuntimeError):
        sqrt_iter(nums[0], nums[1])


def test_zero_error():
    """Show square root finder raises error when zero entered as guess."""
    with pytest.raises(ZeroDivisionError):
        sqrt_iter(0, 25)
