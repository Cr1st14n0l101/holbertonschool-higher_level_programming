#!/usr/bin/python3

"""Module for the function append_write"""


def append_write(filename="", text=""):
    """Function that append a string to a text file"""
    with open(filename, 'a+', encoding='utf-8') as f:
        x = f.write(text)
    f.close
    return x
