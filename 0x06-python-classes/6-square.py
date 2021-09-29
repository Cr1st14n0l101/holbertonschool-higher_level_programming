#!/usr/bin/python3
"""Create a class Square"""


class Square:
    "class Square"

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) or len(value) != 2:
            if not isinstance(value[0], int) and not isinstance(value[1], int):
                raise TypeError
            ("position must be a tuple of 2 positive integers")
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        self.__area = self.__size ** 2
        return self.__area

    def my_print(self):
        if self.__size <= 0:
            print("")
            return
        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
