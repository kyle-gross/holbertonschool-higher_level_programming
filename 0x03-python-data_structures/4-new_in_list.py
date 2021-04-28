#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Replaces an element in a list at a specific
    # position without modifying the original list
    if my_list:
        new_list = my_list.copy()
    # If idx < 0, return COPY of original list
    if idx < 0:
        return new_list
    # If idx out of range, return COPY of original list
    if idx > (len(new_list) - 1):
        return new_list
    new_list[idx] = element
    return new_list
