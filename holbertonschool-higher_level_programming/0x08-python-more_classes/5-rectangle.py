#!/usr/bin/python3
"""
Module 2
adds perimiter and area computation methods
"""


class Rectangle:
    """
    rectangle properties are defined
    area and perimeter fnuctions are defined
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
        """get private attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height and checks for value and type errors """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def perimeter(self):
        """ returns perimiter of rect"""
        if(self.__width == 0 or self.__height == 0):
            return 0

    def area(self):
        """ returns area of traingle"""
        return (self.__width * self.__height)

    def __str__(self):
        """prints the rectangle described in #"""
        if(self.__width == 0 or self.__height == 0):
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """ String representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")
