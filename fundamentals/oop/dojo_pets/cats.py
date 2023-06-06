from pets import Pets

class Cat(Pets):

    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

    def catch_mouse(self):
        print(f"{self.name} just saw a mouse on the loose!")
        print(f"{self.name} just caught the mouse.")
        self.energy -= 50
        print(f"{self.name}'s energy went from {self.energy + 50} to {self.energy}.")
        self.health += 50
        print(f"{self.name}'s health went from {self.health - 50} to {self.health}.")
