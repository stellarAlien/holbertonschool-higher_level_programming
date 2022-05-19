#!/usr/bin/env python3
"""
post request to url with email as data
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    r = requests.post(url, data=email)
    print(r.text)