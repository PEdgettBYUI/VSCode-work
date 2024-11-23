# Shopping cart Version 2
# This program allows the user to create and edit a shopping cart dynamically
# Patrick T. Edgett
# 11/13/24

import time

menu_top = ["1. Add Item", "2. View Cart", "3. Remove Item", "4. Compute Total", "5. Quit"]

selection = 0
cart = []
prices = []
item = ""
price = 0.00
total = 0.00

while selection != 5:
    print("Please select one of the following: ")
    # Top Menu
    for each in menu_top:
        print(f"{each}")
    selection = int(input("Enter an aciton using the number: "))
    if selection == 1:
        item = input("What item would you like to add? ")
        cart.append(item)

        price = float(input(f"What is the price of '{item}'? "))
        print(f"'{item}' has been added to the cart.\n")
        prices.append(price)
        print()
    elif selection == 2:
        for i, each in enumerate(cart):
            print(f" {i + 1}. {each} ${prices[i]:.2f}")
        time.sleep(2)
        print()
    elif selection == 3:
        choice = int(input("Which item would you like to remove? "))
        remove_cart = cart.pop(choice-1)
        remove_price = prices.pop(choice-1)
        print(f"Item \"{remove_cart} - ${remove_price}\" removed.")
        time.sleep(2)
        print()
    elif selection == 4:
        total = 0.00    # Clears total to sum updated lists
        for i, item in enumerate(cart):
            total += prices[i]
        print(f"Your Running Total is: ${total:.2f}")
        time.sleep(2)
        print()


print("Shopping concluded. Thank you. Goodbye.")
print()