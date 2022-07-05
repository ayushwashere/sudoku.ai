'''
    Author: Ayush Kumar
    GitHub: @ayushwashere
'''

class EmptyCell:
    def __init__(self, row, column):
        """
        Creates an EmptyCell object with specified position values (row, column)
        Initially set possible values as a list [1...9]
        """
        self.is_completed = False
        self.row = row
        self.column = column
        self.values = [str(num) for num in range(1, 10)]


    def get_possible_values(self):
        """
        Returns list of possible values for the EmptyCell
        """
        return self.values


    def set_new_values(self, values):
        """
        Set a new list of values as the new list of possible values
        If the new values list contains a single element, the final value of the cell has been determined and we raise a is_completed flag
        """
        self.values = values
        if len(self.values) == 1:
            self.is_completed = True


    def get_identifiers(self):
        """
        Returns the row, column positional identifiers of EmptyCell
        """
        return self.row, self.column


    def __str__(self):
        return "({}, {}) ".format(self.row, self.column) + ', '.join(self.values)
