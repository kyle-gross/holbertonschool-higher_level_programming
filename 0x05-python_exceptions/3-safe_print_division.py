#!/usr/bin/python3
"""
safe_print_division - prints the result of division of a and b
"""


def safe_print_division(a, b):
    """ prints and returns within finally"""
    print("Inside result:", end="")
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("{}".format(quotient))
        return quotient
