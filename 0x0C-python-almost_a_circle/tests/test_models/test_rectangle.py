#!/usr/bin/python3
"""This module contains unit tests for Rectangle"""


import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class tests the Rectangle class"""

    def test_rectangle_2_args(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_4_args(self):
        rect = Rectangle(1, 2, 1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_rectangle_5_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)

    def test_area(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.area(), 2)

    def test_str(self):
        rect = Rectangle(1, 2, 0, 0, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 1/2")

    def test_display(self):
        def display_4_args(mock_print):
            rect = Rectangle(1, 1, 1, 1)
            rect.display()
            mock_print.assert_called_with(1, 1, 1, 1)

    def test_rectangle_type_error(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")

    def test_rectangle_val_error(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -4)
