#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArgs = len(sys.argv)
    if numArgs == 1:
        print("0 arguments.")
    elif numArgs == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(numArgs - 1))
        for i in range(1, numArgs):
            print("{}: {}".format(i, sys.argv[i]))
