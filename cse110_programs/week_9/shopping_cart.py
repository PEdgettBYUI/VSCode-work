# This program allows the user to create and edit a shopping cart dynamically
# Patrick T. Edgett
# 11/13/24

import time

menu_top = ["1. Add Item", "2. View Cart", "3. Remove Item", "4. Compute Total", "5. Quit"]

selection = 0
cart = []
item = ""
price = 0.00

while selection != 5:
    print("Please select one of the following: ")
    # Top Menu
    for each in menu_top:
        print(f"{each}")
    selection = int(input("Enter an aciton using the number: "))
    if selection == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        # price = input(f"What is the price of '{item}'? ")
        # print(f"'{item}' has been added to the cart.\n")
        print()
    elif selection == 2:
        for each in cart:
            print(f" - {each}")
        time.sleep(2)
        print()
    elif selection == 3:
        print("Removing Items to be added in a later update")
    elif selection == 4:
        print("Computing total to be added in a later update")

print("Shopping concluded. Thank you. Goodbye.")