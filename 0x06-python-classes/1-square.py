#!/usr/bin/python3
"""This module creates a new class called Square.
The size of the square is initialized"""


class Square:
    """Square class initializes the size as a private instance attribute"""
    def __init__(self, size):
        """init function which initializes a Square object
        and gives it a size"""
        self.__size = size
