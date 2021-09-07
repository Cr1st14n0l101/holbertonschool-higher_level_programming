#!/usr/bin/python3
for i in range(0, 100, 1):
    if i == 99:
        print("{}\n".format(i), end="")
    else:
        print("{}, ".format(str(i).zfill(2)), end="")
