#!/usr/bin/python3
"""
define Rectangle class
Inherits directly from Base
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """represent rectangle on stdout"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for p in range(self.__x):
                print("",end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """updates values of rectangle as provided"""
        if(args):
            for i, j in enumerate(*args):
                if k == 0:
                    self.id = j
                if k == 1:
                    self.__width = j
                if k == 2:
                    self.__height = j
                if k == 3:
                    self.__x = j
                if k == 4:
                    self.__y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d

    def area(self):
        """returns rectangle's area"""
        return self.__width * self.__height

    @property
    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    @property
    def width(self):
        """returns width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of recrangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns cooridnate x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets coordinate x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns coordinate y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y coordinate"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """returns rectangle instance properties"""
        return"[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(\
                self.id, self.__x, self.__y, self.__width, self.__height)
