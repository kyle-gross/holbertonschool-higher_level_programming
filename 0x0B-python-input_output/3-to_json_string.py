#!/usr/bin/python3
"""This module contains a function that returns the JSON
   representation of an object
"""


def to_json_string(my_obj):
    """This function returns a JSON representation of an object"""
    import json
    return json.dumps(my_obj)
