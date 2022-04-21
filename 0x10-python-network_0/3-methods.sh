#!/bin/bash
# GET  all avaliable methods of server
curl -X OPTIONS "$1" | awk 'for (i=2, i<=NF, i++) print("$i")' 
