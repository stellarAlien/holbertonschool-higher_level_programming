#!/usr/bin/python3
"""
definiton of Base Class
"""


class Base():
    """Base class which all subsquqent classes will depend on"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init  class"""
        if(not(id is None)):
            self.id = id
        elif(id is None):
            self.id = Base.__nb_objects
            Base.__nb_objects = Base.__nb_objects + 1
