#!/usr/bin/python3
"""
File: 2-is_same_clas.py
Desc: This module contains one function; is_same_class
Author: Waithaka (waithakan)
Date Created: 10 July 2023
"""


def is_same_class(obj, a_class):
    """
    Returns true if object is exactly an instance of
    specified class, otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
