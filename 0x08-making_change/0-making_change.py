#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """usind dynamic programing array to find the minimum number of coins"""
    if total <= 0:
        return 0

    dp_arr = [float('inf')] * (total + 1)
    dp_arr[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp_arr[i] = min(dp_arr[i], dp_arr[i - coin] + 1)
    if dp_arr[total] == float('inf'):
        return -1
    else:
        return dp_arr[total]
