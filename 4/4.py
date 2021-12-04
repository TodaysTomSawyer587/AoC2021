"""This script solves both parts of 2021, Day 4"""

import numpy as np


class BingoBoard:
    
    def __init__(self, raw_input, verbose=False):
        """
        Parameters
        ----------
        raw_input : list of strings
            5 lines from the input file that represent a bingo card.
        verbose : bool, optional
            Set to True for additional output for debugging. 
            The default is False.
        """

        self.marked = np.zeros((5, 5))
        self.board = np.zeros((5, 5))
        self.done = False
        self.verbose = verbose
        
        for i, line in enumerate(raw_input):
            self.board[i, :] = [int(line[n*3:n*3+2]) for n in range(5)]
        if verbose:
            print(self.board)
            
    def check_number(self, n):
        """
        Checks if a called number is on the board.
        If it is, that space on the board is marked, and
        victory conditions are checked.

        Parameters
        ----------
        n : int
            The bingo number called.

        Returns
        -------
        int
            0 if victory not yet acheived. Score if victory achieved.

        """
        try:
            index = np.where(self.board == n)
            self.marked[index[0][0], index[1][0]] = 1
            if self.verbose:
                print(f'Found {n} at ({index[0][0]}, {index[1][0]})')
                print(f'Marked spaces are now \n{self.marked}')
            self.last_number = n
        except IndexError:
            return 0
        
        return self.victory
        
    @property
    def victory(self):
        """
        Determines if the card is a winner by checking for filled
        rows and columns. Calculates score if victory achieved.

        Returns
        -------
        int
            0 if victory not yet acheived. Score if victory achieved.

        """
        row_sums = np.sum(self.marked, axis=1)
        col_sums = np.sum(self.marked, axis=0)
        
        if self.verbose:
            print(f'Row and col sums are {np.concatenate((row_sums, col_sums))}')
        
        if max(np.concatenate((row_sums, col_sums))) == 5:
            if self.verbose:
                print(f'This board wins with a score of {self.score}')
            return self.score
        else:
            return 0
        
    @property
    def score(self):
        """Returns the score of a victorious card"""
        unmarked = 1 - self.marked
        return np.sum(unmarked * self.board) * self.last_number


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    numbers_called = [int(n) for n in lines[0].split(',')]
    boards = []
    
    for l in range(2, len(lines), 6):
        boards.append(BingoBoard(lines[l:l+5]))
    
    over = False
    count = 0
    for nc in numbers_called:
        for b in boards:
            if b.done:
                continue
            if b.check_number(nc):
                b.done = True
                count += 1
                if over:
                    last_score = b.check_number(nc)
                else:
                    print(f"The winning board's score is {b.check_number(nc)}")
                    over = True
    print(f"The losing board's score is {last_score}")