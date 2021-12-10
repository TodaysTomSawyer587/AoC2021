"""This script solves both parts of 2021, Day 9"""

if __name__ == "__main__":
    score = 0
    
    bracket_map = {'<' : '>',
                   '(' : ')',
                   '[' : ']',
                   '{' : '}'}
    
    score_map = {')' : 3,
                 ']' : 57,
                 '}' : 1197,
                 '>' : 25137}
    
    completion_score_map = {')' : 1,
                            ']' : 2,
                            '}' : 3,
                            '>' : 4}
            
    autocomplete_scores = []
    
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            
            #check if the line is corrupt
            corrupt = False
            open_brackets = []
            for c in line.strip():
                if c in bracket_map:
                    open_brackets.append(c)
                else:
                    if bracket_map[open_brackets.pop()] != c:
                        score += score_map[c]
                        corrupt = True
            if corrupt:
                continue
            
            #if the line is not corrupt, it is incomplete. score it.
            completion = [bracket_map[ob] for ob in open_brackets]
            completion_string = ''
            while(completion):
                completion_string += completion.pop()
            completion_score = 0
            for c in completion_string:
                completion_score *= 5
                completion_score += completion_score_map[c]
            autocomplete_scores.append(completion_score)
            
                    
    print(f'The score from corrupt lines is {score}')
    
    winner_part_2 = sorted(autocomplete_scores)[len(autocomplete_scores)//2]
    print(f'The autocomplete winning score is {winner_part_2}')