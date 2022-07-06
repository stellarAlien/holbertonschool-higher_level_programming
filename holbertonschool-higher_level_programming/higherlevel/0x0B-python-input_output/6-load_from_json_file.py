#!/usr/bin/python3
"""module 6-load_from_json_file.py"""
import json


def load_from_json_file(filename):
    """returns an Object from a JSON"""
    with open(filename, encoding="UTF8") as f:
        return json.load(f)
