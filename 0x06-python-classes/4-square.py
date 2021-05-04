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
        self.__size = 0

    @property
    def size(self):
        """This function returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the size of a Square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This function returns the area of a square object"""
        area = self.__size ** 2
        return area
