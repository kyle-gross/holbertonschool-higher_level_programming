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

    @staticmethod
    def from_json_string(json_string):
        """Returns the JSON string representation of <json_string>"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation of <list_objs>
           to a file
        """
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs:
            for obj in list_objs:
                my_dict = cls.to_dictionary(obj)
                my_list.append(my_dict)
            json_str = cls.to_json_string(my_list)
        else:
            json_str = "[]"
        with open(filename, "w") as file:
            file.write(json_str)
