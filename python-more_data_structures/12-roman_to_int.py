#!/usr/bin/python3
def roman_to_int(roman_string):
    previousNum = ''
    converted = 0
    for number in roman_string:
        if number == "M":
            if previousNum == "C":
                converted += 800
            else:
                converted += 1000
        elif number == "D":
            if previousNum == "C":
                converted += 300
            else:
                converted += 500
        elif number == "C":
            if previousNum == "X":
                converted += 80
            else:
                converted += 100
        elif number == "L":
            if previousNum == "X":
                converted += 30
            else:
                converted += 50
        elif number == "X":
            if previousNum == "I":
                converted += 8
            else:
                converted += 10
        elif number == "V":
            if previousNum == "I":
                converted += 3
            else:
                converted += 5
        else:
            converted += 1
        previousNum = number
    return converted