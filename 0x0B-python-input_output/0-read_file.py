#!/bin/usr/python3

"""Module for function read_file"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data)
    f.closed
