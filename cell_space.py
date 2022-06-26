'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

class CellSpace:
    def __init__(self, row, column, block):
        self.isCompleted = False
        self.row = row
        self.column = column
        self.block = block
        self.values = [str(num) for num in range(1, 10)]

    def get_possible_values(self):
        return self.values

    def set_new_values(self, values):
        self.values = values

    def is_completed(self):
        return self.isCompleted

    def set_completed(self):
        self.isCompleted = True

    def get_identifiers(self):
        return self.row, self.column, self.block

    def __str__(self):
        return "({}, {})".format(self.row, self.column) + ', '.join(self.values)
