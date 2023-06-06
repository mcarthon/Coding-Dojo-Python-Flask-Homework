from product import Product

class Store:

    all_products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, new_product):
        Store.all_products.append(new_product)
        print(f"{new_product.name} has been added to {self.name}'s inventory.")
        nice_product_list = [product.name for product in Store.all_products]
        print(f"Here is {self.name}'s current inventory:\n{nice_product_list}\n")
        return self

    def sell_product(self, id):
        answer = input(f"Are you sure you want to sell {Store.all_products[id].name}? \n(y/n) or (yes/no):\n")
        if "y" in answer.lower():
            Store.all_products.pop(id)
            print(f"{Store.all_products[id].name} has been sold.")
        nice_product_list = [product.name for product in Store.all_products]
        print(f"Here is {self.name}'s current inventory:\n{nice_product_list}\n")
        return self

    def inflation(self, percent_increase):
        for product in Store.all_products:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        clearance_products = list(filter(lambda product: product.category == category))
        for product in clearance_products:
            product.update_price(percent_discount, False)

if __name__ == "__main__":
    pass