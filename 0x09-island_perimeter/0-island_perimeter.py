#!/usr/bin/python3

'''
0-island_perimeter.py
'''


def island_perimeter(grid):
    '''
    returns the perimeter of the island described in grid
    '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += sum([
                        1 if i - 1 < 0 or not grid[i - 1][j]
                        else 0,
                        1 if i + 1 >= len(grid) or not grid[i + 1][j]
                        else 0,
                        1 if j - 1 < 0 or not grid[i][j - 1]
                        else 0,
                        1 if j + 1 >= len(grid[0]) or not grid[i][j + 1]
                        else 0,
                        ])
    return (perimeter)
