#!/usr/bin/python3
"""This module contains the class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """This constructs Rectangle objects"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """This is a magic method which returns a rectangle string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """This method returns the area of a Rectangle object"""
        return self.__width * self.__height
