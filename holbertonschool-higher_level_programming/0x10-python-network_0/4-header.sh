#!/bin/bash
# send a get request with  X-School-User-Id: 98 pair
curl -s "$1" -X GET -H "X-School-User-Id: 98"
