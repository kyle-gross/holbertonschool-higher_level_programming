#!/usr/bin/python3
"""This module contains unittests for Base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """This class tests the Base class"""
    def test_auto_id(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base2 = Base(None)
        self.assertEqual(base2.id, 2)
        
    def test_passed_id(self):
        base3 = Base(89)
        self.assertEqual(base3.id, 89)

    def test_to_json_string(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_from_json_string(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])
        json_list = Base.from_json_string("[]")
        self.assertEqual(json_list, [])
