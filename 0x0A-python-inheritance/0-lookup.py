#!/usr/bin/python3
"""
Defines lookup function

"""


def lookup(obj):
    """
    Returns the list of object attribute
    Args:
        - obj: object to look into

    """
    return(dir(obj))
