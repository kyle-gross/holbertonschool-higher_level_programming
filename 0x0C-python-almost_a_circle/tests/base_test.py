#!/usr/bin/python3
"""This module contains unittests for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.Testcase):
    """This class tests the Base class"""
    def id_tests(self):
        """This method tests id functionality of Base"""
        base = Base()
        base2 = Base()
        base3 = Base(3)
        self.assertEqual(base.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
