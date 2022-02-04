"""
This module solves both parts of Day 18.
Snail numbers are represented as a list of lists.
Each element in the primary list represents a real number in the snail number.
Each secondary list has two ints: the first is the real number.
The second is the number of brackets the real number is inside.
"""


from copy import deepcopy

def isint(char):
    """Determines if str char can be retyped to an int"""
    
    try:
        int(char)
    except ValueError:
        return False
    
    return True


def process(raw_number):
    """Converts line of input text to snail number"""
    
    level = 0
    digits = []
    
    for char in raw_number:
        if char == '[':
            level += 1
        elif char == ']':
            level -= 1
        elif isint(char):
            digits.append([int(char), level])
        
    return digits


def snail_add(n1, n2):
    """Returns the sum of snail numbers n1, n2"""
    
    out = deepcopy(n1) + deepcopy(n2)
    for i in range(len(out)):
        out[i][1] += 1
    return out


def explode(number):
    """Explodes input if necessary. Return True if explosion ocurred."""
    
    explode = None
    
    for i, digit in enumerate(number):
        if digit[1] == 5:
            explode = i
            break
    
    if explode is None:
        return False
    
    left = number[explode][0]
    right = number.pop(explode + 1)[0]
    
    if explode > 0:
        number[explode - 1][0] += left
    if explode + 1 < len(number):
        number[explode + 1][0] += right
    number[explode] = [0, 4]
    
    return True


def split(number):
    """Splits input if necessary. Return True if split ocurred."""
    
    split_loc = None
    
    for i, digit in enumerate(number):
        if digit[0] > 9:
            split_loc = i
            split_no = digit
            break
    
    if split_loc is None:
        return False
    
    number[split_loc] = [split_no[0] // 2, split_no[1] + 1]
    number.insert(split_loc + 1, 
                  [split_no[0] // 2 + split_no[0] % 2, split_no[1] + 1])
    
    return True


def magnitude(number):
    """Returns magnitude of the input"""
    
    level = 4
    
    while level:
        mag_pos = None
        for i, digit in enumerate(number):
            if digit[1] == level:
                mag_pos = i
                break
        
        if mag_pos is None:
            level -= 1
            continue
        
        magnitude = number[mag_pos][0] * 3 + number[mag_pos+1][0] * 2
        
        number.pop(mag_pos + 1)
        number[mag_pos] = [magnitude, level - 1]
    
    return magnitude
    

if __name__ == '__main__':
    line = True
    with open('input.txt', 'r') as f:
        raw_numbers = [l.strip() for l in f.readlines()]
    
    numbers = [process(r) for r in raw_numbers]
    highest_mag = 0
    
    for i, n in enumerate(numbers):
        if not i:
            final_sum = deepcopy(n)
            continue
        final_sum = snail_add(final_sum, n)
    
        restart = True
        while restart:
            restart = explode(final_sum)
            if restart: continue
        
            restart = split(final_sum)
        
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers):
            if j == i: continue
            temp = snail_add(n, m)
            restart2 = True
            while restart2:
                restart2 = explode(temp)
                if restart2: continue
            
                restart2 = split(temp)
            
            highest_mag = max(highest_mag, magnitude(temp))
            
            
        
    print('Part 1 solution:')
    print(magnitude(final_sum))
    print()
    
    print('Part 2 solution:')
    print(highest_mag)
    print()
    