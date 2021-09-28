#!/usr/bin/python3
"""Create class Square"""


class Square:
    """class square"""

    def __init__(self, new_size=0):
        if isinstance(new_size, int):
            if new_size < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = new_size
        else:
            raise TypeError("size must be an integer")
