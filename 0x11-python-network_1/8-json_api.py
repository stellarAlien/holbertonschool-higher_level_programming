#!/usr/bin/env python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests
if "__name__" == "__main__":
    if(argv[1]):
        q = {'q': argv[1]}
    else:
        q = ""
        with requests.session() as req:
            req.get("http://0.0.0.0:5000/search_user", data=q)
    try:
        r = req.json()
    except ValueError:
        print("Not a valid JSON")
    if(r == ""):
        print("No result")
    try:
        print("[{}] {}".format(r["id"], r["name"]))
    except IndexError:
        print("No result")
