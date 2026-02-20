
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


product = Product("MacBook Air M2", 1450, 100)
product.show()

