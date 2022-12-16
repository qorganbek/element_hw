class Engine(object):

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self):
        return f'This engine is manufactured by {self.company} and its power is {self.power}hp '
