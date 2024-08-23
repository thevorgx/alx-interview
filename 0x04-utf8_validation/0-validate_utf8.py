#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    continuation_bytes = 0
    for byte in data:
        if not 0 <= byte <= 255:
            return (False)
        if continuation_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif continuation_bytes >> 5 == 0b110:
                count = 1
            elif continuation_bytes >> 4 == 0b1110:
                count = 2
            elif continuation_bytes >> 3 == 0b11110:
                count = 3
            else:
                return (False)
        else:
            if continuation_bytes >> 6 == 0b10:
                count -= 1
            else:
                return (False)
    return (continuation_bytes == 0)
