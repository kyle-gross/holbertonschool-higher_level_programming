#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Adds 2 tuples
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    # If a tuple is bigger than 2, use only the first 2 integers
    num1 = tuple_a[0] + tuple_b[0]
    num2 = tuple_a[1] + tuple_b[1]
    # Returns a tuple with 2 integers
    return (num1, num2)
