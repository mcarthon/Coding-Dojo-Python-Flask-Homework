import animal

class Lion(animal.Animal):

    def __init__(self, name: str, age: int = 1000, health: int = 1000, happiness: int = 1000, confidence: int = 1000) -> None:
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.confidence = confidence
        
        super().__init__(
            name = self.name,
            age = self.age,
            health = self.health,
            happiness = self.happiness
        )

    def display_info(self):
        # self.info = f"\nHere is {self.name}'s lion information:" +\
        #     f"\nName: {self.name}\n"+\
        #         f"Age: {self.age}\nHealth: {self.health}\nHappiness: {self.happiness}\n" +\
        self.info = str(super().display_info()) + "Confidence: " + str(self.confidence) + "\n"
        print(self.info)
        # print(dir(super()))
        return self

if __name__ == "__main__":
    pass