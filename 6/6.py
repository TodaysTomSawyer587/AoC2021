"""This script solves both parts of 2021, Day 6"""

def sum_fish(count):
    """Provides the sum of all values in the dictionary"""
    
    return sum([count[n] for n in range(9)])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        fish = [int(n) for n in f.readline().strip().split(',')]
    
    fish_count = {n:0 for n in range(9)}
    while fish:
        fish_count[fish.pop()] += 1
        
    for day in range(256):
        new_fish_count = {n:fish_count[n+1] for n in range(8)}
        new_fish_count[8] = fish_count[0]
        new_fish_count[6] += fish_count[0]
        fish_count = new_fish_count.copy()
        
        if day == 79:
            print(sum_fish(fish_count))
    
    print(sum_fish(fish_count))