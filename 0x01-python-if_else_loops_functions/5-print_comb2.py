#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        print("{0:d}{1:d}".format(i, j), end ='')
        if(i == 9 and j == 9):
            break;
        print(', ', end= '')

