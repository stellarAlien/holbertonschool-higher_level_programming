#!/usr/bin/python3
"""
module 4-inherits_from.py
 instance of a class is inherited (directly or indirectly)
 from the specified class ;
 """


def inherits_from(obj, a_class):
    """
    determines inheritance
    """
    if(issubclass(type(obj), a_class) and not(type(obj) is a_class)):
        return True
    else:
        return False
