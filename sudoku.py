'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

from emptycell import EmptyCell


class Sudoku:
    def __init__(self, base_str):
        """
        Create a Sudoku object using an input string where each empty space is represented by '-'
        and the end of a row is denoted by semicolon (;)
        """

        def parse_input_string(base_str):
            data = base_str.split(';')
            grid = [[row[c] if row[c] != '-' else EmptyCell(r, c) for c in range(0, len(row))] for r, row in enumerate(data)]
            return grid

        self.grid = parse_input_string(base_str)
        self.is_solved = False


    def display(self):
        """
        Display the Sudoku in the terminal
        """
        # TODO: create an interactive GUI for this
        for i, row in enumerate(self.grid):
            row = ["_" if type(cell) == EmptyCell else cell for cell in row]
            print_str = ''.join(row[:3]) + " | " + ''.join(row[3:6]) + " | " + ''.join(row[6:])
            print(print_str)
            if i in [2, 5]:
                print(" ---- "*3)

    
    def get_block(self, row, column):
        """
        Get values in a certain block (indexed by row and column) as a list
        Empty Cells are returned as referrences to the corresponding EmptyCell object
        """
        block_data = []
        block = 3 * (row // 3) + (column // 3)
        rows = self.grid[3*(block//3):3*(block//3)+3]
        for row in rows:
            cdata = row[3*(block%3):3*(block%3)+3]
            block_data += cdata
        return block_data
        
    
    def get_row(self, row):
        """
        Get values in a certain row as a list
        Empty Cells are returned as referrences to the corresponding EmptyCell object
        """
        return self.grid[row]

    
    def get_column(self, column):
        """
        Get values in a certain column as a list
        Empty Cells are returned as referrences to the corresponding EmptyCell object
        """
        return [row[column] for row in self.grid]

    
    def get_all_empty_cells(self):
        """
        Returns a list of all EmptyCell objects in the Sudoku
        """
        empty = [[cell for cell in row if type(cell)==EmptyCell] for row in self.grid]
        return [item for sublist in empty for item in sublist]
    
    
    def set_value(self, row, column, value):
        """
        Tries to update value (if possible) into the Sudoku at specified position (row, column)
        
        Returns:
            True: If value can be inserted without any confliects
            False: If value will create conflicts
        """
        value = str(value)
        
        row_data = self.get_row(row)
        column_data = self.get_column(column)
        block_data = self.get_block(row, column)

        if value not in (row_data + column_data + block_data):
            self.grid[row][column] = value
            self._check_completed()
            return True
        return False

    
    def _check_completed(self):
        """
        Function used by other functions to check if sudoku has already been completed
        """
        if len(self.get_all_empty_cells()) == 0:
            self.is_solved = True
            self.end_time = time.time()
            self.total_time = self.end_time - self.start_time
