#!/usr/bin/python3
"""Defines a class for a pascal triangle."""


def pascal_triangle(n):
    """prints a pascal triangle of size n"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prevRow = triangle[-1]
        currRow = [1]
        for j in range(1, len(prevRow)):
            currRow.append(prevRow[j-1] + prevRow[j])
        currRow.append(1)
        triangle.append(currRow)

    return triangle
