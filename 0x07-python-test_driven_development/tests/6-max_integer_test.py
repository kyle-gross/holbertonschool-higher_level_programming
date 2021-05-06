#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class runs unit tests for the max_integer func"""
    def test_end(self):
        """Tests the max integer on end of list (front or back)"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_middle(self):
        """Tests a max integer somewhere in the middle of a list"""
        self.assertEqual(max_integer([1, 2, 3, 2, 1]), 3)
        self.assertEqual(max_integer([1, 2, 1, 1]), 2)

    def test_random(self):
        """Tests random inputs"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, 5, -10, 10]), 10)
        self.assertRaises(TypeError, max_integer("String"))
        self.assertRaises(TypeError, max_integer((1, 2)))
        self.assertRaises(TypeError, max_integer([2.0, 1.0]))
