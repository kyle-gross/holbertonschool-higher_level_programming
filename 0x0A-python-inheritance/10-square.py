#!/usr/bin/python3
"""This module contains the Square class"""


Square = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class inherits from the Rectangle class"""
    def __init__(self, size):
        """This function constructs a square object"""
        self.integer_validator(size)
        self.__size = size

    def area(self):
        """This function calculates the area of a square"""
        return self.__size ** 2
