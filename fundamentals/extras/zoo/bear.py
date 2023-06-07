import animal

class Bear(animal.Animal):

    def __init__(self, name: str, age: int = 500, health: int = 700, happiness: int = 800, toothpaste_tubes_eaten: int = 0) -> None:
        self.name: str = name
        self.age: int = age
        self.health: int = health
        self.happiness: int = happiness
        self.toothpaste_tubes_eaten: int = toothpaste_tubes_eaten
        
        super().__init__(
            name = self.name,
            age = age,
            health = health,
            happiness = happiness
        )
        

    def eat_my_food_at_the_campsite_while_I_am_hiking(self):
        original_health = self.health
        self.health += 100
        original_happiness = self.happiness
        self.happiness += 200
        original_toothpaste_tubes_eaten = self.toothpaste_tubes_eaten
        self.toothpaste_tubes_eaten += 1
        
        print(
            str(self.name) + "'s original health went from " +\
                str(original_health) + "to " + str(self.health) + ".\n" + \
                    "Happiness went from " + str(original_happiness) + \
                        " to " + str(self.happiness) + ".\n" + \
                            "Hope you brushed your teeth already because " + \
                                str(self.name) + " has eaten another toothpaste tube!\n" + \
                                    "Toothpaste tubes eaten went from " + str(original_toothpaste_tubes_eaten) + \
                                        str(self.toothpaste_tubes_eaten) + "\n"
            )
        return self
