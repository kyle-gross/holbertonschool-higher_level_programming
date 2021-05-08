#!/bin/bash/python3
"""This module contains a function
    ...
    that executes a function!
"""


def safe_function(fct, *args):
    """This function executes a function!"""
    import sys
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
