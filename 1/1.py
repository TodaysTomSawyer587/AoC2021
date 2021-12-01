"""This script solves both parts of 2021, Day 1"""

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [int(l.strip()) for l in f.readlines()]
        
    increases = 0
    prev = 0
    #tmr = three-measurement rolling
    tmr_increases = 0
    tmr_measurements = []
    for i, l in enumerate(lines):
        #Solve using single measurements
        if i and l > prev:
            increases += 1
        prev = l
        
        #Solve using three-measurement rolling (tmr) sums
        current = sum(tmr_measurements)
        tmr_measurements.append(l)
        if i > 2:
            tmr_measurements.pop(0)
            if sum(tmr_measurements) > current:
                tmr_increases += 1            
    
    print(f'Ocean depth increases {increases} times')
    print()
    print(f'Using three-measurement rolling sums, ocean depth increases {tmr_increases} times')