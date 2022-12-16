import Car, Driver, Engine

class Lorry(Car.Car):
    def __init__(self, carClass, engine, driver, brand, carrying):
        super().__init__(carClass, engine, driver, brand)
        self.carrying = carrying

    def __str__(self):
        return f"This lorry mark is {self.brand}  body load capacity = {self.carrying} "

