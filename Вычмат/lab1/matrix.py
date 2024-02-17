class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def get_value(self, row, col):
        return self.data[row][col]

    def swap_rows(self, row1, row2):
        self.data[row1], self.data[row2] = self.data[row2], self.data[row1]

    def scale_row(self, row, scale):
        self.data[row] = [value * scale for value in self.data[row]]

    def add_scaled_row(self, row1, row2, scale):
        self.data[row2] = [a + scale * b for a, b in zip(self.data[row2], self.data[row1])]

    def gauss_elimination(self):
        for pivot_row in range(min(self.rows, self.cols)):
            # Make the diagonal element 1
            pivot_element = self.get_value(pivot_row, pivot_row)
            if pivot_element == 0:
                # If the pivot element is zero, find a non-zero row to swap
                for i in range(pivot_row + 1, self.rows):
                    if self.get_value(i, pivot_row) != 0:
                        self.swap_rows(pivot_row, i)
                        pivot_element = self.get_value(pivot_row, pivot_row)
                        break

            self.scale_row(pivot_row, 1 / pivot_element)

            # Eliminate below the pivot
            for i in range(pivot_row + 1, self.rows):
                factor = -self.get_value(i, pivot_row)
                self.add_scaled_row(pivot_row, i, factor)


# Example usage:
matrix = Matrix(3, 4)
matrix.set_value(0, 0, 2)
matrix.set_value(0, 1, -1)
matrix.set_value(0, 2, 1)
matrix.set_value(0, 3, 8)
matrix.set_value(1, 0, -3)
matrix.set_value(1, 1, 1)
matrix.set_value(1, 2, 2)
matrix.set_value(1, 3, -11)
matrix.set_value(2, 0, -2)
matrix.set_value(2, 1, 1)
matrix.set_value(2, 2, 2)
matrix.set_value(2, 3, -3)

print("Original Matrix:")
print(matrix)
print("\nMatrix after Gauss Elimination:")
matrix.gauss_elimination()
print(matrix)