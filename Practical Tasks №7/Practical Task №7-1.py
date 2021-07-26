class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))

a = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
b = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]

matrix_a = Matrix(a)
matrix_b = Matrix(b)

print(matrix_a, '\n')
print(matrix_b, '\n')
print(matrix_a + matrix_b)