#!/usr/bin/python3
import json

"""Module for function load_from_json_file"""


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, 'r') as f:
        x = json.load(f)
    f.close
    return x
