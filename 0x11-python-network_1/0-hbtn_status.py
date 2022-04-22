#!/usr/bin/python3
"""
fetch status from a link
"""
import urllib.request
if __name__ == "__main__":
	import urllib.response
	with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
		r = response.read()
		print("Body response:")
		print("	- type: {:}".format(type(r)))
		print("	- content: {:}".format(r))
		print("	- utf8 content: OK" if r.decode('utf8') else "")
