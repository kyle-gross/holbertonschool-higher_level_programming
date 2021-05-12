#!/usr/bin/python3
"""This module contains a function that writes an object
   to a text file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file using
       JSON representation
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as afile:
        jsonString = json.dumps(my_obj)
        afile.write(jsonString)
