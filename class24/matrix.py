class Matrix:
    # Define properties here
    row = 0
    column = 0
    matrix = [[0 * column] * row]

    # Define constructor here
    def __init__(self, *args):
        if len(args) >= 2:
            self.row = args[0]
            self.column = args[1]
            self.matrix = [[0 for column in range(self.column)]
                           for row in range(self.row)]

    def input(self):
        for i in range(self.row):
            row = input().split()
            for j in range(self.column):
                self.matrix[i][j] = int(row[j])

    # Complete the function

    def add(self, x: "Matrix") -> "Matrix":
        result = Matrix(self.row,self.column)
        for i in range(self.row):
            for j in range(self.column):
                result.matrix[i][j] = self.matrix[i][j] + x.matrix[i][j]
        return result

    # Complete the function


    def subtract(self, x: "Matrix") -> "Matrix":
        result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result.matrix[i][j] = self.matrix[i][j] - x.matrix[i][j]
        return result

    # Complete the function


    def transpose(self) -> "Matrix":

        result = Matrix(self.column, self.row)

        for i in range(self.row):
            for j in range(self.column):
                result.matrix[j][i] = self.matrix[i][j]
        return result

    def print(self):
        # Complete the functionc
        for i in range(self.row):
            for j in range(self.column):
                print(self.matrix[i][j], end=" ")
            print()


a = Matrix(4, 1)
a.input()
a.print()
