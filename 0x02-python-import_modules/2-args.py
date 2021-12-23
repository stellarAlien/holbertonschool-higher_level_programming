#!/usr/bin/python3
if __name__ =="__main__":
    import os
    i = 1
    if(sys.argc == 1):
        print("{}arguments.".format(0))
    elif(sys.argc ==2):
        print("{}argument:".format(1))
        print("{}: {}".format(i, sys.argv[i])
    else:
        print("{} arguments:".format(sys.argc))
        while(sys.argv[i]):
            print("{}: {}".format(i, sys.argv[i]))
