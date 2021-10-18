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
        """Checks the base cases"""
        try:
            r01 = Rectangle(10, "2")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")
        try:
            r02 = Rectangle(10, 2)
            r02.width = -10
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")
        try:
            r03 = Rectangle(10, 2)
            r03.x = {}
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")
        try:
            r04 = Rectangle(10, 2, 3, -1)
        except ValueError as e:
            self.assertEqual(str(e), "y must be >= 0")

    def test_01_string_argument_height(self):
        """Checks when height is string"""
        try:
            r1 = Rectangle(10, "2")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_02_string_argument_witdh(self):
        """Checks when width is string"""
        try:
            r2 = Rectangle("10", 2)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_03_string_argument_x(self):
        """Checks when x is string"""
        try:
            r14 = Rectangle(10, 2, "str", 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_04_string_argument_y(self):
        """Checks when y is string"""
        try:
            r15 = Rectangle(10, 2, 11, "str")
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_05_negative_argument_width(self):
        """Checks when width is a negative integer"""
        try:
            r3 = Rectangle(-10, 2)
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")

    def test_06_negative_argument_height(self):
        """Checks when height is a negative integer"""
        try:
            r4 = Rectangle(10, -2)
        except ValueError as e:
            self.assertEqual(str(e), "height must be > 0")

    def test_07_negative_argument_x(self):
        """Checks when x is a negative integer"""
        try:
            r7 = Rectangle(10, 2, -1, 1)
        except ValueError as e:
            self.assertEqual(str(e), "x must be >= 0")

    def test_08_negative_argument_y(self):
        """Checks when y is a negative integer"""
        try:
            r8 = Rectangle(10, 2, 1, -1)
        except ValueError as e:
            self.assertEqual(str(e), "y must be >= 0")

    def test_09_zero_arguments_width(self):
        """Checks when width is 0"""
        try:
            r5 = Rectangle(0, 2)
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")

    def test_10_zero_arguments_height(self):
        """Checks when height is 0"""
        try:
            r6 = Rectangle(10, 0)
        except ValueError as e:
            self.assertEqual(str(e), "height must be > 0")

    def test_11_zero_arguments_x_and_y(self):
        """Checks when x and y are 0"""
        r9 = Rectangle(10, 2, 0, 0)
        self.assertEqual([r9.width, r9.height, r9.x, r9.y],
                         [10, 2, 0, 0])

    def test_12_changing_x(self):
        """Checks when x is changed"""
        try:
            r10 = Rectangle(10, 2, 11, 11)
            r10.x = -11
        except ValueError as e:
            self.assertEqual(str(e), "x must be >= 0")

    def test_13_changing_y(self):
        """Checks when y is changed"""
        try:
            r11 = Rectangle(10, 2, 11, 11)
            r11.y = -11
        except ValueError as e:
            self.assertEqual(str(e), "y must be >= 0")

    def test_14_changing_width(self):
        """Checks when witdh is changed"""
        try:
            r12 = Rectangle(10, 2, 11, 11)
            r12.width = 0
        except ValueError as e:
            self.assertEqual(str(e), "width must be > 0")

    def test_15_changing_height(self):
        """Checks when height is changed"""
        try:
            r13 = Rectangle(10, 2, 11, 11)
            r13.height = 0
        except ValueError as e:
            self.assertEqual(str(e), "height must be > 0")

    def test_16_float_x(self):
        """Checks when x is float"""
        try:
            r16 = Rectangle(10, 2, 11.12, 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_17_float_y(self):
        """Checks when y is float"""
        try:
            r17 = Rectangle(10, 2, 11, 11.12)
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_18_float_width(self):
        """Checks when width is float"""
        try:
            r30 = Rectangle(10.11, 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_19_float_height(self):
        """Checks when height is float"""
        try:
            r31 = Rectangle(10, 2.11, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_20_list_x(self):
        """Checks when x is a list"""
        try:
            r22 = Rectangle(10, 2, [11], 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_21_list_y(self):
        """Checks when y is a list"""
        try:
            r23 = Rectangle(10, 2, 11, [11])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_22_list_x(self):
        """Checks when x is a list"""
        try:
            r24 = Rectangle(10, 2, [1, 2], 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_23_list_y(self):
        """Checks when y is a list"""
        try:
            r25 = Rectangle(10, 2, 11, [1, 2])
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_24_list_width(self):
        """Checks when width is a list"""
        try:
            r32 = Rectangle([10], 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_25_list_height(self):
        """Checks when height is a list"""
        try:
            r33 = Rectangle(10, [2], 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_26_list_width(self):
        """Checks when width is a list"""
        try:
            r34 = Rectangle([10, 2], 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_27_list_height(self):
        """Checks when height is a list"""
        try:
            r35 = Rectangle(10, [2, 10], 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_28_tuple_x(self):
        """Checks when x is a tuple"""
        r26 = Rectangle(10, 2, (11), 11)
        self.assertEqual([r26.width, r26.height, r26.x, r26.y],
                         [10, 2, 11, 11])

    def test_29_tuple_y(self):
        """Checks when y is a tuple"""
        r27 = Rectangle(10, 2, 11, (11))
        self.assertEqual([r27.width, r27.height, r27.x, r27.y],
                         [10, 2, 11, 11])

    def test_30_tuple_x(self):
        """Checks when x is a tuple"""
        try:
            r28 = Rectangle(10, 2, (1, 2), 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_31_tuple_y(self):
        """Checks when y is a tuple"""
        try:
            r29 = Rectangle(10, 2, 11, (1, 2))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_32_tuple_width(self):
        """Checks when width is a tuple"""
        r36 = Rectangle((10), 2, 11, 11)
        self.assertEqual([r36.width, r36.height, r36.x, r36.y],
                         [10, 2, 11, 11])

    def test_33_tuple_height(self):
        """Checks when height is a tuple"""
        r37 = Rectangle(10, (2), 11, 11)
        self.assertEqual([r37.width, r37.height, r37.x, r37.y],
                         [10, 2, 11, 11])

    def test_34_tuple_width(self):
        """Checks when width is a tuple"""
        try:
            r38 = Rectangle((10, 2), 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_35_tuple_height(self):
        """Checks when height is a tuple"""
        try:
            r39 = Rectangle(10, (10, 2), 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_36_dictionary_height(self):
        """Checks when height is a tuple"""
        try:
            r40 = Rectangle(10, {10: 2}, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_37_dictionary_width(self):
        """Checks when height is a dictionary"""
        try:
            r41 = Rectangle({10: 2}, 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_38_dictionary_x(self):
        """Checks when height is a dictionary"""
        try:
            r40 = Rectangle(10, 2, {10: 2}, 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_39_dictionary_y(self):
        """Checks when x is a dictionary"""
        try:
            r41 = Rectangle(10, 2, 11, {10: 2})
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_40_infinite_width(self):
        """Checks when width is a dictionary"""
        try:
            r42 = Rectangle(float('inf'), 2, 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_41_infinite_height(self):
        """Checks when height is a dictionary"""
        try:
            r43 = Rectangle(10, float('inf'), 11, 11)
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_42_infinite_x(self):
        """Checks when x is a dictionary"""
        try:
            r18 = Rectangle(10, 2, float('inf'), 11)
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_43_infinite_y(self):
        """Checks when y is a dictionary"""
        try:
            r19 = Rectangle(10, 2, 11, float('inf'))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")

    def test_45_not_a_number_width(self):
        """Checks when width is not a number"""
        try:
            Rectangle(float('nan'), 2)
        except TypeError as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_46_not_a_number_height(self):
        """Checks when height is not a number"""
        try:
            Rectangle(10, float('nan'))
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_46_not_a_number_x(self):
        """Check when x is not a number"""
        try:
            Rectangle(10, 2, float('nan'))
        except TypeError as e:
            self.assertEqual(str(e), "x must be an integer")

    def test_46_not_a_number_y(self):
        """Check when y is not a number"""
        try:
            Rectangle(10, 2, 11, float('nan'))
        except TypeError as e:
            self.assertEqual(str(e), "y must be an integer")


if __name__ == "__main__":
    unittest.main()
