#!/usr/bin/python3
"""
module 8-class_to_json.py
return dictionary of an object
"""


def class_to_json(obj):
    """return dictionary"""
    return obj.__dict__
