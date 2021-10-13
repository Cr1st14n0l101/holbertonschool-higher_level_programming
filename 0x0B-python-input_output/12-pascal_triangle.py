#!/usr/bin/python3
"""Function that calcuate the pascal triangle"""


def pascal_triangle(n):
    """The pascal triangle"""
    z = 0
    new_list = []

    for x in range(n):
        new_list.append([])

    if n <= 0:
        return new_list
    for x in range(n):

        for y in range(x + 1):
            if y == 0 or y == x:
                new_list[x].append(1)
            else:
                z = new_list[x - 1][y] + new_list[x - 1][y - 1]
                new_list[x].append(z)
    return new_list
