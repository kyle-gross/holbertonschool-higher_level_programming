#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """This function returns True if the object is exactly an instance
       of the specified class; otherwise False
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
