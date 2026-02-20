
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


try:
    product1 = Product("MacBook Air M2", 1450, 100)
    product1.show()
except Exception as e:
    print(e)

try:
    product2 = Product("apple air 4", -1600, 200)
    product2.show()
except Exception as e:
    print(e)


try:
    product3 = Product("",600, 200)
    product3.show()
except Exception as e:
    print(e)




