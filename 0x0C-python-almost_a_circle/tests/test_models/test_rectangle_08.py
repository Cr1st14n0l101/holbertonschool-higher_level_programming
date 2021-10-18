#!/usr/bin/python3
"""Module for test the rectangle class"""
from typing import TYPE_CHECKING
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

    def test_base_case(self):
        """Check the base case"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(2, height=1)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (2) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update()
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (2) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(y=1, width=2, x=3, id=89)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 3/1 - 2/10\n")

        file = io.StringIO()
        r1.update(x=1, height=2, y=3, width=4)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 1/3 - 4/2\n")

    def test_args_and_no_keys(self):
        """Checks the behavior when arg is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(2, height=1)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (2) 10/10 - 10/10\n")

    def test_only_keys(self):
        """Checks the behavior when arg is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(y=1, width=2, x=3, id=89)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 3/1 - 2/10\n")

    def test_one_key_(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(width=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 2/10\n")

    def test_two_keys_(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(width=2, height=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 2/2\n")

    def test_three_keys_(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(width=2, height=2, x=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 2/10 - 2/2\n")

    def test_four_keys_(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(width=2, height=2, x=2, y=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 2/2 - 2/2\n")

    def test_five_keys_(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(width=2, height=2, x=2, y=2, id=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (2) 2/2 - 2/2\n")

    def test_six_keys_(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(width=2, height=2, x=2, y=2, id=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (2) 2/2 - 2/2\n")

    def test_key_unknown(self):
        """Checks the behavior when a key is passed"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(something=2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")


if __name__ == "__main__":
    unittest.main()
