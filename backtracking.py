'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
from emptycell import EmptyCell
import copy


def backtracking(sudoku):
    # this can be done as a BFS or a DFS solution -- I think DFS makes more sense?? we need to try both and see which on works better
    # TODO: this can be simplified by not checking for immediate neihbiars and jsut calling the child function -- if it works, cool if not it just dies out

    if sudoku.is_solved:
        return sudoku
    current_empty = sudoku.get_all_empty_cells()[0]
    row, column = current_empty.get_identifiers()
    
    valid_children = []
    for guess_value in current_empty.get_possible_values():
        sudoku_copy = copy.deepcopy(sudoku)
        if sudoku_copy.set_value(row, column, guess_value):
            valid_children.append(sudoku_copy)

    for next_sudoku in valid_children:
        ret = backtracking(next_sudoku)
        if type(ret) == Sudoku:
            return ret
    return


# ----------- COMPARISON -----------
'''
1. total time taken
2. count the total number of nodes/states generated
'''



def hybrid_backtracking(sudoku):
    # implementing a 

    if sudoku.is_solved:
        return sudoku

    
    # before I start making any guesses, I narrow down the possible guesses and the impact of any existing guess
    # so If I made a guess in the previous one --or-- starting raw, I want to solve it all the way such that 

    current_empty = sudoku.get_all_empty_cells()[0]
    row, column = current_empty.get_identifiers()

    valid_children = []
    for guess_value in current_empty.get_possible_values():
        sudoku_copy = copy.deepcopy(sudoku)
        if sudoku_copy.set_value(row, column, guess_value):
            valid_children.append(sudoku_copy)

    for next_sudoku in valid_children:
        ret = backtracking(next_sudoku)
        if type(ret) == Sudoku:
            return ret
    return