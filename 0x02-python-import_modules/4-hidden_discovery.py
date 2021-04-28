#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirlen = len(dir(hidden_4))
    for i in range(dirlen):
        names = dir(hidden_4)[i]
        if names.startswith("__") == True:
            continue
        print("{}".format(names))
