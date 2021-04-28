#!/usr/bin/python3
def no_c(my_string):
    # Removes all characters c and C from a string
    if my_string:
        # Return the new string
        return my_string.translate({ord(i): None for i in 'Cc'})
