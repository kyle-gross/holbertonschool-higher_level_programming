#!/usr/bin/python3
"""This module contains the Student class"""


class Student:
    """This class defines students by these public attributes:
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        """Constructs a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation"""
        if isinstance(attrs, list):
            my_dict = {}
            for att in attrs:
                if hasattr(self, att):
                    my_dict[att] = getattr(self, att)
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """This method replaces all attributes of a Student instance"""
        for item in json.items():
            if hasattr(self, item[0]):
                setattr(self, item[0], item[1])
