#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mylastdigt = abs(number) % 10
if number < 0:
    mylastdigt = -(mylastdigt)
mystring = "Last digit of {} is {}".format(number, mylastdigt)
if mylastdigt > 5:
    print(f"{mystring} and is greater than 5")
elif mylastdigt == 0:
    print(f"{mystring} and is 0")
elif mylastdigt < 6:
    print(f"{mystring} and is less than 6 and not 0")
