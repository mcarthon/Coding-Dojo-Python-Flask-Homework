from pets import Pets
from cats import Cat

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
        return self

    def feed(self):
        print(f"{self.pet.name} the {self.pet.type} is now being fed.")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.pet.name} is a bit of a stinky poo at the moment")
        print(f"{self.first_name} is now giving {self.pet.name} a bath")
        self.pet.noise()
        print(f"Since {self.pet.name} was a good boy, {self.first_name} gave {self.pet.name} some {self.treats}")
        return self

if __name__ == "__main__":
    pet = Pets(
        name = "Bard",
        type = "dog",
        tricks = "catch frisby",
        health = 200,
        energy = 180
    )
    
    owner = Ninja(
        first_name = "John",
        last_name = "Wick",
        treats = "scooby snacks",
        pet_food = "danimals",
        pet = pet 
    )

    cat = Cat(
        name = "Garfield",
        type = "cat",
        tricks = "scratch",
        health = 340,
        energy = 100
    )

    cat_owner = Ninja(
        first_name = "Patrick",
        last_name = "Star",
        treats = "credit cards",
        pet_food = "rain drops",
        pet = cat 
    )

    owner.feed().walk().bathe()
    print()
    cat_owner.feed().walk().bathe()