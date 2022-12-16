import Car, Driver, Engine

class SportCar(Car.Car):
    def __init__(self, carClass: str, engine: Engine, driver: Driver, brand: str, speed: int):
        super().__init__(carClass, engine, driver, brand)
        self.speed = speed


    def __str__(self):
        return f'This Super Car mark {self.brand}, power of engine equal to {self.speed}'

