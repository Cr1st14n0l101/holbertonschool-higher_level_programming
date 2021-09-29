#!/usr/bin/python3
""""Create a Rectangle"""


class Rectangle:
    """Class Rectangle Empty"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Set the Value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Set the Value to the height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.width)

    def __str__(self):
        """
        Returns an “informal” and nicely printable
        string representation of an instance
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            if i < self.__height - 1:
                string += "#" * self.__width + "\n"
            elif i == self.height - 1:
                string += "#" * self.__width
        return string

    def __repr__(self):
        """Returns an “official” string representation of an instance"""
        represent = "Rectangle ({}, {})".format(self.__width, self.__height)
        return represent

    def __del__(self):
        print("Bye rectangle...")
