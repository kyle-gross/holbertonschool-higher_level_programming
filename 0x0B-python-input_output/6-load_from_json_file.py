#!/usr/bin/python3
"""This module contains a function that creates an object
   from a JSON file
"""


def load_from_json_file(filename):
    """This function creates an object from a JSON file"""
    import json
    with open(filename, encoding="utf-8") as afile:
        objJson = json.dumps(afile)
        obj = json.loads(objJson)
