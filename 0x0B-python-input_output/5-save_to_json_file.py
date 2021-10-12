#!/usr/bin/python3
import json

"""Module for function save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as f:
        chars_readed = f.write(json.dumps(my_obj))
    f.close
    return chars_readed
