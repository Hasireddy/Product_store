from products import Product

class Store:
    def __init__(self, products):
        self.products = products


    def add_product(self, product_to_add):
        self.products.append(product_to_add)
        return self.products


    def remove_product(self,product_remove):
            if product_remove in self.products:
                self.products.remove(product_remove)


    def total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self):
        return self.products


    def order(self, shopping_list):
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price




bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

best_buy = Store([bose, mac])

print("All Products: ", best_buy.get_all_products())


lenova = Product("Lenovo Asus",600, 200)

total =  best_buy.add_product(lenova)

print("After adding new product:")

for product in total:
    product.show()

product_remove  = best_buy.remove_product(mac)
print("After removing product:")
print("All Products: ", best_buy.get_all_products())

purchase = best_buy.order([(bose, 5),(lenova, 10)])
print(f"The order cost: {purchase} dollars")

