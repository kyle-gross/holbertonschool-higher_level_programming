#!/usr/bin/python3
# Function to print all integers of a list
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(my_list.index(i))) # One integer per line, str.format()
