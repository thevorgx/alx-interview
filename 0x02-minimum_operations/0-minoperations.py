#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """function find min num of operation to reach a num of chars"""
    operations_count = 0
    factor = 2

    if n <= 1:
        return (0)

    while n > 1:
        if n % factor == 0:
            operations_count += factor
            n = int(n / factor)
        else:
            factor += 1

    return (operations_count)
