"""This script solves both parts of 2021, Day 3"""

def col_bit(lines, col_no, oxygen=True):
    """
    Determines the most common bit or least common bit in the remaining
    lines when calculating oxygen and co2 ratings.

    Parameters
    ----------
    lines : list of strings
        The remaining lines when calculating oxygen and co2 ratings.
    col_no : int
        The column to examine.
    oxygen : bool, optional
        True when determining oxygen rating. 
        False for CO2. The default is True.

    Returns
    -------
    str
        '1' or '0'.

    """
    
    col_sum = sum([int(l[col_no]) for l in lines])
    
    if col_sum >= len(lines) / 2:
        out = 1
    else:
        out = 0
    
    if not oxygen:
        out = 1 - out
    
    return str(out)
    

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    
    #Part 1: determine power consumption
    line_count = len(lines)
    col_count = len(lines[0])
    #use a dictionary to keep track of number of 1s by index
    ones = {}
    for n in range(col_count):
        ones[n] = 0
    
    for l in lines:
        for n in range(col_count):
            if l[n] == '1':
                ones[n] += 1
    
    gamma_rate = ''
    for n in range(col_count):
        if ones[n] > line_count / 2:
            gamma_rate += '1'
        else:
            gamma_rate += '0'
        
    gamma_rate = int(gamma_rate, 2)
    mask = int('1' * col_count, 2)
    epsilon_rate = ~gamma_rate & mask
    
    print(f'The power consumption is {gamma_rate * epsilon_rate}')
    
    #Part 2: determine life support rating
    oxy_lines = lines[:]
    co2_lines = lines[:]
    for col in range(col_count):
        oxy_bit = col_bit(oxy_lines, col)
        co2_bit = col_bit(co2_lines, col, oxygen=False)
        oxy_deletions = []
        co2_deletions = []
        for i, line in enumerate(oxy_lines):
            if line[col] != oxy_bit:
                oxy_deletions.append(i)
        for i, line in enumerate(co2_lines):
            if line[col] != co2_bit:
                co2_deletions.append(i)
        for d in reversed(oxy_deletions):
            oxy_lines.pop(d)
        for d in reversed(co2_deletions):
            if len(co2_lines) == 1:
                #without this, the last line will be removed
                #because it always has the most common bit
                break
            co2_lines.pop(d)
    
    #at this point there should only be one line left in each list
    oxy_rating = int(oxy_lines[0], 2)
    co2_rating = int(co2_lines[0], 2)
    
    print(f'The life support rating is {oxy_rating * co2_rating}')