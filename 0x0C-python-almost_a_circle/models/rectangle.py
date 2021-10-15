#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class with sizes a of rectangle"""
    @property
    def width(self):
        """Set with in the class Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            self.verificator(1, "width")
        if value <= 0:
            self.verificator(2, "width")
        self.__width = value

    @property
    def height(self):
        """Set height in the class Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            self.verificator(1, "height")
        if value <= 0:
            self.verificator(2, "height")
        self.__height = value

    @property
    def x(self):
        """Set x in the class Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            self.verificator(1, "x")
        if value < 0:
            self.verificator(3, "x")
        self.__x = value

    @property
    def y(self):
        """Set y in the class Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            self.verificator(1, "y")
        if value < 0:
            self.verificator(3, "y")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def verificator(self, key, obj):
        """Method for handle errors"""
        if key == 1:
            raise TypeError("{} must be an integer".format(obj))
        if key == 2:
            raise ValueError("{} must be > 0".format(obj))
        if key == 3:
            raise ValueError("{} must be >= 0".format(obj))

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string that represent the objects class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
            )

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        if args and args is not None:
            for position in range(len(args)):
                if position == 0:
                    self.id = args[position]
                if position == 1:
                    self.__width = args[position]
                if position == 2:
                    self.__height = args[position]
                if position == 3:
                    self.__x = args[position]
                if position == 4:
                    self.__y = args[position]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        new_dictionary = {}
        for k, v in self.__dict__.items():
            if k[:12] == "_Rectangle__":
                new_dictionary[k[12:]] = v
            else:
                new_dictionary[k] = v
        return new_dictionary
