#!/usr/bin/python3
"""This module contains the Base class"""


class Base:
    """This class is the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the base level constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
