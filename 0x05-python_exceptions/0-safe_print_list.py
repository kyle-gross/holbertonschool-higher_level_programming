#!/usr/bin/python3
"""
safe_print_list - prints a list of integers even if there
is an index error
"""


def safe_print_list(my_list=[], x=0):
    """ returns a count of the printed items
    """
    if my_list is None:
        return 0
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return 0
