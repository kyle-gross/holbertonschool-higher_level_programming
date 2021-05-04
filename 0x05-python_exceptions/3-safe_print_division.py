#!/usr/bin/python3
def safe_print_division(a, b):
    print("Inside result:", end="")
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("{}".format(quotient))
        return quotient
