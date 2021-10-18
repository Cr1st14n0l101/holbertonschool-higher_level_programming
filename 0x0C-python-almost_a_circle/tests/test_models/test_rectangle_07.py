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

    def test_base_case(self):
        """Checks the update method representation"""
        file = io.StringIO()
        r1 = Rectangle(10, 10, 10, 10)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(89)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        file = io.StringIO()
        r1.update(89, 2)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

        file = io.StringIO()
        r1.update(89, 2, 3)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

        file = io.StringIO()
        r1.update(89, 2, 3, 4)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

        file = io.StringIO()
        r1.update(89, 2, 3, 4, 5)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_many_arguments(self):
        """Checks the update method representation"""
        r1 = Rectangle(10, 10, 10, 10)
        file = io.StringIO()
        r1.update(89, 2, 3, 4, 5)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

        file = io.StringIO()
        r1.update(89, 2, 3, 4, 5, 6)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_no_arguments(self):
        """Checks the update method representation"""
        r1 = Rectangle(10, 10, 10, 10)
        file = io.StringIO()
        r1.update(89, 2, 3, 4, 5)
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

        file = io.StringIO()
        r1.update()
        with redirect_stdout(file):
            print(r1)
        self.assertEqual(file.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")


if __name__ == "__main__":
    unittest.main()
