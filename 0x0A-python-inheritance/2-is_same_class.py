#!/usr/bin/python3
"""Defines is_same_class function"""

def is_same_class(obj, a_class):
    """
    Returns true if object is exactly an instance of
    specified class, otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
