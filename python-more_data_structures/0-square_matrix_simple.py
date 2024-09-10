#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for rows in matrix:
        addedRow = []
        for integers in rows:
            addedRow.append(integers ** 2)
        copy.append(addedRow)
    return copy
