'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from sudoku import Sudoku
import copy

'''
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

'''

'''
In this approach, I'm creating an initial state space and then iteratively reducing it

1. I look at each spot and reduce the set of possible values that can exist there
2. If there's only one possible value, I set that value
3. repeat step 1

'''

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


# ----------- COMPARISON -----------
'''
1. total time taken
2. count the total number of nodes/states generated
'''


def hybrid_backtracking(sudoku):

    if sudoku.is_solved:
        return sudoku

    # ??? : do i need to check if the update will run into some problems?? that is if it sets a value that shouldn't be set
    #       i think the checks in Sudoku.set_value() shuold be able to catch that but idk -- let's see
    extend_fill(sudoku)


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