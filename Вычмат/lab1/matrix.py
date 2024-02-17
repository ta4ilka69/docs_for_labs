class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.n = len(rows)
        self.m = len(rows[0])
        if any(len(row) != self.m for row in rows):
            raise ValueError("All rows must have the same length")
        if self.n != self.m - 1:
            raise ValueError("Matrix must be (n x n+1)")
        if any(not isinstance(x, (int, float)) for x in sum(rows, [])):
            raise ValueError("All elements must be numbers")
        self.triangular_rows = None
        self.permutations = -1

    def triangular_matrix(self):
        perm = 0
        result = [row[:] for row in self.rows]
        for i in range(self.n):
            if result[i][i] == 0:
                for j in range(i + 1, self.n):
                    if result[j][i] != 0:
                        result[i], result[j] = result[j], result[i]
                        perm+=1
                        break
                else:
                    return -1
            for j in range(i + 1, self.n):
                factor = result[j][i] / result[i][i]
                for k in range(self.n + 1):
                    result[j][k] -= factor * result[i][k]
        self.triangular_rows = result
        self.permutations = perm
        return perm

    def determinant(self):
        if self.permutations >=0:
            result = 1
            for i in range(self.n):
                result *= self.triangular_rows[i][i]
            return result * (-1)**self.permutations
        else:
            return 0
    
    def solve_system_gauss(self):
        if self.determinant() == 0:
            raise ValueError()
        solutions = [0] * self.n
        for i in range(self.n - 1, -1, -1):
            solution = self.triangular_rows[i][self.n]
            for j in range(i + 1, self.n):
                solution -= self.triangular_rows[i][j] * solutions[j]
            solutions[i] = solution / self.triangular_rows[i][i]
        return solutions
    def __str__(self):
        col_widths = [max(len(str(elem)) for elem in col) for col in zip(*self.rows)]
        matrix_str = "\nMatrix:\n\n"
        for row in self.rows:
            for i, elem in enumerate(row):
                matrix_str += str(elem).ljust(col_widths[i]) + " | "
            matrix_str = matrix_str[:-3]
            matrix_str += "\n" + "-" * (sum(col_widths) + 3 * (len(row) - 1)) + "\n"
        return matrix_str[:-1]
    
    
    @staticmethod
    def residual_vector(data, solution):
        if len(data) != len(solution):
            raise ValueError("Data and solution lengths do not match")
        residual = []
        for i in range(len(data)):
            eq_residual = data[i][-1]
            for j in range(len(solution)):
                eq_residual -= data[i][j] * solution[j]
            residual.append(eq_residual)
        return residual
    

    def print_triangular(self):
        col_widths = [max(len(str(elem)) for elem in col) for col in zip(*self.triangular_rows)]
        matrix_str = "\nMatrix triangular:\n\n"
        for row in self.triangular_rows:
            for i, elem in enumerate(row):
                matrix_str += str(elem).ljust(col_widths[i]) + " | "
            matrix_str = matrix_str[:-3]
            matrix_str += "\n" + "-" * (sum(col_widths) + 3 * (len(row) - 1)) + "\n"
        return matrix_str[:-1]