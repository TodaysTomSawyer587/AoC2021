"""This script solves both parts of 2021, Day 17"""

import re


def launch(x_vel, y_vel, target):
    """
    Determine if a given velocity will hit the target

    Parameters
    ----------
    x_vel : int
        x component of velocity.
    y_vel : int
        y component of velocity.
    target : list of int
        the left, right, lower, and upper boundaries of the target.

    Returns
    -------
    target_hit : bool
        whether the target will be hit.

    """
    
    x, y = 0, 0
    target_hit, target_passed = False, False
    ymax = 0
    
    while not (target_hit or target_passed):
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        ymax = max(y, ymax)
        
        target_hit, target_passed = check_target(x, y, target, y_vel)
    
    return target_hit


def check_target(x, y, target, y_vel):
    """
    Determines if the target is hit or passed

    Parameters
    ----------
    x : int
        current x-coordinate of probe.
    y : int
        current y-coordinate of probe.
    target : list of int
        the left, right, lower, and upper boundaries of the target..
    y_vel : int
        the y-velocity of the probe.

    Returns
    -------
    bool
        True if the target is hit.
    bool
        True if the probe missed and has gone past the target.

    """
    
    xmin, xmax, ymin, ymax = tuple(target)
    
    if (xmin <= x
        and xmax >=x
        and ymin <= y
        and ymax >= y):
        return True, False
    
    if y_vel < 0 and y < ymin:
        return False, True
    
    return False, False


def pyramid_sum(n):
    """returns 1 + 2 + 3... + n-1 + n"""
    
    return sum([i for i in range(1, n+1)])


if __name__ == '__main__':
    pattern = r'x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)'
    
    with open('input.txt', 'r') as f:
        match = re.search(pattern, f.readline())
    
    target = [int(match.group(n)) for n in range(1, 5)]
    
    max_height = pyramid_sum(abs(target[2]) - 1)
    print(f'The projectile can go as high as {max_height}')
    
    count = 0
    for y_vel in range(target[2], -target[2] + 1):
        for x_vel in range(target[1] + 1):
            if launch(x_vel, y_vel, target):
                count += 1
    
    print(f'There are {count} velocities that land within the target')