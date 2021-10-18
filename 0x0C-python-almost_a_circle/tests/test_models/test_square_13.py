#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout
import json


class TestRectangleClass_dict(unittest.TestCase):

    """Test Square"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset_nb_objects()

    def test_base_case(self):
        """Checks the base case"""
        s1 = Square(10, 2, 1)
        d = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, d)

    def test_if_dictionary(self):
        """checks if the result is a dictionary"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertIsInstance(s1_dictionary, dict)

    def test_base_case(self):
        """checks the correct output for other square"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        f = io.StringIO()
        with redirect_stdout(f):
            print(s2)
        self.assertEqual(f.getvalue(), "[Square] (1) 2/1 - 10\n")

    def test_diferents_squares(self):
        """checks that squares are differents"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        f = io.StringIO()
        with redirect_stdout(f):
            print(s1 == s2)
        self.assertEqual(f.getvalue(), "False\n")

    def test_json_file(self):
        """Check the json file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(14, 2, 5, 8)
        dictionary = r1.to_dictionary()
        dictionary1 = r2.to_dictionary()
        ss = [dictionary, dictionary1]
        json_dictionary = Square.to_json_string(ss)
        self.assertEqual(ss, json.loads(json_dictionary))

    def test_argument_passed(self):
        """check when a argument is pased"""
        s1 = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            dictionary = s1.to_dictionary(32)

    def test_unexpected_keyword(self):
        """check a keyword argument is passed"""
        s1 = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            dictionary = s1.to_dictionary(width=2)

    def test_json(self):
        """test of Base.to_json_string([ { 'id': 12 }]) returning a string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(isinstance(json_dictionary, str))

    def test_json_empty(self):
        """test json empty"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Rectangle.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Square.to_json_string([])
        self.assertEqual([], json.loads(json_dictionary))

    def test_json_none(self):
        """test json"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Rectangle.to_json_string(None)
        self.assertEqual([], json.loads(json_dictionary))

        json_dictionary = Square.to_json_string(None)
        self.assertEqual([], json.loads(json_dictionary))


if __name__ == "__main__":
    unittest.main()
