#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Function to print all integers of a list
    for i in my_list:
        # One integer per line, str.format()
        print("{:d}".format(my_list.index(i)))
