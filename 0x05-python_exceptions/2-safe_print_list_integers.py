#!/usr/bin/python3
"""
safe_print_list_integers - prints 'x' elements of integers
only prints integers, other data types handed by except
"""


def safe_print_list_integers(my_list=[], x=0):
    """ if x > list length, only the length of the shorter list is printed"""
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except (TypeError, IndexError):
        return None
