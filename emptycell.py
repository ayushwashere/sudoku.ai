'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

class EmptyCell:
    def __init__(self, row, column):
        self.is_completed = False
        self.row = row
        self.column = column
        self.values = [str(num) for num in range(1, 10)]

    def get_possible_values(self):
        return self.values

    def set_new_values(self, values):
        self.values = values
        if len(self.values) == 1:
            self.is_completed = True

    def get_identifiers(self):
        return self.row, self.column

    def __str__(self):
        return "({}, {}) ".format(self.row, self.column) + ', '.join(self.values)
