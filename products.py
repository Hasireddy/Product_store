
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
        return f"The quantity is {self.quantity}"


    def set_quantity(self,quantity):
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()
        else:
            self.activate()

        return self.quantity


    def is_active(self):
       return self.active


    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def buy(self,quantity):
        if not self.active:
            print("Product is not active")

        if quantity <= 0:
            print("Quantity cannot be negative")

        if quantity > self.quantity:
            return f"The quantity currently in stock is {self.quantity} and less then the quantity to buy {quantity}"

        total_price = quantity  * self.price
        self.quantity = self.quantity - quantity

        if self.quantity == 0:
            self.deactivate()

        return float(total_price)


try:
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.show()
    print(bose.get_quantity())

    print(bose.is_active())
    print(bose.buy(500))

    print(bose.is_active())
    print(bose.buy(200))

    print(bose.set_quantity(1000))
    print(bose.is_active())
    bose.show()


except Exception as e:
    print(e)

"""try:
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    mac.show()
    print(mac.get_quantity())
    print(mac.buy(200))
except Exception as e:
    print(e)


try:
    product = Product("",600, 200)
    product.show()
except Exception as e:
    print(e)"""




