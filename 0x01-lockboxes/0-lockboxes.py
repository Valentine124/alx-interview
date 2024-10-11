#!/usr/bin/python3
"""
Contains Solution to the Lockboxes
algorithm question
"""


def canUnlockAll(boxes):
    """ Returns True if the boxes can be unlocked """

    keys = {0}

    if not (type(boxes) is list):
        return False

    for box in boxes:
        if not (type(box) is list):
            return False
        for key in box:
            idx = boxes.index(box)

            if not (key == idx):
                keys.add(key)

        for num in range(0, len(boxes)):
            if not (num in keys):
                return False
return True
