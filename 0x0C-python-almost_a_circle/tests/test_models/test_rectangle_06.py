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
        """Checks the display method"""
        file = io.StringIO()
        expected = "\n" * 2 + ((' ' * 2 + '#' * 2 + '\n') * 3)
        r1 = Rectangle(2, 3, 2, 2)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)

    def test_base_case_01(self):
        """Checks the display method"""
        file = io.StringIO()
        expected = "\n" * 0 + ((' ' * 1 + '#' * 3 + '\n') * 2)
        r1 = Rectangle(3, 2, 1, 0)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
