#!/usr/bin/python3
"""
This module contains the print_square function which prints
a square with the character '#'
"""


def print_square(size):
    """
    This function prints a square with the character '#'
    -------------
    * <size> is the length of the square
    * <size> must be an integer otherwise raise a TypeError
      with the msessage "size must be an integer"
    * if <size> is < 0 raise a ValueError wit hthe message
      "size must be >= 0"
    * if <size> is a float and is < 0 raise a TypeError
      with the message "size must be an integer
    """
    # Integer check
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Less than 0 check
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
