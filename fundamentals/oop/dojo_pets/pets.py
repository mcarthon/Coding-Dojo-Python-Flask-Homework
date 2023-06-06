class Pets:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print(f"{self.name} the {self.type} is now sleeping")
        self.energy += 25
        print(f"{self.name}'s energy has been increased from {self.energy - 5} to {self.energy}\n\n")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy has been increased from {self.energy - 5} to {self.energy}")
        print(f"{self.name}'s health has been increased from {self.health - 5} to {self.health}\n\n")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name}'s health has been increased from {self.health - 5} to {self.health}\n\n")
        return self

    def noise(self):
        print(f"{self.type} noises ensue")
        return self