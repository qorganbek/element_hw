class Driver(object):

    def __init__(self, full_name: str, experience: int):
        self.full_name = full_name
        self.experience = experience

    def __str__(self):
        return f"Hello I'm {self.full_name}, my driving experience {self.experience} years "


