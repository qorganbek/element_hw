import Engine as eng, Driver as drv
class Car(object):
    def __init__(self, carClass: str, engine: eng.Engine, driver: drv.Driver, brand: str):
        self.carClass = carClass
        self.engine = engine
        self.driver = driver
        self.brand = brand

    def start(self):
        print("Let's go! ")

    def stop(self):
        print("Stop! ")

    def turnRight(self):
        print("Right turn! ")

    def turnLeft(self):
        print("Left turn! ")

    def __str__(self):
        return f"Hello I'm {self.driver.full_name} and my car driving experience is {self.driver.experience}, This car brand is {self.brand}, car engine is {self.engine.company} have {self.engine.power}hp "




