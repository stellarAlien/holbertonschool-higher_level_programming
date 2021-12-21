#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    cpnumber = number * -1
    n = -(cpnumber % 10)
else:
    n = number % 10
if(n > 5):
    print("the last digit of", number, "is", n, "and is greater than 5")
elif(n < 6 and n != 0):
    print("the last digit of", number, "is",  n, "and is less than 6 and not")
else:
    print("the last digit of", number, "is",  n, "and is 0")
