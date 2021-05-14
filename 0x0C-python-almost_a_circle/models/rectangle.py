#!/usr/bin/python3
"""This module contains the class Rectangle"""


from models.base import Base


class Rectangle(Base):

    """This class creates Rectangle objects"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle objects"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """Width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0") 
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """Height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0") 
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """x setter"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0") 
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif x < 0:
            raise ValueError("y must be >= 0") 
        else:
            self.__y = y
