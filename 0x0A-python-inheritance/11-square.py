#!/usr/bin/python3
'''Module for Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Make a square"""
    def __init__(self, size):
        """Contructor"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area"""
        return self.__size * self.__size

    def __str__(self):
        """Print a string"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
