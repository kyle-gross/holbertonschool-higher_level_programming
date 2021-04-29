#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Function that replaces all occurrences of an element by
    # another in a new list
    new_list = my_list.copy()
    new_list = [replace if i == search else i for i in new_list]
    return new_list
