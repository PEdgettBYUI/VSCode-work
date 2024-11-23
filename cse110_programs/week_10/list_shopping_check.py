# Shopping list program
# Create and edit a list of items at indexes the user can input

shopping_list = []
user_input = ""
new_item = ""
repeat = ""

print("Please enter the items of the shopping list (type: quit to finish): ")

while user_input != "Quit":
    user_input = input("Item: ").title()
    if user_input != "Quit":
        shopping_list.append(user_input)
print()

# shopping_list without indexes
print("The Shopping List Is:")
for i in shopping_list:
    print(i)

# Prints shopping_list with indexes,
# Allows user to edit the list repeatedly
while repeat != "N":
    repeat = ""
    print()
    print("The Shopping list with indexes:")
    for i in range(len(shopping_list)):
        item = shopping_list[i]
        print(f"{i}. {item}")


    change = int(input("Which item would you like to change an item? "))
    new_item = input("What is the new item? ").title()
    
    shopping_list[change] = new_item
    print(f"{new_item} added.")
    print()

    print("The Shopping list with indexes:")
    for i in range(len(shopping_list)):
        item = shopping_list[i]
        print(f"{i}. {item}")
    while repeat != "Y" and repeat != "N":
        repeat = input("Would you like to change another item(Y/N)? ").title()
        print()
        if repeat != "Y" and repeat != "N":
            print("INVALID. Please use (Y/N).")
        elif repeat == "N":
            print("The Final Shopping list with indexes:")
            for i in range(len(shopping_list)):
                item = shopping_list[i]
                print(f"{i}. {item}")