#!/usr/bin/python3
"""This function is a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor for the matrix.
    Raises:
        TypeError: If the matrix has non int or float values included.
        TypeError: If the matrix has different lengths for its rows.
        TypeError: If div has a non int or float value.
        ZeroDivisionError: If div equals to 0.
    Returns:
        A new matrix with the results of the divisions.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)
            or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
