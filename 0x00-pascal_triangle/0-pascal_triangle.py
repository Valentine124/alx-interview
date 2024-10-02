#!/usr/bin/python3
"""
Contains a function that implements
the Pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of list that represents
    the Pascal's triangle

    Args:
        n (int) - The length og the triangle
    """
    pascal_list = []

    if n <= 0:
        return pascal_list

    for idx in range(n):
        new_list = []

        for index in range(idx + 1):
            if index == 0:
                new_list.append(1)
            elif index == idx:
                new_list.append(1)
            else:
                prev_list = pascal_list[idx - 1]
                next = prev_list[index] + prev_list[index - 1]
                new_list.append(next)

        pascal_list.append(new_list)

    return pascal_list
