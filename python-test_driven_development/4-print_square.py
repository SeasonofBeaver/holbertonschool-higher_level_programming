#!/usr/bin/python3
    """Prints a square of #"""


def print_square(size):
    """Prints a square of # of the size 'size'.

    Args:
        size (int): size of the square to be printed.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is smaller than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for char in range(size):
            print("#", end="")
        print()
