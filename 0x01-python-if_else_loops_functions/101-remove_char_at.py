#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if i == (n - 1):
            continue
        print("{}".format(i), end="")
    print()
