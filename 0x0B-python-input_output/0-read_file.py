#!/usr/bin/python3
"""This module contains a function that reads a file"""


def read_file(filename=""):
    """This function reads a file and prints it to stdout"""
    with open(filename, encoding="utf-8") as afile:
        print(afile.readline(), end="")
