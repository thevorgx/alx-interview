#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island using a grid"""

    perimeter = 0
    grid_rows = len(grid)
    grid_columns = len(grid[0]) if grid_rows > 0 else 0

    for i in range(grid_rows):
        for j in range(grid_columns):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == grid_rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == grid_columns - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
