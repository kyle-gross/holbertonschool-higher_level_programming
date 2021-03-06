#!/usr/bin/python3
"""This module contains unit tests for Rectangle"""


import os
import io
import unittest
import unittest.mock
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
        # update() test
        rect.update(2, 2, 2, 2, 2)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 2)

    def test_rectangle_5_args(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)
        # to_dict test
        rect_dict = rect.to_dictionary()
        self.assertEqual(
            rect_dict, {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5})
        rect2 = Rectangle.create(**rect_dict)

    def test_save(self):
        file_path = "Rectangle.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        Rectangle.save_to_file(None)
        with open(file_path, "r") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(file_path))
        if os.path.exists(file_path):
            os.remove(file_path)
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 89)])
        self.assertTrue(os.path.exists(file_path))

    def test_load(self):
        file_path = "Rectangle.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(file_path))        

    def test_area(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.area(), 2)

    def test_str(self):
        rect = Rectangle(1, 2, 0, 0, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 0/0 - 1/2")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        rect = Rectangle(1, 1)
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), "#\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_all_args(self, mock_stdout):
        rect = Rectangle(1, 1, 1, 1)
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), "\n #\n")

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
