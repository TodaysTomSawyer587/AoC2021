"""This script solves both parts of 2021, Day 14"""

from collections import defaultdict
import re


def count_elements(polymer, start_letter, end_letter):
    """
    Translate a polymer from a dictionary of pair counts to a count
    of individual elements.

    Parameters
    ----------
    polymer : defaultdict
        element pairs : number of occurances.
    start_letter : str
        the letter at the start of the polymer
    end_letter : str
        the letter at the end of the polymer

    Returns
    -------
    count : defaultdict
        element : number of occurances.

    """
    
    count = defaultdict(lambda : 0)
    for pair, amount in polymer.items():
        for element in pair:
            count[element] += amount
    
    #every letter is counted twice except the beginning and the end, 
    #which don't change
    for element in count:
        count[element] //= 2
        if element in [start_letter, end_letter]:
            count[element] += 1
            
    return count


def element_diff(count):
    """Returns the difference in occurences of the most
       and least common elements"""
    
    min_element = None
    max_element = None
    
    for element, amount in count.items():
        if not min_element:
            min_element = element
            max_element = element
        else:
            if amount < count[min_element]:
                min_element = element
            elif amount > count[max_element]:
                max_element = element
    
    return count[max_element] - count[min_element]


if __name__ == '__main__':
    pattern = r'([A-Z][A-Z]) -\> ([A-Z])'
    rules = {}
    
    with open('input.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                start = line.strip()
                start_letter = start[0]
                end_letter = start[-1]
            elif i == 1:
                continue
            else:
                match = re.search(pattern, line.strip())
                #list rules as a dict of {pair: inserted element}
                rules[match.group(1)] = match.group(2)
    
    polymer = defaultdict(lambda : 0)
    for i in range(len(start) - 1):
        polymer[start[i:i+2]] += 1
        
    for step in range(40):
        new_polymer = defaultdict(lambda : 0)
        for pair, count in polymer.items():
            if pair in rules:
                insert = rules[pair]
                new_polymer[pair[0] + insert] += count
                new_polymer[insert + pair[1]] += count
            else:
                new_polymer[pair] += count
        
        polymer = new_polymer.copy()
        if step == 9:
            polymer1 = polymer.copy()
    
    count1 = count_elements(polymer1, start_letter, end_letter)
    count2 = count_elements(polymer, start_letter, end_letter)
    
    element_diff1 = element_diff(count1)
    element_diff2 = element_diff(count2)
        
    print('The differences between the most and least common elements are:')
    print(f'At step 10: {element_diff1}')
    print(f'At step 40: {element_diff2}')
        