import abc

class Clothes(abc.ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abc.abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5

class Costume(Clothes):

    @property
    def consumption(self):
        return round(2 * self.param + 0.3) / 100

coat = Coat(int(input('Введите размер пальто: ')))
costume = Costume(int(input('Введите рост: ')))

print(f'Расход ткани для пальто составляет {coat.consumption}')
print(f'Расход ткани для костюма составляет {costume.consumption}')
print(f'Общий расход ткани равен {coat + costume}')