#!/usr/bin/python3
"""
add_integer returns the sum of 2 integers
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    # Check for None
    if a is None or b is None:
        raise TypeError("a must be an integer")

    # Check for floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Check for strings
    if isinstance(a, str):
        raise TypeError("a must be an integer")
    if isinstance(b, str):
        raise TypeError("b must be an integer")

    return a + b
