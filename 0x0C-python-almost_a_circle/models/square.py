#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class with sizes a of Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for class Square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string that represent the objects class"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size
            )

    @property
    def size(self):
        """Set size in the class Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            self.verificator(1, "width")
        if value < 0:
            self.verificator(2, "width")
        self.__size = value

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        if args and args is not None:
            for position in range(len(args)):
                if position == 0:
                    self.id = args[position]
                if position == 1:
                    self.width = args[position]
                    self.height = args[position]
                if position == 2:
                    self.x = args[position]
                if position == 3:
                    self.y = args[position]
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        new_dictionary = {}
        for k, v in self.__dict__.items():
            if k == "_Rectangle__width":
                continue
            elif k == "_Rectangle__height":
                continue
            elif k[:12] == "_Rectangle__":
                new_dictionary[k[12:]] = v
            elif k[:9] == "_Square__":
                new_dictionary[k[9:]] = v
            else:
                new_dictionary[k] = v
        return new_dictionary
