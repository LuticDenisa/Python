class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth."

class Bird(Animal):
    def __init__(self, name, habitat, flight_speed):
        super().__init__(name, habitat)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at a speed of {self.flight_speed} units."

class Fish(Animal):
    def __init__(self, name, habitat, swim_speed):
        super().__init__(name, habitat)
        self.swim_speed = swim_speed

    def swim(self):
        return f"{self.name} is swimming at a speed of {self.swim_speed} units."


lion = Mammal("Lion", "Grasslands", "Golden")
print(lion.give_birth())

colibri = Bird("Eagle", "Mountains", 40)
print(colibri.fly())

shark = Fish("Shark", "Oceans",  20)
print(shark.swim())
