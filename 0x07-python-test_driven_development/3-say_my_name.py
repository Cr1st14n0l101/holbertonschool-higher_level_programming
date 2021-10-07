#!/usr/bin/python3

"""
    Functions the prints two strings
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        String 1 and string 2
    Raises:
        TypeError:
            If some of the strings are not str type
    Return:
        Void
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
