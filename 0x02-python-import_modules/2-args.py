#!/usr/bin/python3
if __name__ == "__main__":
    import os
    i = 1
    c = len(sys.argv) - 1
    if(c == 1):
        print("{}arguments.".format(0))
    elif(c == 2):
        print("{} argument:".format(1))
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(c))
        while i in range l:
            print("{}: {}".format(i, sys.argv[i]))
