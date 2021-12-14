"""This script solves both parts of 2021, Day 13"""

import re

import numpy as np


def fold(grid, axis, coordinate):
    """
    Fold the paper along the given axis and coordinate

    Parameters
    ----------
    grid : np.ndarry of int
        integers representing the paper (non-zero have dots).
    axis : str
        'x' or 'y'. whether the fold is along "x=" or "y="
    coordinate : int
        what coordinate the paper is folded along.

    Returns
    -------
    np.ndarry of int
        The grid after folding.

    """
    
    if axis == 'x':
        bottom = grid[:coordinate, :]
        top = grid[coordinate+1:, :]
        return bottom + np.flip(top, 0)
    else:
        bottom = grid[:, :coordinate]
        top = grid[:, coordinate+1:]
        return bottom + np.flip(top, 1)
    

if __name__ == '__main__':
    dot_pattern = r'(\d+),(\d+)'
    fold_pattern = r'fold along ([x,y])=(\d+)'
    dots = []
    folds = []
    
    reading_folds = False
    xmax = 0
    ymax = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if reading_folds:
                match = re.search(fold_pattern, line)
                axis = match.group(1)
                coordinate = int(match.group(2))
                folds.append((axis, coordinate))
            else:
                match = re.search(dot_pattern, line)
                if match:
                    x = int(match.group(1))
                    y = int(match.group(2))
                    xmax = max(x+1, xmax)
                    ymax = max(y+1, ymax)
                    dots.append((x, y))
                else:
                    reading_folds = True
    
    grid = np.zeros((xmax, ymax))
    for d in dots:
        grid[d[0], d[1]] += 1
    
    for i, f in enumerate(folds):
        grid = fold(grid, f[0], f[1])
        dots_visible = np.count_nonzero(grid)
        if not i:
            print(f'{dots_visible} dots are visible')
    
    #Where the grid has dots (i.e. is non-zero), print "#"
    for y in range(grid.shape[1]):
        row = ['#' if x > 0 else ' ' for x in grid[:, y]]
        line = ''
        for char in row:
            line += char
        print(line)
    
    