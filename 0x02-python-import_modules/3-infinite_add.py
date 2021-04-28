#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArgs = len(sys.argv)
    num = 0
    for i in range(1, numArgs):
        num += int(sys.argv[i])
    print("{}".format(num))
