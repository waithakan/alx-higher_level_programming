#!/usr/bin/python3
"""Defining a function that adds attributes to objects."""

def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
