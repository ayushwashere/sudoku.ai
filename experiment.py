'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
# import solver
import backtracking

with open('./data/evil.txt') as fp:
    data = fp.readlines()
    for sudoku_str in data:
        sudoku = Sudoku(sudoku_str)
        sudoku.display()
        result = backtracking.backtracking(sudoku)
        print("--------- SOLVED --------")
        result.display()



# store time_taken, number of attempts made and the memory usage for good testing criteria
# I can store the time taken inside the sudoku itself --