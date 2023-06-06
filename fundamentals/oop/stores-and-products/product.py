import math 
import random

class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = random.randint(10**6, 10**7)

    def update_price(self, percent_change, is_increased):
        temp = self.price
        if is_increased == True:
            self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)
        self.price = round(self.price, 2)
        print()
        print(f"The price of the {self.name} went from {temp} to {self.price}.")
        print()
        return self

    def print_info(self):
        print()
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Category: {self.category}")
        print(f"Price: {round(self.price, 2)}")
        print()
        return self