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
            tmp = n
            count = 0
            while tmp >= factor:
                tmp -= factor
                count += 1
            n = count
            operations_count += factor
        else:
            factor += 1

    return (operations_count)
