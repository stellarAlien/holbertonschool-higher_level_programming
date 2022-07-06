#!/usr/bin/python3
"""
module def lookup(obj):
returns list of all attributes and method in a class
"""


def lookup(obj):
    """ return elements of an objects"""
    ls = dir(obj)
    return(list(ls))
