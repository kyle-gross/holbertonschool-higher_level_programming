#!/usr/bin/python3
"""This module contains unittests for Base class"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """This class tests the Base class"""
    def test_id(self):
        """This method tests id functionality of Base"""
        base = Base()
        self.assertEqual(base.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(3)
        self.assertEqual(base3.id, 3)
