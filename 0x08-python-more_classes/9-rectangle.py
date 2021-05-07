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
    Attributes:
        number_of_instances: keeps track of number of Rectangles
        print_symbol: the symbol to print when building Rectangle
            strings
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle objects"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints a rectangle object"""
        if self.height == 0 or self.width == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            rectangle += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rectangle += "\n"
        return rectangle

    def __del__(self):
        """Prints 'Bye rectangle...' when a rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """Returns a string representation of a Rectangle object"""
        return 'Rectangle(%d, %d)' % (self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method which returns bigggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method which returns a new Rectangle instance with w == h"""
        return cls(width=size, height=size)

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
