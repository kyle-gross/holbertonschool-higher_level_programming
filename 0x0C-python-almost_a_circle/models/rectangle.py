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

    def __str__(self):
        """Returns str representation of Rectangle object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args):
        """This method updates a Rectangle object"""
        largs = list(args)
        if len(largs) == 5:
            self.y = largs[4]
            largs.pop()
        if len(largs) == 4:
            self.x = largs[3]
            largs.pop()
        if len(largs) == 3:
            self.height = largs[2]
            largs.pop()
        if len(largs) == 2:
            self.width = largs[1]
            largs.pop()
        if len(largs) == 1:
            self.id = largs[0]

    def area(self):
        """Returns the area of a Rectangle object"""
        return self.width * self.height

    def display(self):
        """This method prints a Rectangle instance to stdout"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

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
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
