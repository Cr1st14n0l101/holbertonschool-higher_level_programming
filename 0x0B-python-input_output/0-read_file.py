#!/usr/bin/python3

"""Module for function read_file"""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end="")
        print("")
    f.closed
