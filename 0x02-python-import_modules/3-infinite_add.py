#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = 0
    lenght = len(sys.argv)

    for i in range(1, lenght):
        number += int(sys.argv[i])
    print(number)
