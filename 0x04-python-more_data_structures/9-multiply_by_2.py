#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_copy = a_dictionary.copy()
    dict_copy.update((x, y * 2) for x, y in dict_copy.items())
    return dict_copy
