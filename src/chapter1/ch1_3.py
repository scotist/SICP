"""Sum of squares of two largest inputs."""


def square(n):
    """Given a number, return its square."""
    return n * n


def sum_of_squares(x, y):
    """Return sum of squares of parameters."""
    return square(x) + square(y)


def square_of_largest(x, y, z):
    """Return the sum of the squares of the larger two of three numbers."""
    if x <= y and x <= z:
        return sum_of_squares(y, z)
    elif y <= x and y <= z:
        return sum_of_squares(x, z)
    elif z <= x and z <= y:
        return sum_of_squares(x, y)
