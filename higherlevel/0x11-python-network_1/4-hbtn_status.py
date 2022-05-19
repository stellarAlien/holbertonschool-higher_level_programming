#!/usr/bin/env python3
"""
fetch https://intranet.hbtn.io/status
"""
import requests
if "__name__" == "__main__":
    with requests.get("https://intranet.hbtn.io/status") as r:
        print("Body response:")
        print("\t- type: {:}".format(type(r)))
        print("\t- content: {:}".format(r.text))