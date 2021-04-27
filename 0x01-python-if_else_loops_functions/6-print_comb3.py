#!/usr/bin/python3
n = 0
for i in range(10):
    ii = 1 + n
    while ii < 10:
        print("{}{}".format(i, ii), end="")
        if i == 8 and ii == 9:
            break
        ii += 1
        print(",", end=" ")
    n += 1
print("")
