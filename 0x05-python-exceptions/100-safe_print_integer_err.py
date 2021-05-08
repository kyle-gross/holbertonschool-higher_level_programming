#!/usr/bin/python3
"""This method contains a function that prints an integer
"""


def safe_print_integer_err(value):
    """This function safely prints integers"""
    import sys
    try:
        print("{:d}".format(value))
        return True

    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
