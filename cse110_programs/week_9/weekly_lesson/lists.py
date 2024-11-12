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
# Not good, try and avoid just printing the list
# print(movies)

# # Acceptable but not good.
# print("Movies:")
# for movie in movies:
#     print(f" - {movie}")

# movies.append("Star Wars")

# # Get more movies from the user
# from_user = ""
# while from_user != "quit":
#     from_user = input("What movie would you like to add (QUIT to stop adding movies)? ")
#     if from_user != "quit":
#         movies.append(from_user)

# Below is an example of a menu made of lists
print()
menu = [
    '1 - Drink',
    '2 - Entree',
    '3 - Side',
    '4 - Quit'
]

drinks = [
    "Water",
    "Root Beer",
    "Pepsi",
    "Coke",
    "Guarana"
    ]

entrees = [
    "Hamburger",
    "Cheeseburger",
    "Big Mac",
    "Whopper"
]

selection = ""
order_items = []

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
        else:
            print("Invalid.")

    if selection == '2':
        print("entree options are: ")
        for entree in entrees:
            print(entree)
        entree_selection = input("Which entree would you like to order? ")
        if entree_selection.title() in entrees:
            order_items.append(entree_selection)
        else:
            print("Invalid.")

print(f"\nOrder finalized. You selected: ")
for item in order_items:
    print(f" - {item.title()}")
print()
