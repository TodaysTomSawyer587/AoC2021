"""This script solves both parts of 2021, Day 8"""

import re


def segment_set(chars):
    """Returns the chars in the string as a set"""
    
    out = set(())
    for c in chars:
        out.add(c)
    return out


def segments_to_digit(chars, segment_maps):
    """
    

    Parameters
    ----------
    chars : str
        display segments
    segment_maps : dict
        a mapping of digits to solved segment sets.

    Returns
    -------
    digit : int
        the digit with the respective segments

    """
    
    s = segment_set(chars)
    for digit, seg_set in segment_maps.items():
        if s == seg_set:
            return digit


if __name__ == '__main__':
    pattern = '([a-g]+) ' * 10 + r'\|' + ' ([a-g]+)' * 4
    
    #segments is a set that keeps track of the different segment combos
    segments = set(())
    
    # #segments is {displayed number: segments that currently show}
    # segments = {}
    
    #soln1 and soln2 track the answers to part 1 and 2, respectively
    #soln1 counts the number of occurances for 1/4/7/8
    #soln2 sums the output digits
    soln1 = 0
    soln2 = 0
    
    with open('input.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        
    for line in lines:
        iteration = 1
        match = re.search(pattern, line)
        output = [match.group(n) for n in range(1, 15)]
        #solved is {displayed number: its segments as str}
        solved = {8 : segment_set('abcdefg')}
        while len(solved) < 10 and iteration < 10:
            for o in output:
                if len(o) == 2:
                    if 1 not in solved:
                        solved[1] = segment_set(o)
                elif len(o) == 3:
                    if 7 not in solved:
                        solved[7] = segment_set(o)
                elif len(o) == 4:
                    if 4 not in solved:
                        solved[4] = segment_set(o)
                elif len(o) == 5:
                    #3 is the only 5-segment digit containing both segments from 1
                    if 3 not in solved:
                        try:
                            if segment_set(o).intersection(solved[1]) == solved[1]:
                                solved[3] = segment_set(o)
                        except KeyError:
                            pass
                    #5 is the only 5-segment digit containing the two segments
                    # from 4 that are not in one
                    if 5 not in solved:
                        try:
                            test_segs = solved[4] - solved[1]
                            if segment_set(o).intersection(test_segs) == test_segs:
                                solved[5] = segment_set(o)
                        except KeyError:
                            pass
                    #2 is the only 5-segment digit sharing exactly 3 segments with 5
                    if 2 not in solved:
                        try:
                            if len(segment_set(o).intersection(solved[5])) == 3:
                                solved[2] = segment_set(o)
                        except KeyError:
                            pass
                elif len(o) == 6:
                    #6 is the only 6-segment digit not containing both segments from 1
                    if 6 not in solved:
                        try:
                            if segment_set(o).intersection(solved[1]) != solved[1]:
                                solved[6] = segment_set(o)
                        except KeyError:
                            pass
                    #9 is the only 6-segment digit containing all segments from 4
                    if 9 not in solved:
                        try:
                            if segment_set(o).intersection(solved[4]) == solved[4]:
                                solved[9] = segment_set(o)
                        except KeyError:
                            pass
                    #0 is the only 6-segment digit not containing all segments from 5
                    if 0 not in solved:
                        try:
                            if segment_set(o).intersection(solved[5]) != solved[5]:
                                solved[0] = segment_set(o)
                        except KeyError:
                            pass
            iteration += 1
            
        if len(solved) < 10:
            print(solved)
            raise RuntimeError('Max iterations reached.')
            
        for place, o in enumerate(output[-4:]):
            if segments_to_digit(o, solved) in [1, 4, 7, 8]:
                soln1 += 1
            soln2 += segments_to_digit(o, solved) * 10 ** (3 - place)
            
    print(f'The digits 1, 4, 7, and 8 appear {soln1} times')
    
    print(f'All numbers in the output sum to {soln2}')
    