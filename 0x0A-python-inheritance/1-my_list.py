#!/usr/bin/python3
"""
Mylist class
This file contains one class
a parent class and sub class
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

