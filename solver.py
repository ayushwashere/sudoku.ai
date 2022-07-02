'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
from emptycell import CellSpace


def update_possibilties(sudoku, cell):
    row, column, block = cell.get_identifiers()

    curr_values = cell.get_possible_values()
    column_values = sudoku.get_column(column)
    row_values = sudoku.get_row(row)
    block_values = sudoku.get_block(block)

    updated_values = list(set(curr_values) - set(column_values) - set(row_values) - set(block_values))
    cell.set_new_values(updated_values)



def create_intial_state_space(sudoku):
    state = []
    empty_cells = sudoku.get_all_empty_cells()
    for element in empty_cells:
        row, column = element
        block = sudoku.calculate_block_from_indices(row, column)
        cell = CellSpace(row, column, block)
        state.append(cell)
    return state


# in this recursive thing, I need to have a special return for when I have exhausted all possibilities but not solved yet
def solve_recursive(sudoku, current_state):
    if len(current_state) == 0:
        print()
        print("----------- SOLVED --------")
        print()
        sudoku.display()

    else:
        next_state = []
        for cell in current_state:
            update_possibilties(sudoku, cell)
            if cell.is_completed():
                row, column, block = cell.get_identifiers()
                value = cell.get_possible_values()[0]
                sudoku.set_value(row, column, value)
            else:
                next_state.append(cell)
        
        if next_state == current_state:
            print("Unable to solve using existing numbers")
            print()
            sudoku.display()
            return 
        return solve_recursive(sudoku, next_state)

