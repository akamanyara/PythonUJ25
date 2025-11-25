import random

class ZeroOne:
    def __iter__(self):
        self.state = 0
        return self

    def __next__(self):
        v = self.state
        self.state = 1 - self.state
        return v


class RandomNESW:
    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(("N", "E", "S", "W"))


class WeekdayCycle:
    def __iter__(self):
        self.day = 0
        return self

    def __next__(self):
        v = self.day
        self.day = (self.day + 1) % 7
        return v