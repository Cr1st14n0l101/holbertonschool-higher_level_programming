#!/usr/bin/python3

"""Sort a List"""


class MyList(list):
    """Prints and sort a list"""

    def print_sorted(self):
        """
        rints and sort a list
        Return: (void)
        """
        print(sorted(self))
