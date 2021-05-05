#!/usr/bin/python3
"""
This module contains the funciton say_my_name which prints
the name given as arguments
"""


def say_my_name(first_name, last_name=""):
    """
    * <first_name> and <last_name> must be strings otherwise
      raise a TypeError with the message "<name> must be a string"
    """
    # String checks
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
