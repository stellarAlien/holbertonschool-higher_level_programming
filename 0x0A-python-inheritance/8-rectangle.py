#!/usr/bin/python3
"""
module:8-rectangle.py
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
            raise TypeError("<name> must be an integer")
            return
        if(value <= 0):
            raise ValueError("<name> must be greater than 0")
            return
        return(value)


class Rectangle(BaseGeometry):
    """
    rectangle class
    """

    def __init__(self, width, height):
        """
        init rectangle
        """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
