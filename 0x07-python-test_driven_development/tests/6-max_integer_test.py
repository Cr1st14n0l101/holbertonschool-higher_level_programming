#!/usr/bin/python3

"""
    Test the max integer in the function max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests for sum function
    """
    def test__00_base_case(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_01_same_number(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_02_zero_number(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_03_negative_numbers(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_04_float_numbers(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([2.33, 2.10, 2.83, 2.99]), 2.99)

    def test_05_float_negative_numbers(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([2.33, 2.10, -2.83, -2.99]), 2.33)

    def test_06_float_negative_numbers(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer(), None)

    def test_07_none(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_08_infinite(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer(float('inf'))

    def test_09_Not_a_Number(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer(float('nan'))

    def test_10_Many_Arguments(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer([1], [1])

    def test_11_argument_list(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer([1, [1]])

    def test_12_argument_tuple(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([1, (1)]), 1)

    def test_13_argument_string(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer("string"), "t")

    def test_14_argument_lists_of_strings(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([["mnl"], ["abc"], ["xyz"]]), ['xyz'])

    def test_15_float(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_16_float(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

    def test_17_infinite(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer(
            [99, float('inf'), 1000, 100]), float('inf'))

    def test_18_Not_a_Number(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([99, float('nan'), 1000, 100]), 1000)

    def test_19_numeric_string(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_20_dict(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_21_string_in_list(self):
        """Test the max integer in the function max_integer"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "string"])

    def test_22_lists(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_23_one(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([98]), 98)

    def test_24_empty_list(self):
        """Test the max integer in the function max_integer"""
        self.assertEqual(max_integer([]), None)
