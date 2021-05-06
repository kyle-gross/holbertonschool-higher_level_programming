#!/usr/bin/python3
"""
This module contains the Rectangle class
Rectangles have the attributes:
    height: the height of rectangle
    width: the width of rectangle
"""


class Rectangle:
    """
    This class creates a Rectangle object
    """
    def __init__(self, width=0, height=0):
        """Constructor for Rectangle objects"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
