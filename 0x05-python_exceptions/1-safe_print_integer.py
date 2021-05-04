#!/usr/bin/python3
"""
safe_print_integer - prints a list of integers even if
there are conflicting data types
"""


def safe_print_integer(value):
    """ Returns True if value is printed correctly or False if not"""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
