#!/usr/bin/python3
"""This module creates a new class called Square.
The size of the square is initialized"""


class Square:
    """Square class initializes the size as a private instance attribute"""
    def __init__(self, size=0):
        """init function which initializes a Square object
        and gives it a size.
        Raises a TypeError if given size is not an integer.
        Raises a ValueError if size is less than 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
