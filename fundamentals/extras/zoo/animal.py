import lion

class Animal:

    def __init__(self, name: str, age: int, health: int, happiness: int) -> None:
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        self.info = f"\nHere is {self.name}'s information:\nName: {self.name}\nAge: {self.age}\nHealth: {self.health}\nHappiness: {self.happiness}\n"
        print(self.info)
        return self

    def feed(self):
        original_health = self.health
        self.health += 10
        original_happiness = self.happiness
        self.happiness += 10

        print(f"{self.name} was extremely hungry and you fed him meat.")
        print(f"{self.name}'s health increased from {original_health} to {self.health}.")
        print(f"{self.name}'s happiness increased from {original_happiness} to {self.happiness}.\n")

        return self

if __name__ == "__main__":
    
    animal = Animal(
        name = "Charlie",
        age = 100,
        health = 35,
        happiness = 3
    ).display_info()

    lion = lion.Lion(
        name = "Mufasa"
    ).display_info()

