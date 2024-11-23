# Week 9 - Lists
# Patrick T. Edgett
# 11/11/24


# # Example one
# # "List" is a protected keyword, don't name a variable list
# # list() is a way to initialize a list, but stick to []
# # movies = list()
# movies = [
#     "Iron Man", 
#     "Batman", 
#     "Hunk", 
#     "The Legend of Lonk"
# ]
# # Not good, try and avoid just printing the list
# print(movies)

# # Adds item to end of list
# movies.append("Star Wars")

# # "insert" adds an item to a specific index of the list
# movies.insert(2, "Scrooge")

# # You can update a list like a variable, using specific indexes
# movies[1] = "Incredible Bulk"

# # # Get more movies from the user
# # from_user = ""
# # while from_user != "quit":
# #     from_user = input("What movie would you like to add (QUIT to stop adding movies)? ")
# #     if from_user != "quit":
# #         movies.append(from_user)

# # Acceptable but not good.
# print("Movies:")
# # for movie in movies:
# #     print(f" - {movie}")

# # NOTE: "i" = index number
# print(f"{len(movies)} Movies: ")
# for i in range(len(movies)):
#     movie = movies[i]
#     print(f"{i + 1} - {movie}")


# # DEMO of .pop() 
# # Pop takes in an index and removes it, if left blank it takes "-1" or the end of the list
# # Pop also returns the removed item, which can be placed into a variable
# print(movies)
# print("removing... ")
# # .pop() is the recommended method of removing an item from the list
# removed = movies.pop(1)
# # .remove()
# # Does not return a variable, only removes the first occurance of a given exact value
# # Can cause more errors, not recommended
# movies.remove("Star Wars")
# print(movies)





# Below is an example of a menu made of lists
print()
menu = [
    '1 - Drink',
    '2 - Entree',
    '3 - Side',
    '4 - Quit'
]

drinks = ["Water", "Root Beer", "Pepsi", "Coke", "Guarana"]
entrees = ["Hamburger", "Cheeseburger", "Big Mac", "Whopper"]

selection = ""
order_items = []
prices = []

while selection != "4":
    print("What would you like to order? ")
    for item in menu:
        print(item)
    selection = input("Enter 1-4: ")

    if selection == '1':
        print("Drink options are: ")
        for drink in drinks:
            print(drink)
        drink_selection = input("Which drink would you like to order? ")
        if drink_selection.title() in drinks:
            order_items.append(drink_selection)
            drink_price = float(input("How much does it cost? "))
            prices.append(drink_price)
        else:
            print("Invalid.")

    if selection == '2':
        print("entree options are: ")
        for entree in entrees:
            print(entree)
        entree_selection = input("Which entree would you like to order? ")
        if entree_selection.title() in entrees:
            order_items.append(entree_selection)
            entree_price = float(input("How much does it cost? "))
            prices.append(entree_price)
        else:
            print("Invalid.")

print(order_items)
print(prices)

print(f"\nOrder finalized. You selected: ")
# for item in order_items:
for i in range(len(order_items)):
    item = order_items[i]
    price = prices[i]
    print(f" - {item.title()} ${price:.2f}")

# Using enumerate
sum = 0
for i, item in enumerate(order_items):
    # item = order_items[i]
    price = prices[i]
    sum += price
    print(f" - {item.title()} ${price:.2f}")
print(f"Total of ${sum:.2f}")

