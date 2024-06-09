#!/usr/bin/python3
"""LockBoxes Module"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): list of lists, where each sublist contains
        the boxes that can be opened with the corresponding box.

    Returns:
        bool: True if all boxes can be opened, else False
    """

    # Set of boxes that have been opened
    opened_boxes = set()
    # Add the first box to the set of opened boxes
    opened_boxes.add(0)
    # List of boxes to check
    to_check = []
    # Add the boxes that can be opened with the
    # first box to the list of boxes to check
    to_check.extend(boxes[0])

    # Loop until there are no more boxes to check
    while to_check:
        # Get the next box to check
        box = to_check.pop(0)
        # If the box has not been opened already
        # add it to the set of opened boxes and add the boxes
        # that can be opened with it to the list of boxes to check
        if box not in opened_boxes:
            opened_boxes.add(box)
            to_check.extend(boxes[box])

    # If the number of boxes is equal to the number of opened boxes
    # all boxes can be opened, else they cannot
    return len(boxes) == len(opened_boxes)
