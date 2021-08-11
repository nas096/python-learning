class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.strip().split("\n")
        # Turn the matrix string into real matrix in form of lists of list.
        self.matrix = [row.split(" ") for row in self.matrix]
        self.matrix = [list(map(int, x)) for x in self.matrix]

    def row(self, index):
        try:
            return self.matrix[index-1]
        except IndexError:
            print("Out of range! Please try again.")

    def column(self, index):
        # Return the result
        try:
            return [number[index-1] for number in self.matrix]
        except IndexError:
            print("Out of range! Please try again.")
