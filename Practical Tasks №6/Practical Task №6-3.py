class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name, self.surname}\n {self.position}')

    def get_total_income(self):
        print(f'{sum(self._incom.values())}')

worker = Position('Alexey', 'Ivanov', 'CFO', 150000, 38000)
worker.get_full_name()
worker.get_total_income()