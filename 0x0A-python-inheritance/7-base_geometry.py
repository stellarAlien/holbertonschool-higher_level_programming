#!/usr/bin/python3
"""
module:6-base_geometry.py
makes a class Basegeometry
"""


class BaseGeometry:
    """
    still empty
    """
    pass

    @staticmethod
    def area():
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if(not isinstance(value, int)):
            raise TypeError("<name> must be an integer")
        elif(value <= 0):
            raise ValueError("<name> must be greater than 0")
