#!/usr/bin/python3
"""Create a class Square"""


class Square:
    "class Square"

    def __init__(self, new_size=0):
        self.__size = new_size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        self.__area = self.__size ** 2
        return self.__area
