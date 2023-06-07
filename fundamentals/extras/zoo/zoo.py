import lion, animal, bear, dinosaur

class Zoo(animal.Animal):

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.animals: list = []

    def add_lion(self, name: str):
        self.animals.append(lion.Lion(name))
        return self

    def add_bear(self, name: str):
        self.animals.append(bear.Bear(name))
        return self

    def add_dinosaur(self, name: str):
        self.animals.append(dinosaur.Dinosaur(name))
        return self

    def print_all_info(self):
        for animal in self.animals:
            animal.display_info()
        return self

if __name__ == "__main__":
    zoo_name = "Muh Zoo"
    zoo = Zoo(name = zoo_name)

    zoo.add_bear("Bearstein Bear")
    zoo.add_dinosaur("Coach Dino")
    zoo.add_lion("Mufasa")

    zoo.print_all_info()
