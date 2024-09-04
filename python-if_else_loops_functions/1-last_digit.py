#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10

msg = "Last digit of %d is %d and is" % (number, digit)

if digit == 0:
    print(msg, "0")
elif digit < 6:
    print(msg, "less than 6 and not 0")
else:
    print(msg, "greater than 5")
