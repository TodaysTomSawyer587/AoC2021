"""This script solves both parts of 2021, Day 12"""

from collections import defaultdict
import re


def is_large_cave(cave):
    """Determines if the cave is large by testing if it's all uppercase"""
    
    return cave.upper() == cave


def traverse(cave_map, visited, current_spot, visited_twice=True):
    """
    Recursively count paths through the cave system

    Parameters
    ----------
    cave_map : dict
        Maps connecting caves to the current location.
    visited : list
        Caves that have been visited on the way to the current spot.
    current_spot : str
        The cave we are currently in.
    visited_twice : bool, optional
        Tracks if a small cave has been visited twice. Also set to True if
        going to a small cave twice is not allowed. The default is True.

    Returns
    -------
    paths : int
        The number of valid paths to the "end" cave.

    """
    
    paths = 0
    visited.append(current_spot)
    for connection in cave_map[current_spot]:
        if connection == 'start':
            continue
        if connection not in visited or is_large_cave(connection) or not visited_twice:
            if not visited_twice and not is_large_cave(connection) and connection in visited:
                cxn_visited_twice = True
            else:
                cxn_visited_twice = visited_twice
            if connection == 'end':
                paths += 1
            else:
                paths += traverse(cave_map, visited[:], connection, 
                                  visited_twice=cxn_visited_twice)
    return paths


if __name__ == '__main__':
    pattern = r'(\w+)-(\w+)'
    cave_map = defaultdict(lambda : [])
    
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            match = re.search(pattern, line)
            cave1 = match.group(1)
            cave2 = match.group(2)
            cave_map[cave1].append(cave2)
            cave_map[cave2].append(cave1)
    
    paths = traverse(cave_map, [], 'start')
    print(f'There are {paths} paths through the cave system')
    
    paths = traverse(cave_map, [], 'start', visited_twice=False)
    print(f'There are {paths} paths when you can visit a small cave twice')