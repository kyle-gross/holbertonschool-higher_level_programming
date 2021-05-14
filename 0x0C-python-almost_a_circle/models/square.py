#!/usr/bin/python3
"""This module contains the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class creates Square objects"""
    def __init__(self, size, x=0, y=0, id=None):
        """This method constructs Square objects"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a Square object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
