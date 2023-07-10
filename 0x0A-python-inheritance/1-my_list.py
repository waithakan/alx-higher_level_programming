#!/usr/bin/python3
"""
File: 1-my_list.py
Mylist class
This file contains one class: Mylist

"""


class MyList(list):
    """
    Represents a class MyList
    """

    def print_sorted(self):
        """
        Prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))

