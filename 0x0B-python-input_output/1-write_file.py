#!/usr/bin/python3

"""Module for the function write_file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, 'w+', encoding='utf-8') as f:
        x = f.write(text)
    f.close
    return x
