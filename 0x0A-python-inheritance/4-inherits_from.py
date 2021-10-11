#!/usr/bin/pytñhon3

"""
Verify if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """Verifi if obj is a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
