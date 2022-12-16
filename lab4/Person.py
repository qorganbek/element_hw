import Driver as drv

class Person(drv.Driver):
    def __init__(self, full_name: str, experience: int, age: int):
        super().__init__(full_name, experience)
        self.age = age


    def __str__(self):
        return f"Hello guys my name is {self.full_name} and i'm {self.age} years old! "
