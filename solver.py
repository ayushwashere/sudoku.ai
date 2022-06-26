'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from threading import currentThread
from sudoku import Sudoku
from cell_space import CellSpace


def update_possibilties(sudoku, cell):
    row, column, block = cell.get_identifiers()

    curr_values = cell.get_possible_values()
    column_values = sudoku.get_column(column)
    row_values = sudoku.get_row(row)
    block_values = sudoku.get_block(block)

    updated_values = list(set(curr_values) - set(column_values) - set(row_values) - set(block_values))
    cell.set_new_values(updated_values)

    if len(updated_values) == 1:
        return True
    return False



def create_intial_state_space(sudoku):
    state = []
    empty_cells = sudoku.get_all_empty_cells()
    for element in empty_cells:
        row, column = element
        block = sudoku.calculate_block_from_indices(row, column)
        cell = CellSpace(row, column, block)
        state.append(cell)
    return state



def solve_recursive(sudoku, current_state):
    if len(current_state) == 0:
        print()
        print("----------- SOLVED --------")
        print()
        sudoku.display()
    else:
        next_state = []
        for cell in current_state:
            if not cell.is_completed():
                if update_possibilties(sudoku, cell):
                    row, column, block = cell.get_identifiers()
                    value = cell.get_possible_values()[0]
                    sudoku.set_value(row, column, value)
                else:
                    next_state.append(cell)
        return solve_recursive(sudoku, next_state)




sudoku_str = "-31-----6;-492---38;-2--1--45;75---6---;2-8--56--;-96-3275-;-62-7---4;--5--93-7;-7-561-2-"
sudoku = Sudoku(sudoku_str)
sudoku.display()

current_state = create_intial_state_space(sudoku)
solve_recursive(sudoku, current_state)

for el in current_state:
    print(el)