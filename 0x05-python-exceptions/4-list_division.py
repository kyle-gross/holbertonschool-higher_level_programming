#!/usr/bin/python3
"""
list_division - divides 2 lists of integers
"""


def list_division(my_list_1, my_list_2, list_length):
    """ if conflicting data type, add '0' to that list index"""
    new_list = []
    for i in range(list_length):
        try:
            number = my_list_1[i] / my_list_2[i]
        except IndexError:
            number = 0
            print("out of range")
        except ZeroDivisionError:
            number = 0
            print("division by 0")
        except TypeError:
            number = 0
            print("wrong type")
        finally:
            new_list.append(number)
    return new_list
