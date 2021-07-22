class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Stationery - {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Pen - {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Pencil - {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Handle - {self.title}')

stationery = Stationery('Stationery')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()