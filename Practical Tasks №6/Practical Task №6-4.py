class Car():
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} - GO')

    def stop(self):
        print(f'{self.name} - STOP')

    def turn(self, direction):
        print(f"{self.name} - TURN {'LEFT' if direction == 0 else 'RIGHT'}")

    def show_speed(self):
        print(f'{self.name} - SPEED - {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f"{self.name} - SPEED - {self.speed} - !!!" if self.speed > 60 else f'{self.name} - SPEED - {self.speed}')

class SportCar(Car):
    def show_speed(self):
        print(f"{self.name} - SPEED - {self.speed} - !!!" if self.speed > 360 else f'{self.name} - SPEED - {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        print(f"{self.name} - SPEED - {self.speed} - !!!" if self.speed > 40 else f'{self.name} - SPEED - {self.speed}')

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('Skoda', 'White', 120, True)
town_car = TownCar('VW', 'Blue', 90, False)
sport_car = SportCar('Ferrari', 'Red', 300, False)
work_car = WorkCar('Ford', 'Green', 100, False)

police_car.go()
police_car.stop()
police_car.turn(0)
police_car.turn(1)
police_car.show_speed()
town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()