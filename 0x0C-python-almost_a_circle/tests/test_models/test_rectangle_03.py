#!/usr/bin/python3
"""Module for test the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests method area from rectangle class"""
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_objects()

    def test_base_cases(self):
        """Tests for base cases"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_base_cases(self):
        """Tests when argumens is passed to area"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 2)
            self.assertEqual(r1.area(2343456436), 6)


if __name__ == "__main__":
    unittest.main()
