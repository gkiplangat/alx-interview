#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """
    take boxes
        create set of keys
            go to box0
                get all keys and add them setofkeys
            start opening boxes from setofkeys
                go to each box of each key
                    and take the keys from it and add them to set of keys
                keep loping through all setof keys
            ignore keys that dont have box
            track opening of boxes by a counter, if at end it
            equal to lentgh of boxes it mean all boxes unlock
            OPTIMIZE IDEA :
                if we add 0 to setofkeys at start, we dont need for in 23
    """
    ttl_boxes = len(boxes)
    keys = [0]
    counter = 0
    index = 0

    while index < len(keys):
        setkey = keys[index]
        for key in boxes[setkey]:
            if 0 < key < ttl_boxes and key not in keys:
                keys.append(key)
                counter += 1
        index += 1

    return counter == ttl_boxes - 1
