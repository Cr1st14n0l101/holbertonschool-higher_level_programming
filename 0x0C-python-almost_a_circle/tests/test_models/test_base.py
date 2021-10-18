#!/usr/bin/python3
"""Module for test the base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Tests for the instance id from base class"""
    def test_00_base_case(self):
        """Test for a instance"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_01_base_cases(self):
        """Tests normal instances"""
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base()
        self.assertEqual(b2.id, 3)
        b3 = Base()
        self.assertEqual(b3.id, 4)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_02_giving_not_a_integer(self):
        """Tests for None case"""
        b6 = Base()
        self.assertEqual(b6.id, 6)
        b7 = Base()
        self.assertEqual(b7.id, 7)
        b8 = Base()
        self.assertEqual(b8.id, 8)
        b9 = Base(None)
        self.assertEqual(b9.id, 9)

    def test_03_arguments_in_init(self):
        """Tests for arguments exceded in the class"""
        with self.assertRaises(TypeError):
            b10 = Base(1, 2)

    def test_04_infinite_passed(self):
        """Tests when infinite is passed to the class"""
        b11 = Base(float('inf'))
        self.assertEqual(b11.id, float('inf'))

    def test_negative_numbers(self):
        """Tests for negative numbers"""
        b12 = Base(-13)
        self.assertEqual(b12.id, -13)

    def test_floats_numbers(self):
        """Tests for floats numbers"""
        b13 = Base(13.3)
        self.assertEqual(b13.id, 13.3)

    def test_float_negative_numbers(self):
        """Tests for float negative numbers"""
        b14 = Base(-13.3)
        self.assertEqual(b14.id, -13.3)

    def test_bolean_true(self):
        """Tests for bloean true"""
        b15 = Base(True)
        self.assertEqual(b15.id, 1)

    def test_bolean_false(self):
        """Tests for bolean false numbers"""
        b16 = Base(False)
        self.assertEqual(b16.id, 0)

    def test_list_01(self):
        """Tests for list"""
        b17 = Base([])
        self.assertEqual(b17.id, [])

    def test_tuple_01(self):
        """Tests for tuple"""
        b18 = Base(())
        self.assertEqual(b18.id, ())

    def test_list_02(self):
        """Tests for list"""
        b19 = Base([1])
        self.assertEqual(b19.id, [1])

    def test_tuple_02(self):
        """Tests for list"""
        b20 = Base((1))
        self.assertEqual(b20.id, 1)

    def test_list_03(self):
        """Tests for list"""
        b21 = Base([1, 2, 3])
        self.assertEqual(b21.id, [1, 2, 3])

    def test_tuple_03(self):
        """Tests for tuple"""
        b22 = Base((1, 2, 3))
        self.assertEqual(b22.id, (1, 2, 3))

    def test_strings(self):
        """Tests for string"""
        b23 = Base("python")
        self.assertEqual(b23.id, "python")

    def test_character(self):
        """Tests for characters"""
        b24 = Base('C')
        self.assertEqual(b24.id, 'C')

    def test_05_instances_with_same_id(self):
        """Tests instances with same id"""
        b25 = Base(123)
        self.assertEqual(b25.id, 123)
        b26 = Base(123)
        self.assertEqual(b26.id, 123)

    def test_06_ids_too_large(self):
        """Tests id with long numbers"""
        b27 = Base(54651513215645416546546548974486846874987889877)
        self.assertEqual(
            b27.id, 54651513215645416546546548974486846874987889877)
        b28 = Base(
            87437568947689547689576985487689547569847654756486798954)
        self.assertEqual(
            b28.id, 87437568947689547689576985487689547569847654756486798954)


if __name__ == "__main__":
    unittest.main()
