"""Approximate square root of input number."""
from ch1_3 import square


def average(x, y):
    """Find average of two positive integers."""
    return (x + y) / 2


def improve(guess, num):
    """Apply Heron's algorithm to improve square root guess."""
    return average(guess, (num / guess))


def good_enough(guess, num):
    """Determine whether approximation is good enough."""
    if abs(num - square(guess)) < 0.001:
        return 'hello'
    return 'goodbye'


def sqrt_iter(guess, num):
    """Iteratively approximate square root of desired number."""
    if good_enough(guess, num) == 'hello':
        return guess
    else:
        return sqrt_iter(improve(guess, num), num)

# This module works very well when the number and its root are both integers;
# otherwise Python doesn't handle the necessary recursion well at all.
# Scheme and Python are not equally good tools for this approach!
