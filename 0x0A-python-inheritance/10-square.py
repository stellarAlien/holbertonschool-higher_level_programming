#!/usr/bin/python3
"""
square class: 10-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """init  square"""
        super().__init__(size, size)
        self.__size = size
        self.area()
