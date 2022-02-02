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
        if(not (type(value) is int)):
            raise TypeError("{:} must be an integer".format(name))
        elif(not value or value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))
