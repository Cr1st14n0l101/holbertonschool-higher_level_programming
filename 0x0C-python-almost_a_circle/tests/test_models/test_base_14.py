#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout
import json


class TestRectangleClass_dict(unittest.TestCase):

    """Test Square"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset_nb_objects()


if __name__ == "__main__":
    unittest.main()
