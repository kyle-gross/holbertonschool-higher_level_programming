#!/usr/bin/python3
"""This module contains the class BaseGeometry"""


class BaseGeometry:
    """This class defines behavior for BaseGeometry"""
    def __init__(self, width, height):
        """This constructs shapes"""
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height


    def area(self):
        """This function raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates that value is an integer"""
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """This constructs Rectangle objects"""
        BaseGeometry.__init__(self, width, height)
