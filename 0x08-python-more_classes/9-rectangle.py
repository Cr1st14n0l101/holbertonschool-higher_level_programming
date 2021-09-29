#!/usr/bin/python3
""""Create a Rectangle"""


class Rectangle:
    """Class Rectangle Empty"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Set the Value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Set the Value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
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
                string += str(self.print_symbol) * self.__width + "\n"
            elif i == self.height - 1:
                string += str(self.print_symbol) * self.__width
        return string

    def __repr__(self):
        """Returns an “official” string representation of an instance"""
        represent = "Rectangle({}, {})".format(self.__width, self.__height)
        return represent

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class Method that create a Square"""
        return cls(size, size)

    def __del__(self):
        """Delete all the references to the object"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
