#!/usr/bin/python3
"""LockBoxes Module"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    Args:
        boxes (list): A list of lists
        where boxes[i] is a list of keys that can open box i.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Initialize opened_boxes and used_keys
    opened_boxes = set([0])
    used_keys = set()

    # Initialize queue with the first box
    queue = [0]

    # BFS
    while queue:
        # Pop the current_box from the queue
        current_box = queue.pop(0)

        # Add the current_box to used_keys
        used_keys.add(current_box)

        # Iterate over the keys of the current_box
        for key in boxes[current_box]:
            # If the key has not been used
            if key not in used_keys:
                # If the key is a valid box and it has not been opened
                if key < len(boxes) and key not in opened_boxes:
                    # Add the key to opened_boxes
                    opened_boxes.add(key)
                    # Add the key to queue
                    queue.append(key)

    # Return True if all boxes can be opened, False otherwise
    return len(used_keys) == len(boxes)
