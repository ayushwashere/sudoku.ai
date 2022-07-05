'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
import solver

import sys
import time
import random

mode, method = sys.argv[1:]

def solve_sudoku(sudoku_str, method):
    start_time = time.time()
    
    sudoku = Sudoku(sudoku_str)
    sudoku.display()
    
    if method == 'reduction':
        solver.extend_fill(sudoku)
        result = sudoku
        if not sudoku.is_solved:
            print("Cannot Solve Using State Space Reduction")
    elif method == 'backtracking':
        result = solver.backtracking(sudoku)
    elif method == 'hybrid':
        result = solver.hybrid_backtracking(sudoku)
    
    print("Solved\n")
    result.display()
    end_time = time.time()
    time_taken = end_time - start_time
    print("Time Taken: {}s".format(time_taken))


if mode in ['easy', 'medium', 'hard', 'evil'] and method in ['reduction', 'backtracking', 'hybrid']:
    with open('./data/{}.txt'.format(mode)) as fp:
        data = fp.readlines()
        select_index = random.randint(0, len(data)-1)
        sudoku_str = data[select_index]
        solve_sudoku(sudoku_str, method)
else:
    print("Try again!")
    