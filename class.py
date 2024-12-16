import os

os.system("clear")


class Bird:
    # CLASS ATTRIBUTE
    numBirds = 0

    # CONSTRUCTOR
    def __init__(self, kind, call):
        # INSTANCE VARTIABLES/PROPERTIES
        self.kind = kind
        self.call = call
        Bird.numBirds += 1
        print(f"Number of birds = {Bird.numBirds}")

    # BEHAVIOUR
    def describe(self):
        return f"{self.kind} goes {self.call}."


class Big_Bird(Bird):

    def __init__(self, kind, call, wingspan):
        self.wingspan = wingspan
        super().__init__(kind, call)

    def describe(self):
        return f"{self.kind} goes {self.call}, and has a wingspan of {self.wingspan} feet!"


class Really_big_Bird(Big_Bird):
    def __init__(self, kind, call, wingspan, age):
        self.age = age
        super().__init__(kind, call, wingspan)

    def describe(self):
        return f"{self.kind} goes {self.call}, and has a wingspan of {self.wingspan} feet! It is {self.age} years old and massive!"


owl = Bird("Owl", "Twit Twoo")
crow = Bird("Crow", "Caw")

eagle = Big_Bird("Eagle", "Screech", 25)

vulture = Really_big_Bird("Vulture", "Sqawk", 60, 200)

print(vulture.describe())
