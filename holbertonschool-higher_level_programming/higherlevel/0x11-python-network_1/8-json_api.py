#!/usr/bin/env python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if "__name__" == "__main__":
    data = {"q": argv[1] if len(argv) > 1 else ""}
    request = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        request = request.json()
    except ValueError:
        print("Not a valid JSON")
    if(request == ""):
        print("No result")
    try:
        print("[{}] {}".format(request["id"], request["name"]))
    except IndexError:
        print("No result")
