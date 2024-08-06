#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """function find min num of operation to reach a num of chars"""
    chars = 2
    prev_chars = 1
    count = 2
    paste = 1
    copy_paste = 2
    for i in range(n-1):
        res = n / chars
        if res != int(res) and chars != n:
            count += paste
            chars += prev_chars
            continue
        elif res == int(res) and chars != n:
            count += copy_paste
            prev_chars = chars
            chars += prev_chars
            continue
        elif chars == n:
            break
        else:
            return (0)
    return (count)
