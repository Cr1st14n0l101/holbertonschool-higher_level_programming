#!/usr/bin/python3
"""Module for test the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import io
from contextlib import redirect_stdout


class TestBaseClass(unittest.TestCase):
    """Tests method area from rectangle class"""
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_objects()

    def test_display(self):
        """Test display with valid arguments"""
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 2) + (" " * 2 + '#' * 2 + '\n') * 3
        r1 = Rectangle(2, 3, 2, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 0) + (" " * 2 + '#' * 2 + '\n') * 3
        r1 = Rectangle(2, 3, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

    def test_draw(self):
        """Test square with the size of 1"""
        f = io.StringIO()
        s = ('#' * 1 + '\n') * 1
        r1 = Rectangle(1, 1)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, 2)
            r1.display(32)

    def test_square(self):
        """Test if square is inheriting display method"""
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 4
        r1 = Square(4)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 2) + (" " * 2 + '#' * 2 + '\n') * 2
        r1 = Square(2, 2, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)
