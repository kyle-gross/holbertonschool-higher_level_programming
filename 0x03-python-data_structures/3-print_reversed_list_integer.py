#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Prints all integers of a list, in reverse order
    if my_list:
        my_list.reverse()
        for i in my_list:
            # One integer per line
            # Use str.format() to print integers
            print("{:d}".format(i))
