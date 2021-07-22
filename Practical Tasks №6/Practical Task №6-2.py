class Road():
    def __init__(self, lenght, width, weight, thickness):
        self._lenght = lenght
        self._width = width
        self._weight = weight
        self._thickness = thickness


    def calculetion(self):
        print(f'Масса асфальта, толщиной {self._thickness} см. равна {self._lenght * self._width * self._weight * self._thickness } кг')

road = Road(5000, 20, 25, 5)
road.calculetion()

