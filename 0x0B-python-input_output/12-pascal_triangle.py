#!/usr/bin/python3
"""This module contains a function that returns a list of
   integers representing the Pascal's tringle of <n>
"""


def pascal_triangle(n):
    """This function returns a list of integers representing
       the Pascal's triangle of <n>
    """
    if n <= 0:
        return []

    my_list = []

    for i in range(1, n + 1):
        sub_list = []
        n = 1
        for j in range(1, i + 1):
            sub_list.append(n)
            n = n * (i - j) // j
        my_list.append(sub_list)
    
    return my_list
