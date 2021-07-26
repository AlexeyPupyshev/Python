class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Результат операции сложения равен {self.quantity + other.quantity}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Результат операции вычитания равен {self.quantity - other.quantity}'
        else:
            return f'Операция вычитания невозможна'

    def __mul__(self, other):
        return f'Результат операции умножения равен {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Результат операции деления (округленного до целого числа) равен {round(self.quantity // other.quantity)}'

    def make_order(self, cells_in_rows):
        return '\n'.join(['*' * cells_in_rows for _ in range(int(self.quantity / cells_in_rows))]) + '\n' + '*' * (int(self.quantity % cells_in_rows))

cell_1 = Cell(126)
cell_2 = Cell(120)
cell_3 = Cell(320)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 - cell_3)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_1.make_order(35))
