#!/usr/bin/python3
"""This module prints 'x' elements of a list"""


def safe_print_list(my_list=[], x=0):
    """This function prints integers from a list

    Args:
        my_list (list): first parameter
        x (int): second parameter

    Return: count - # of items printed
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
