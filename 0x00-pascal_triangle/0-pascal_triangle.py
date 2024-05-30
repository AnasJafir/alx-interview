#!/usr/bin/python3
"""Pascla's Triangle Module"""


def pascal_triangle(n):
    """
    Method that returns a list of lists of integers representing
    the Pascal's triangle of n rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's triangle.

    Notes:
        - Returns an empty list if n <= 0.
        - You can assume n will always be an integer.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle
