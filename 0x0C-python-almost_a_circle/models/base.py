#!/usr/bin/python3
"""This module contains the Base class"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
