import animal

class Dinosaur(animal.Animal):

    def __init__(self, name: str, age: int = 4000, health: int = 4000, happiness: int = 3000, flying: bool = False) -> None:
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.flying = flying

        super().__init__(
            name = self.name,
            age = self.age,
            health = self.health,
            happiness = self.happiness
        )

    def fly_and_destroy(self):
        print("FEEL MY POWER\nHEAR ME ROAR")
        print(f"When someone challenges {self.name}, he becomes angry and activates flying.\n")
        self.flying = True
        self.happiness = 0
        return self

    