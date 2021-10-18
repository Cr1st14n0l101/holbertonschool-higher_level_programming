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

    def test_base_case_00(self):
        """Checks the __str__ representation"""
        file = io.StringIO()
        r1 = Rectangle(4, 6, 2, 1, 12)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_base_case_01(self):
        """Checks the __str__ representation"""
        file = io.StringIO()
        r2 = Rectangle(5, 5, 1)
        with redirect_stdout(file):
            print(r2)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")


if __name__ == "__main__":
    unittest.main()
