#!/usr/bin/python3
"""Module for test the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests for the instances width, height and id from rectangle class"""
    def setUp(self):
        """Reset the number of objects"""
        Base.reset_nb_objects()

    def test_00_base_case(self):
        """Tests for id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2)
        self.assertEqual(r4.id, 3)

    def test_01_test_height_and_width(self):
        """Tests for height and width"""
        r5 = Rectangle(10, 2)
        self.assertEqual([r5.width, r5.height, r5.x, r5.y, r5.id],
                         [10, 2, 0, 0, 1])
        r6 = Rectangle(10, 2, 8, 9, 81)
        self.assertEqual([r6.width, r6.height, r6.x, r6.y, r6.id],
                         [10, 2, 8, 9, 81])
        r7 = Rectangle(44, 33)
        self.assertEqual([r7.width, r7.height], [44, 33])
        r8 = Rectangle(45, 43)
        self.assertEqual([r8.width, r8.height], [45, 43])

    def test_02_with_no_arguments(self):
        """Tests for no arguments"""
        with self.assertRaises(TypeError):
            r9 = Rectangle()
        with self.assertRaises(TypeError):
            r10 = Rectangle(32)

    def test_03_3_arguments(self):
        """Test with 3 arguments"""
        r11 = Rectangle(12, 13, 14)
        self.assertEqual([r11.width, r11.height, r11.x, r11.y, r11.id],
                         [12, 13, 14, 0, 1])

    def test_04_change_attributes_manually(self):
        """Tests changind manually the attributes"""
        r11 = Rectangle(45, 43)
        r11.width = 32
        r11.height = 11
        self.assertEqual([r11.width, r11.height], [32, 11])
        r12 = Rectangle(12, 13, 14, 15)
        r12.width = 22
        r12.height = 23
        r12.x = 24
        r12.y = 25
        self.assertEqual([r12.width, r12.height, r12.x, r12.y],
                         [22, 23, 24, 25])


if __name__ == "__main__":
    unittest.main()
