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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                rect = rect + str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """ String representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
