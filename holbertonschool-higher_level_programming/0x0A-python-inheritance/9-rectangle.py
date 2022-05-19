#!/usr/bin/python3
"""
module:8-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """print dimensions of instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
