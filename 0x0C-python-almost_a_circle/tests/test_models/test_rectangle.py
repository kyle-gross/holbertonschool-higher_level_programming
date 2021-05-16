#!/usr/bin/python3
"""This module contains unit tests for Rectangle"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.Testcase):
    """This class tests the Rectangle class"""

    def test_rectangle_exists(self):
        rect = Rectangle(1, 2, 1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
