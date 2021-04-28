#!/usr/bin/python3
def element_at(my_list, idx):
    # Retrieves an element from a list
    # If idx is negative, return "None"
    if idx < 0:
        return None
    # If idx > # of elements, return "None"
    if idx > (len(my_list) - 1):
        return None
    return my_list[idx]
