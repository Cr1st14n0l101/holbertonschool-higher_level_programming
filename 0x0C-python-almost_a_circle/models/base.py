#!/usr/bin/python3
"""Module for class Base"""
import json
import os


class Base:
    """Class that have the number of objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The Constructor for class Base(super)"""
        if id is not None:
            self.id = id
        else:
            # calling Base for uptade the private attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_nb_objects():
        """Reset the number of objects"""
        Base._Base__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        new_list = []
        if list_objs is None:
            with open(cls.__name__ + ".json", 'w') as f:
                f.write("[]")
        else:
            with open(cls.__name__ + ".json", 'w') as f:
                for i in range(len(list_objs)):
                    new_list.append(cls.to_dictionary(list_objs[i]))
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(666, 666)
            instance.update(**dictionary)
            return instance
        if cls.__name__ == "Square":
            instance = cls(666)
            instance.update(**dictionary)
            return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        instances = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            line_readed = f.read()
        istances_list = cls.from_json_string(line_readed)
        for i in range(len(istances_list)):
            instances.append(cls.create(**istances_list[i]))
        return instances
