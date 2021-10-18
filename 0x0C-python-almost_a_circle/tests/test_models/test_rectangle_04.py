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

    def test_base_case_01(self):
        """Test for case base 01"""
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.display(), None)

    def test_display(self):
        """Test display with valid arguments"""
        # creation of file that stores the
        # representation of display() in the future
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            # the result of display stores the content in
            # f accessing to his content with getvalue
            r1.display()
        # compare s and f
        self.assertEqual(f.getvalue(), s)

    def test_display_valid(self):
        """Test display with valid arguments"""
        file = io.StringIO()
        expected = ('#' * 32 + '\n') * 32
        r1 = Rectangle(32, 32)
        with redirect_stdout(file):
            r1.display()
        self.assertEqual(file.getvalue(), expected)

        file = io.StringIO()
        expected = ('#' * 2 + '\n') * 52
        r2 = Rectangle(2, 52)
        with redirect_stdout(file):
            r2.display()
        self.assertEqual(file.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
