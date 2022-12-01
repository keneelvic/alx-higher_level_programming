#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    lastd = ((number * -1) % 10) * -1
else:
    lastd = number % 10
if lastd > 5:
    print("Last digit of {0:d} is {1:d} and is greater than 5".format(number, lastd))
elif lastd == 0:
    print("Last digit of {0:d} is {1:d} and is 0".format(number, lastd))
elif lastd < 6 and not 0:
    print("Last digit of {0:d} is {1:d} andis less than 6 and not 0".format(number, lastd))
