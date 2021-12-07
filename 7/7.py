"""This script solves both parts of 2021, Day 7"""

def pyr_sum(n):
    """ returns the pyramid sum of int n (1+2+3+...+n)"""
    
    return (1 + n) * n // 2


def calc_fuel(crab_pos, final_pos, part=1):
    """
    

    Parameters
    ----------
    crab_pos : list of int
        The horizontal positions of crab subs from the input.
    final_pos : int
        Calculate fuel use to bring all subs to this position.
    part : int (1 or 2), optional
        Choose to calculate fuel use for part 1 or 2. The default is 1.

    Returns
    -------
    int
        total fuel burn for all crab subs.

    """
    
    if part == 1:
        return sum([abs(c-final_pos) for c in crab_pos])
    else:
        return sum([pyr_sum(abs(c-final_pos)) for c in crab_pos])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        pos = [int(n) for n in f.readline().strip().split(',')]
    
    first = True
    for p in range(min(pos), max(pos)+1):
        if first:
            first = False
            min_fuel1 = calc_fuel(pos, p)
            min_fuel2 = calc_fuel(pos, p, part=2)
        else:
            fuel1 = calc_fuel(pos, p)
            fuel2 = calc_fuel(pos, p, part=2)
            if fuel1 < min_fuel1:
                min_fuel1 = fuel1
            if fuel2 < min_fuel2:
                min_fuel2 = fuel2
            
            if fuel2 > min_fuel2 and fuel1 > min_fuel1:
                #starting at position zero, fuel use will 
                #monotonically decrease
                #once it hits minimum, it will monotonically increase
                break
    
    print(f'Optimum part 1 fuel use is {min_fuel1}')
    print(f'Optimum part 2 fuel use is {min_fuel2}')