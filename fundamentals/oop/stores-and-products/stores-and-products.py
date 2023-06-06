from store import Store
from product import Product

if __name__ == "__main__":
    irish_spring = Product(
        name = "Irish Spring Soap",
        price = 5.99,
        category = "soap"
    )
    
    dove = Product(
        name = "Dove Soap",
        price = 4.99,
        category = "soap"
    )

    aquafina = Product(
        name = "Aquafina Bottle Water",
        price = 1.99,
        category = "water"
    )

    dasani = Product(
        name = "Dasani Bottle Water",
        price = 2.99,
        category = "water"
    )

    walmark = Store(
        name = "WalMark's Convenient Store",
    )

    walmark.add_product(irish_spring).add_product(dove).add_product(aquafina).add_product(dasani)
    walmark.inflation(0.15)
    walmark.sell_product(2)
    print(walmark.all_products[0].print_info())
    print(walmark.all_products[1].print_info())
    print([x.name for x in walmark.all_products])
