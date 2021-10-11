#!/usr/bin/python3

"""Class BaseGeometry"""


class BaseGeometry:
    """Implement an area"""
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Make the area of a rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def __str__(self):
        """Print a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
