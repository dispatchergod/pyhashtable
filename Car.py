import hashlib


class Car(object):
    weight = 0
    color = ""

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __getitem__(self, item):
        return self.weight, self.color

    def __hash__(self):
        return 123

    def get_car(self):
        print(self.weight)
        print(self.color, "\n")
