#!/usr/bin/python3
"""
module 2-is_same_class.py
determines if object is an instance 
of a specified class
return true if as stated else flase
"""


def is_same_class(obj, a_class):
    """return true if obj type is a_class"""
    if(type(obj) is a_class):
        return True
    else:
        return False

