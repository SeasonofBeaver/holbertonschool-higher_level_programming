#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    sum = 0
    for i in my_list:
        nonunique = False
        for j in unique:
            if i == j:
                nonunique = True
                break
        if nonunique:
            continue
        sum += i
        unique.append(i)
    return sum
