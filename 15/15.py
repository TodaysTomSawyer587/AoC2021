"""
This script solves both parts of 2021, Day 15

My original solution took 10 hours to process the second part. I give credit
to u/skawid on Reddit for posting a Python solution that gave me the
inspiration to work in heapq to my code to speed things up to 2 seconds for
both parts. Here's the link to his comment to the solution thread on Reddit:
    https://www.reddit.com/r/adventofcode/comments/rgqzt5/comment/hs95xc4/?utm_source=share&utm_medium=web2x&context=3

Here's the direct link to the posted solution:
    https://github.com/simonbrahan/aoc2021/commit/dbfbad0fc57d5ee56bd49e894fc2f62e9c47cc39

"""


import datetime
import heapq

import numpy as np


def check_neighbors(grid, travel_cost, coordinates, unvisited, candidates):
    
    x, y = coordinates
    current_distance = travel_cost[x, y]
    
    if x and (x-1, y) in unvisited:
        travel_cost[x-1, y] = min(grid[x-1, y] + current_distance, 
                                  travel_cost[x-1, y])
        heapq.heappush(candidates, (travel_cost[x-1, y], (x-1, y)))
    if x + 1 < grid.shape[0] and (x+1, y) in unvisited:
        travel_cost[x+1, y] = min(grid[x+1, y] + current_distance, 
                                  travel_cost[x+1, y])
        heapq.heappush(candidates, (travel_cost[x+1, y], (x+1, y)))
    if y and (x, y-1) in unvisited:
        travel_cost[x, y-1] = min(grid[x, y-1] + current_distance, 
                                  travel_cost[x, y-1])
        heapq.heappush(candidates, (travel_cost[x, y-1], (x, y-1)))
    if y + 1 < grid.shape[1] and (x, y+1) in unvisited:
        travel_cost[x, y+1] = min(grid[x, y+1] + current_distance, 
                                  travel_cost[x, y+1])
        heapq.heappush(candidates, (travel_cost[x, y+1], (x, y+1)))
    
    return travel_cost


def calc_path_risk(grid):
    
    travel_cost = np.ones(grid.shape) * np.inf
    travel_cost[0, 0] = 0
    unvisited = set(())
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            unvisited.add((x, y))
    candidates = []
    heapq.heappush(candidates, (0, (0, 0)))
    target = (grid.shape[0] - 1, grid.shape[1] - 1)
    
    while target in unvisited:
        last_visited = heapq.heappop(candidates)[1]
        if last_visited not in unvisited:
            continue
        travel_cost = check_neighbors(grid, travel_cost, last_visited, 
                                      unvisited, candidates)
        unvisited.discard(last_visited)
        
    return travel_cost[target]


if __name__ == '__main__':
    start = datetime.datetime.now()
    
    with open('input.txt', 'r') as f:
        original_grid = np.array([[int(n) for n in line.strip()] 
                                  for line in f.readlines()])
    
    grid = original_grid.copy()
    horiz_tiles = []
    for n in range(1, 5):
        tile_grid = grid + n
        tile_grid[tile_grid > 9] -= 9
        horiz_tiles.append(tile_grid)
    
    for h in horiz_tiles:
        grid = np.concatenate((grid, h))
    
    vert_tiles = []
    for n in range(1, 5):
        tile_grid = grid + n
        tile_grid[tile_grid > 9] -= 9
        vert_tiles.append(tile_grid)
    
    for v in vert_tiles:
        grid = np.concatenate((grid, v), axis=1)
        
    soln1 = calc_path_risk(original_grid)
    
    print(f'The lowest risk path in part 1 is {soln1}')
    
    soln2 = calc_path_risk(grid)    
    
    print(f'The lowest risk path in part 2 is {soln2}')
    
    end = datetime.datetime.now()
    time = (end - start).seconds
    print(f'Solution took {time} seconds')
            
    