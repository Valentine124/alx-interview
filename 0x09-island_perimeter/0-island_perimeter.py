#!/usr/bin/python3
"""Contains The solution for the island perimeter problem"""


def island_perimeter(grid):
    """Implementation of the Solution"""

    if grid is None:
        return None

    perimeter = 0
    grid_len = len(grid)

    for i in range(0, grid_len):
        row_len = len(grid[i])
        for j in range(0, row_len):
            if grid[i][j] == 1:
                if i != 0:
                    if grid[i - 1][j] != 1:
                        perimeter += 1
                else:
                    perimeter += 1

                if j != row_len - 1:
                    if grid[i][j + 1] != 1:
                        perimeter += 1
                else:
                    perimeter += 1

                if i != grid_len - 1:
                    if grid[i + 1][j] != 1:
                        perimeter += 1
                else:
                    perimeter += 1

                if j != 0:
                    if grid[i][j - 1] != 1:
                        perimeter += 1
                else:
                    perimeter += 1
    return perimeter
