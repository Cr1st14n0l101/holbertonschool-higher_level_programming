#!/usr/bin/python3
class Square:
    "class Square"
    def __init__(self, new_size=0):
        if isinstance(new_size, int):
            if new_size < 0:
                raise ValueError("size must be >= 0")
            self._Square__size = new_size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        self.__area = self.__size * self.__size
        return self.__area
