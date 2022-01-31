#!/usr/bin/python3
"""
module:8-rectangle.py
makes a class Basegeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class
    """

    def __init__(self, width, height):
        """
        init rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
