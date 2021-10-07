#!/usr/bin/python3

"""
    Prints a square with the character #
"""


def print_square(size):
    """
    Args:
        The size required for the square
    Raises:
        TypeError:
            If size isn't integer or float
            If size is float but less than zero
        ValueError:
            If size is integer but less or equal to than zero
    Return:
        Void
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        print("#" * size)
