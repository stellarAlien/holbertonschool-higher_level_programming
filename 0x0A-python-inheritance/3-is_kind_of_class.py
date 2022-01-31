#!/usr/bin/python3
"""
module 3-is_kind_of_class.py
determines if instance is from class
or from a subclass
"""


def is_kind_of_class(obj, a_class):
    """
    object inherits from a_class ?
    """
    if(issubclass(type(obj), a_class)):
        return True
    else:
        return False
