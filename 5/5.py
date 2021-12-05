"""This script solves both parts of 2021, Day 5"""

import re

import numpy as np


def smart_range(n1, n2):
    """
    Does what range(n1, n2) does except:
        n2 will be included in the generator
        n2 < n1 will automatically count down instead of up
    Used with diagonal lines for part 2
    """
    
    if n2 > n1:
        return range(n1, n2+1)
    else:
        return range(n1, n2-1, -1)
    

if __name__ == '__main__':
    pattern = r'(\d*),(\d*) -\> (\d*),(\d*)'
    
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        
    data = []
    xmax = 0
    ymax = 0    
    for l in lines:
        #use regex to change each line to this list: [x1, y1, x2, y2]
        coordinates = [int(re.match(pattern, l).group(n)) for n in range(1,5)]
        data.append(coordinates)
        xmax = max(xmax, coordinates[0], coordinates[2])
        ymax = max(ymax, coordinates[1], coordinates[3])
    
    ocean = np.zeros((xmax+1, ymax+1))
    diag_ocean = np.copy(ocean)
    
    for coordinates in data:
        x1, y1, x2, y2 = coordinates
        if x1 == x2:
            ocean[x1, min(y1,y2):max(y1,y2)+1] += 1
            diag_ocean[x1, min(y1,y2):max(y1,y2)+1] += 1
        elif y1 == y2:
            ocean[min(x1,x2):max(x1,x2)+1, y1] += 1
            diag_ocean[min(x1,x2):max(x1,x2)+1, y1] += 1
        else:
            #guaranteed by problem statement to be diagonal
            for x, y in zip(smart_range(x1, x2), smart_range(y1, y2)):
                diag_ocean[x,y] += 1
            
            
    #set values of 1 to 0 so we can use np.count_nonzero
    ocean[ocean==1] = 0
    diag_ocean[diag_ocean==1] = 0
    dangerous_areas = np.count_nonzero(ocean)
    diag_areas = np.count_nonzero(diag_ocean)
    print(f'There are {dangerous_areas} areas with 2 or more lines crossing')
    print(f'When considering diagonal lines, there are {diag_areas} areas where 2 or more lines cross.')