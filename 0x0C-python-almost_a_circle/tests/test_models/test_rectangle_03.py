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

    def test_area(self):
        """Simple area test"""
        r = Rectangle(32, 2)
        self.assertEqual(r.area(), 64)

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            s1 = Rectangle(10, 5)
            s1.area(32343)
