#!/usr/bin/python3
"""lockboxes Problem"""


def canUnlockAll(boxes):
    """unlock boxes func"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while len(keys) > 0:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n:
                if not unlocked[key]:
                    unlocked[key] = True
                    keys.append(key)

    for box in unlocked:
        if not box:
            return False
    return True
