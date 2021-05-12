#!/usr/bin/python3
"""This module contains a function that appends a string
   to the end of a text file
"""


def append_write(filename="", text=""):
    """This function appends <text> to <filename>"""
    with open(filename, mode='a', encoding='utf-8') as afile:
        afile.write(text)

    return len(text)
