#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, att, value):
    """Add a new attribute to an object if possble.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj
        value (any) : the value of att.

    Raises:
        TypeError: if the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("cant add new attribute")
    setattr(obj att, value)
