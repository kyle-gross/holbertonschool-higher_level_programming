#!/usr/bin/python3
def uppercase(str):
    for i in (str):
        if ord(i) >= 97 and ord(i) <= 122:
            x = ord(i) - 32
            y = chr(x)
            print("{}".format(y), end="")
        else:
            print("{}".format(i), end="")
