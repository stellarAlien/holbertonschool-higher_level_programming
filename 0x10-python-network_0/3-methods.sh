#!/bin/bash
# GET  all avaliable methods of server
curl -sI OPTIONS "$1" | grep Allow |  cut -f2- -d ' '  
