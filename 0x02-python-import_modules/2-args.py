#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    c = len(sys.argv)
    if(c == 1):
        print("{} arguments.".format(0))
    elif(c == 2):
        print("{} argument:".format(1))
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(c - 1))
        for i in range (1, c):
            print("{}: {}".format(i, sys.argv[i]))
