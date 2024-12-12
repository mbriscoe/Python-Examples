import os

os.system("clear")


class Bird:
    """
    Bird class
    """

    # CLASS ATTRIBUTES ARE VARIABLES DECLARED OUTSIDE THE CONSTRUCTOR
    numBirds = 0

    def __init__(self, kind, call):
        # properties
        # INSTANCE ATTRIBUTES DECLARED INSIDE CONSTRUCTOR
        self.kind = kind
        self.call = call
        Bird.numBirds += 1
        print(f"Number of birds: {Bird.numBirds}")

    # behaviour
    def description(self):
        """
        describe the bird
        """
        return f"{self.kind} goes {self.call}."


# class Big_bird(Bird):
#     beak_color = "yellow"

#     def __init__(self, kind, call, wingspan):
#         self.wingspan = wingspan
#         super().__init__(kind, call)

#     def description(self):
#         """
#         describe the Big_bird
#         """

#         return f"{self.kind} goes {self.call} and has a wing span of {self.wingspan} feet. It's beak color is {self.beak_color}."


owl = Bird("Owl", "Twit Twoo")

crow = Bird("Crow", "Caw")

# eagle = Big_bird("Eagle", "Screech", 25)
# eagle.color = "White"
# eagle.beak_color = "red"

print(owl.description())
print(crow.description())
# print(eagle.description())
