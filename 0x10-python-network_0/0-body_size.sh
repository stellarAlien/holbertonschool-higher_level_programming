#!/usr/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl "$1" | awk '/^Content-length/ {print $2}'