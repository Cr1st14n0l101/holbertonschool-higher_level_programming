#!/usr/bin/python3
"""Module for test the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestBaseClass(unittest.TestCase):
    """Tests method area from rectangle class"""
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_objects()

    def test_str_defaults(self):
        """Tests __str__ method"""
        Base.reset_nb_objects()
        f = io.StringIO()
        s = "[Rectangle] (1) 0/0 - 4/3"
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (2) 32/0 - 4/3"
        r2 = Rectangle(4, 3, 32)
        with redirect_stdout(f):
            print(r2, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (3) 3/5 - 4/3"
        r3 = Rectangle(4, 3, 3, 5)
        with redirect_stdout(f):
            print(r3, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (77) 3/5 - 4/3"
        r77 = Rectangle(4, 3, 3, 5, 77)
        with redirect_stdout(f):
            print(r77, end="")
        self.assertEqual(f.getvalue(), s)
