#!/usr/bin/python3
"""This module contains the class MyInt"""


class MyInt(int):
    """MyInt is a class that is a rebel. It's an integer
       but it doesn't want to be.
    """
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        """== magic method"""
        if self.num is other:
            return False
        return True

    def __ne__(self, other):
        """!= magic method"""
        if self.num is other:
            return True
        return False
