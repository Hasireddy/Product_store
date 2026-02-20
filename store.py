class Store:
    def __init__(self, product):
        self.product = product
        products = []

    def add_product(self, product):
        self.products.append(product)
        return self.products


    def remove_product(self,product_remove):
        for product in self.products:
            if product == product_remove:
                self.products.remove(product)

    def total_quantity(self):
        pass

    def get_all_products(self):
        pass

    def order(self, shopping_list):
        pass



