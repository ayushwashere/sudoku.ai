'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

class Sudoku:
    # We store an array of arrays in row-major format where empty space are stored as None

    def __init__(self, base_str):
        def parse_input_string(base_str):
            data = base_str.split(';')
            grid = [[char if char != '-' else None for char in row] for row in data]
            return grid

        self.grid = parse_input_string(base_str)
        self.is_solved = False

    
    def display(self):
        # TODO: create an interactive GUI for this
        for i, row in enumerate(self.grid):
            row = ["_" if cell is None else cell for cell in row]
            print_str = ''.join(row[:3]) + " | " + ''.join(row[3:6]) + " | " + ''.join(row[6:])
            print(print_str)
            if i in [2, 5]:
                print("-"*15)

    
    def get_block(self, block):
        block_data = []
        rows = self.grid[3*(block//3):3*(block//3)+3]
        for row in rows:
            cdata = row[3*(block%3):3*(block%3)+3]
            block_data += cdata
        return block_data
        
    
    def get_row(self, row):
        return self.grid[row]

    
    def get_column(self, column):
        return [row[column] for row in self.grid]

    
    def get_all_empty_cells(self):
        empty = []
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                if cell is None:
                    empty.append((row_index, col_index))
        return empty
    
    
    def set_value(self, row, column, value):
        block = self.calculate_block_from_indices(row, column)
        row_data = self.get_row(row)
        column_data = self.get_column(column)
        block_data = self.get_block(block)

        if value not in row_data and value not in column_data or value not in block_data:
            self.grid[row][column] = value
            self.check_solved()
            return True
        else:
            return False


    def calculate_block_from_indices(self, row, column):
        return 3 * (row // 3) + (column // 3)


    def check_solved(self):
        foundNone = False
        for row in self.grid:
            if None in row:
                foundNone = True
                break
        if not foundNone:
            self.is_solved = True
        
