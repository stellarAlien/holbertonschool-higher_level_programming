#!/usr/bin/python3
"""
Module 101-locked_class
don't let users add attributes
"""
class LockedClass:
    """
    lockedclass that only has first_name attribute
    """
    __slots__ =["first name"]
