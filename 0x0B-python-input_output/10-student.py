#!/usr/bin/python3
"""Module for the class Student"""


class Student:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        new_dict = {}
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(type(i) == str for i in attrs):
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
