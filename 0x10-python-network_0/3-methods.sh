#!/bin/bash
# GET  all avaliable methods of server
cut f2- -d ' ' | curl -X OPTIONS "$1"  
