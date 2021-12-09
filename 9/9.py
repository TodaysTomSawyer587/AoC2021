"""This script solves both parts of 2021, Day 9"""

import numpy as np


def find_neighbors(coordinates, heightmap):
    """
    Finds neighbors' heights in the cardinal directions from given coordinates.

    Parameters
    ----------
    coordinates : tuple: (int, int)
        (x, y) coordinates of a point to find neighbors for
    heightmap : 2-D np int array
        the height map from the problem's input

    Returns
    -------
    neighbors : list of int
        The heights of applicable neighbors.

    """
    
    x, y = coordinates
    xmax, ymax = heightmap.shape
    neighbors = []
    if x:
        neighbors.append(heightmap[x-1, y])
    if x < xmax - 1:
        neighbors.append(heightmap[x+1, y])
    if y:
        neighbors.append(heightmap[x, y-1])
    if y < ymax - 1:
        neighbors.append(heightmap[x, y+1])
    
    return neighbors


def coord_str(coordinates):
    """Converts a tuple of integer coordinates to a string"""
    
    x, y = coordinates
    return f'({x}, {y})'


class Basin:
    """Represents a basin for part 2"""
    
    def __init__(self, low_point, heightmap):
        """
        Creates basin starting at the low point

        Parameters
        ----------
        low_point : tuple: (int, int)
            The coordinates of the low point of the basin.
        heightmap : 2-D np int array
            the height map from the problem's input

        """
        
        self.coordinates = set(())
        self._propagate(low_point, heightmap)
        
    @property
    def size(self):
        """Gives the size of the basin"""
        
        return len(self.coordinates)
    
    def _propagate(self, coordinates, heightmap):
        """
        Recursively finds higher neighboring points less than 9 and
        adds them to the object's set of coordinates

        Parameters
        ----------
        coordinates : tuple: (int, int)
            The point from which to propagate in the cardinal directions.
        heightmap : 2-D np int array
            the height map from the problem's input

        """
        x, y = coordinates
        self.coordinates.add(coord_str(coordinates))
        current = heightmap[x, y]
        xmax, ymax = heightmap.shape
        if x:
            neighbor = heightmap[x-1, y]
            if neighbor < 9 and neighbor > current:
                self._propagate((x-1, y), heightmap)
        if x < xmax - 1:
            neighbor = heightmap[x+1, y]
            if neighbor < 9 and neighbor > current:
                self._propagate((x+1, y), heightmap)
        if y:
            neighbor = heightmap[x, y-1]
            if neighbor < 9 and neighbor > current:
                self._propagate((x, y-1), heightmap)
        if y < ymax - 1:
            neighbor = heightmap[x, y+1]
            if neighbor < 9 and neighbor > current:
                self._propagate((x, y+1), heightmap)
                

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        heightmap = np.array([[int(n) for n in line.strip()] 
                                  for line in f.readlines()])
        
    xmax, ymax = heightmap.shape
    risk_sum = 0
    basins = []
    
    for x in range(xmax):
        for y in range(ymax):
            neighbors = find_neighbors((x, y), heightmap)
            
            if heightmap[x, y] < min(neighbors):
                risk_sum += heightmap[x, y] + 1
                basins.append(Basin((x, y), heightmap))
    
    print(f'The risk levels of all low points sum to {risk_sum}')
    sizes = sorted([b.size for b in basins])
    soln2 = sizes[-1] * sizes[-2] * sizes[-3]
    print(f'The product of the 3 largest basin sizes is {soln2}')