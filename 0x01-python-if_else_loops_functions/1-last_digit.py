#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    cpnumber = -number
    n = -(cpnumber % 10)
else:
    n = number % 10
if(n > 5):
    print("Last digit of", number, "is", n, "and is greater than 5")
elif(n < 6 and n != 0):
    print("Last digit of", number, "is",  n, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is",  n, "and is 0")
