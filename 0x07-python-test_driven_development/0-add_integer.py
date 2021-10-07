#!/usr/bin/python3

"""
    Function that add two values
"""


def add_integer(a, b=98):
    """
    Args:
        Values to add, b is 98 by default
    Raise:
        TypeError: If some value isn't a integer or float
    Return:
        The addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
