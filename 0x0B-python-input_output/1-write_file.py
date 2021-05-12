#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """This function writes <text> to <filename>"""
    with open(filename, mode="w", encoding="utf-8") as afile:
        afile.write(text)
        num_chars = len(text)

    return num_chars
