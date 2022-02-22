#!/usr/bin/python3
"""
definiton of Base Class
"""
import json


class Base():
    """Base class which all subsquqent classes will depend on"""

    __nb_objects = 1

    def __init__(self, id=None):
        """init  class"""
        if(not(id is None)):
            self.id = id
        elif(id is None):
            self.id = Base.__nb_objects
            Base.__nb_objects = Base.__nb_objects + 1
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json rep of list of dicts"""
        if((list_dictionaries is None) or list_dictionaries == [] or list_dictionaries == "[]"):
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """write repr of obj to a file"""
        if((list_objs is None) or len(list_objs) == 0):
            list_objs = []
        if cls.__name__ == "Rectangle":
            with open("Rectangle.json", "w") as f:
                json.loads(list_objs, f)
        elif cls.__name__ == "Square":
            with open("Rectangle.json", "w") as f:
                json.loads(list_objs, f)
    def from_json_string(json_string):
        """ return json rep of json as list"""
        if((json_string is None) or (json_string == "") or (json_string == "{}")):
            li = list()
        else:
            li = json.loads(json_string)
            return list
