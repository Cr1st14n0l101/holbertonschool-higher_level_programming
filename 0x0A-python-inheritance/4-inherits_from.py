#!/usr/bin/python3

"""
Verify if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """Verifi if obj is a subclass of a_class"""
    return isinstance(type(obj), a_class) or type(obj) != a_class
