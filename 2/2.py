"""This script solves both parts of 2021, Day 2"""

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        
    horizontal = 0
    depth = 0
    aim = 0
    aim_depth = 0
    
    #all movements are by single digits
    for l in lines:
        if l.startswith('forward'):
            horizontal += int(l[-1])
            aim_depth += aim * int(l[-1])
        elif l.startswith('up'):
            depth -= int(l[-1])
            aim -= int(l[-1])
        elif l.startswith('down'):
            depth += int(l[-1])
            aim += int(l[-1])
    
    print(f'Part 1: depth * horizontal position = {depth * horizontal}')
    print(f'Part 2: depth * horizontal position = {aim_depth * horizontal}')