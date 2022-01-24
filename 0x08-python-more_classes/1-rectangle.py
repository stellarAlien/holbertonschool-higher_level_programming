#!/usr/bin/python3
"""
Module 1-rectangle
sets height adn width for triangle
"""


class Rectangle:
    """
    rectangle properties are defined
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """  return private attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width and checks for errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """  get private attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height and checks for value and type errors """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
