#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
    except ZeroDivisionError as div_zero:
        print("Exception: {}".format(div_zero), file=sys.stderr)
        return None
    except IndexError as out_index:
        print("Exception: {}".format(out_index), file=sys.stderr)
        return None
    return result
