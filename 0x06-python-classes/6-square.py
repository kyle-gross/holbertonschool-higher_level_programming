#!/usr/bin/python3
"""This module creates a new class called Square.
The size of the square is initialized"""


class Square:
    """Square class initializes the size as a private instance attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """init function which constructs a Square object
        and gives it a size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """This function returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets the size of a Square object
        Raises a TypeError if given size is not an integer.
        Raises a ValueError if size is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This function returns the position within a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """This function sets the position of a square
        Raises a TypeError if not a tuple
        containing 2 integers or a value is < 0"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif min(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This function returns the area of a square object"""
        area = self.__size ** 2
        return area

    def my_print(self):
        """This function prints a Square object"""
        if self.__size is 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
