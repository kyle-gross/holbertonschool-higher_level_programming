#!/usr/bin/python3
"""This module contains the Square class"""


from models.rectangle import Rectangle
import inspect


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

    def update(self, *args, **kwargs):
        """This method updates a Rectangle object"""
        if args is None or len(args) == 0:
            for i in kwargs:
                if hasattr(self, i):
                    setattr(self, i, kwargs[i])
        else:
            largs = list(args)
            latts = ["id", "size", "x", "y"]
            for i in range(len(largs)):
                setattr(self, latts[i], largs[i])

    def to_dictionary(self):
        """Returns dict representation of a Rectangle object"""
        my_dict = {}
        for i in inspect.getmembers(self):
            if not i[0].startswith("_"):
                if not inspect.ismethod(i[1]):
                    if i[1] == "height" or i[1] == "width":
                        continue
                    my_dict[i[0]] = i[1]
        return my_dict

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
