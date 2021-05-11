#!/usr/bin/python3
"""This module contains the lookup function"""


def lookup(obj):
    """
    This function returns the list of available attributes and
    methods of an object
    """
    att_list = []

    for i in dir(obj):
        att_list.append(i)

    return att_list
