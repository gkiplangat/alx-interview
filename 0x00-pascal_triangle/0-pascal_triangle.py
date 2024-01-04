#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integets representing the pascal triangle"""
    base = [[1], [1, 1]]

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return base

    start = 2
    while start < n:
        array_toAdd = [1]
        for i in range(1, start):
            array_toAdd.append(base[start - 1][i - 1] + base[start - 1][i])
        base.append(array_toAdd + [1])
        start += 1
    return base
