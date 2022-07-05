'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
import copy


def update_state(sudoku):
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
    # Go through all the empty cells and make updates to the state is a cell has only one possibe value
    # Keep updating state if have been previous updates
    isUpdated = update_state(sudoku)
    while isUpdated:
        isUpdated = update_state(sudoku)




def backtracking(sudoku):
    # this can be done as a BFS or a DFS solution -- I think DFS makes more sense?? we need to try both and see which on works better
    # TODO: this can be simplified by not checking for immediate neighbors and jsut calling the child function -- if it works, cool if not it just dies out

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


def hybrid_backtracking(sudoku):
    if sudoku.is_solved:
        return sudoku

    extend_fill(sudoku)
    current_empty = sudoku.get_all_empty_cells()[0]
    row, column = current_empty.get_identifiers()

    for guess_value in current_empty.get_possible_values():
        sudoku_copy = copy.deepcopy(sudoku)
        if sudoku_copy.set_value(row, column, guess_value):
            ret = backtracking(sudoku_copy)
            if type(ret) == Sudoku:
                return ret
    return
    