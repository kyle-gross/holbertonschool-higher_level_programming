#!/usr/bin/python3
"""This module contains the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class creates Square objects"""
    def __init__(self, size, x=0, y=0, id=None):
        """This method constructs Square objects"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of a Square object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value
