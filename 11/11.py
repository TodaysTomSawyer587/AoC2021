"""This script solves both parts of 2021, Day 11"""

import numpy as np


def valid(n):
    """Determines if int n is a valid index in a 10x10 array"""
    
    return n >= 0 and n < 10


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        octopuses = np.array([[int(n) for n in line.strip()] 
                                  for line in f.readlines()])
    
    flash_count = 0
    step = 1 
    while step:
        octopuses += 1
        flashes = np.where(octopuses > 9)
        while flashes[0].size > 0:
            for row, col in zip(flashes[0], flashes[1]):
                octopuses[row, col] = 0
                flash_count += 1
                for row_mod in range(-1, 2):
                    for col_mod in range(-1, 2):
                        if valid(row+row_mod) and valid(col+col_mod):
                            if octopuses[row+row_mod, col+col_mod]:
                                octopuses[row+row_mod, col+col_mod] += 1
            flashes = np.where(octopuses > 9)
        
        if step == 100:
            print(f'There are {flash_count} flashes in the first 100 steps')
        
        if np.array_equal(octopuses, np.zeros((10, 10))):
            print(f'Octopuses all flash in step {step}')
            break
        
        step += 1
            