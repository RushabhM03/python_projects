class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("WE are out of stock")
        else:
            print("We do not keep that product")

    def print_purchases(self):
        print("The summary of your purchase is:")
        for i in range(8):
            print()
        for i in self.purchases:
            print(i.name)


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:

    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):

        print("Inventory stock :")
        for i in range(5):
            print()

        for i, j in self.inventory.items():
            print(i.name + '\t:\t' + str(j))
        print()


c1 = Customer('joe', 'joe@gmail.com')
applewatch = Product('Apple watch', 299)
Mac = Product('Mac', 1900)

inv = Inventory()
inv.add_product(applewatch, 100)
inv.add_product(Mac, 160)


inv.print_inventory()
c1.purchase(inv, applewatch)
c1.purchase(inv, Mac)
inv.print_inventory()
c1.print_purchases()
