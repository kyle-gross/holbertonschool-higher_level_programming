#!/usr/bin/python3
"""This module contains unit tests for Rectangle"""


import os
import io
import unittest
import unittest.mock
from models.square import Square


class TestSquare(unittest.TestCase):
    """This class tests the Rectangle class"""

    def test_square_1_arg(self):
        s = Square(1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)

    def test_square_3_args(self):
        s = Square(1, 1, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
        # update() test
        s.update(2, 2, 2, 2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 2)

    def test_square_4_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        # to_dict test
        sq_dict = s.to_dictionary()
        self.assertEqual(
            sq_dict, {'size': 1, 'x': 2, 'y': 3, 'id': 4})
        s2 = Square.create(**sq_dict)

    def test_save(self):
        file_path = "Square.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        Square.save_to_file(None)
        with open(file_path, "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        self.assertTrue(os.path.exists(file_path))
        if os.path.exists(file_path):
            os.remove(file_path)
        Square.save_to_file([Square(1, 0, 0, 89)])
        self.assertTrue(os.path.exists(file_path))

    def test_load(self):
        file_path = "Square.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertTrue(os.path.exists(file_path))        

    def test_area(self):
        s = Square(1)
        self.assertEqual(s.area(), 1)

    def test_str(self):
        s = Square(1, 2, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 1")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        s = Square(1)
        s.display()
        self.assertEqual(mock_stdout.getvalue(), "#\n")

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_all_args(self, mock_stdout):
        s = Square(1, 1, 1)
        s.display()
        self.assertEqual(mock_stdout.getvalue(), "\n #\n")

    def test_square_type_error(self):
        with self.assertRaises(TypeError):
            s = Square("1")
        with self.assertRaises(TypeError):
            s = Square(1, "2")
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

    def test_square_val_error(self):
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(-1)
        with self.assertRaises(ValueError):
            s = Square(1, -2)
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)
