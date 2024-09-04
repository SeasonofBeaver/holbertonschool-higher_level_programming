#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("%s" % ("FizzBuzz"), end=" ")
        elif i % 5 == 0:
            print("%s" % ("Buzz"), end=" ")
        elif i % 3 == 0:
            print("%s" % ("Fizz"), end=" ")
        else:
            print("%d" % (i), end=" ")
