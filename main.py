import sys
from products import Product
from store import Store


product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]

best_buy = Store(product_list)


def list_products():
    total_products = best_buy.get_all_products()

    for i, product in enumerate(total_products):
        print(f"{i+1}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")



def total_amount():
    total_amount = best_buy.total_quantity()
    print(f"Total of {total_amount} items in store")


def order():
    list_products()
    order_list = []

    print("When you want to finish order , enter empty text.")

    while True:
        order_input = input("Which product # do you want? ")
        if order_input == "":
            break

        amount = input("What amount do you want? ")
        if amount == "":
            break

        product_index = int(order_input) - 1
        quantity = int(amount)

        product = best_buy.products[product_index]

        order_list.append((product, quantity))
        print("Product added to the list!")


    make_order = best_buy.order(order_list)
    print(f"Order made! Total payment: ${int(make_order)}")


def exit_program():
    print("Bye")
    sys.exit()



my_choice = {
              1: list_products,
              2: total_amount,
              3: order,
              4: exit_program
            }



def start(best_buy):
    print("""
             Store Menu
             -------------
             1. List all products in store
             2. Show total amount in store
             3. Make an order
             4. Quit""")




def main():
    while True:
        start(best_buy)
        user_input = int(input("Please choose a number: "))

        if user_input not in my_choice:
            break
        result = my_choice[user_input]
        result()




if __name__ == "__main__":
    main()
