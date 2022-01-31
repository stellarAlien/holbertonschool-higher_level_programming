#!/usr/bin/python3
"""
square class: 10-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class child class of Rectangle"""
    def __init__(self, size):
        """init  square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

