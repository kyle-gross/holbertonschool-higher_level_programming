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

    def to_json(self):
        return self.__dict__
