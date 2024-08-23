#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """determines if a given data set represents a valid UTF-8 encoding"""
    continuation_bytes = 0
    for num in data:
        if num < 0 or num > 255:
            return (False)
        if continuation_bytes == 0:
            if num >> 7 == 0b0:
                continue
            elif num >> 5 == 0b110:
                continuation_bytes = 1
            elif num >> 4 == 0b1110:
                continuation_bytes = 2
            elif num >> 3 == 0b11110:
                continuation_bytes = 3
            else:
                return (False)
        else:
            if num >> 6 != 0b10:
                return (False)
            continuation_bytes -= 1

    return (True)
