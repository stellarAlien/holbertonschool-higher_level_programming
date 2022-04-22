#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays
 the body of the response
"""
import urllib
from sys import argv
import urllib.error

if "__name__" == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.status_code)
