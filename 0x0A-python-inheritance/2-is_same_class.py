#!/usr/bin/python3
"""
file: 2-is_same_class.py
desc: Defines is_same_class function
Date: 10 July 2023
"""

def is_same_class(obj, a_class):
    """
    Returns true if object is exactly an instance of
    specified class, otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
