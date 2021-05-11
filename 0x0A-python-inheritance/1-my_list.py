#!/usr/bin/python3
"""This module contains the class MyList"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """This function prints the sorted list"""
        sorted_list = []
        sorted_list = self.copy()
        sorted_list.sort()
        print("{}".format(sorted_list))
