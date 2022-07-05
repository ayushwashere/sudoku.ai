'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
import copy

# ----------------- STATE SPACE REDUCTION -----------------

def update_state(sudoku):
    '''
    Makes updates for one layer in the state space, that is, goes through all empty cells once.
    '''

    isUpdated = False

    all_empty = sudoku.get_all_empty_cells()
    for empty_cell in all_empty:
        row, column = empty_cell.get_identifiers()
        
        row_values = sudoku.get_row(row)
        column_values = sudoku.get_column(column)
        block_values = sudoku.get_block(row, column)
        
        possible_values = empty_cell.get_possible_values()
        new_values = list(set(possible_values) - set(column_values) - set(row_values) - set(block_values))
        empty_cell.set_new_values(new_values)
        
        if len(new_values) == 1:
            sudoku.set_value(row, column, new_values[0])
            isUpdated = True
    return isUpdated




def extend_fill(sudoku):
    '''
    Driver function for running the State Space Reduction layer after layer until no changes are possible or solved
    '''
    isUpdated = update_state(sudoku)
    while isUpdated:
        isUpdated = update_state(sudoku)



# ----------------- BACKTRACKING -----------------

def backtracking(sudoku):
    '''
    Recursively check if a sudoku is solved. If not solved, yet, make a guess in an empty cell and check again
    '''

    if sudoku.is_solved:
        return sudoku
    current_empty = sudoku.get_all_empty_cells()[0]
    row, column = current_empty.get_identifiers()
    
    # TODO: This can be changed to not check all children before calling recursively
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



# ----------------- HYBRID BACKTRACKING -----------------

def hybrid_backtracking(sudoku):
    '''
    Recursively check if a sudoku is solved. If not solved, yet, make a guess in an empty cell and solve all empty cells that
    can be determined from this guess. Then make another guess and repeat process until solved
    '''
    extend_fill(sudoku)
    if sudoku.is_solved:
        return sudoku

    current_empty = sudoku.get_all_empty_cells()[0]
    row, column = current_empty.get_identifiers()

    for guess_value in current_empty.get_possible_values():
        sudoku_copy = copy.deepcopy(sudoku)
        if sudoku_copy.set_value(row, column, guess_value):
            ret = backtracking(sudoku_copy)
            if type(ret) == Sudoku:
                return ret
    return
    