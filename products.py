
class Product:
    def __init__(self, name, price, quantity):
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if price <0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def get_quantity(self):
        print(f"The quantity is {self.quantity}")


    def set_quantity(self):
        if self.quantity == 0:
            del self

    def is_active(self):
        if self.active == True:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def buy(self,quantity):
        return self.quantity * self.price




try:
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.show()
    bose.get_quantity()
except Exception as e:
    print(e)

"""try:
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    mac.show()
except Exception as e:
    print(e)


try:
    product = Product("",600, 200)
    product.show()
except Exception as e:
    print(e)"""




