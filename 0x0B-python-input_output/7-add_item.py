#!/usr/bin/python3
"""Script that adds all arguments to a Python list"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_ = []
list_argv = sys.argv
list_argv.pop(0)
filename = "add_item.json"
if os.path.exists(filename):
    list_ = load_from_json_file(filename)
    for i in list_argv:
        list_.append(i)
save_to_json_file(list_, filename)
