#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Replaces an element of a list at specific position
    # If idx > 0, do nothing, return original list
    if idx < 0:
        return my_list
    # If idx out of range, do nothing, return original list
    if idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list
