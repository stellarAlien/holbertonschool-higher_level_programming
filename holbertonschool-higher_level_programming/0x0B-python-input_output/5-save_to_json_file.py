#!/usr/bin/python3
"""module 5-save_to_json_file.py"""

import json


def save_to_json_file(my_obj, filename):
    """return str"""
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
