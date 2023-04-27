#!/usr/bin/python3
"""
    This defines a function that determines if a number of lists of lists can be
    opened by keys whose value is the number of the box
"""


def canUnlockAll(boxes):
    """This determines if the boxes (lists of lists) can be unlocked"""
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False