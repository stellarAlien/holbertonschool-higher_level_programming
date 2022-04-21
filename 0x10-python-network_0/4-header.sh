#!/bin/bash
# send a get request with  X-School-User-Id: 98 pair
curl -sL -H " X-School-User-Id: 98" "$1"