# Shopping Cart using **kwargs

def shopping_cart(**products):
    total = 0

    print("Shopping Cart Details:")

    for item, price in products.items():
        print(item, ": ₹", price)
        total = total + price

    print("Total Amount: ₹", total)

# Function call
shopping_cart(apple=15, orange=12, mango=10)