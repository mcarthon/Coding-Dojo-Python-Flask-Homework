from pets import Pets

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

        self.pet = Pets(
            name = self.pet.name,
            type = self.pet.type,
            tricks = self.pet.tricks,
            health = self.pet.health,
            energy = self.pet.energy
        )

    def walk(self):
        print(f"{self.pet.name} the {self.pet.type} is going for a walk.")
        self.pet.play()

    def feed(self):
        print(f"{self.pet.name} the {self.pet.type} is now being fed.")
        self.pet.eat()

    def bathe(self):
        print(f"{self.pet.name} is a bit of a stinky poo at the moment")
        print(f"{self.first_name} is now giving {self.pet.name} a bath")
        self.pet.noise()
        print(f"Since {self.pet.name} was a good boy, {self.first_name} gave {self.pet.name} some {self.treats}")

if __name__ == "__main__":
    pass