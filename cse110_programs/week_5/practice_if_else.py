# Prepare 05: Practicing if/else statements
# Patrick Edgett
# Function: Compare input values and output the appropriate response

first_num = input("What is the first number? ")
second_num = input("What is the second number? ")
my_animal = "cat"

# If number 1 is greater
if first_num > second_num:
    print("\nThe first number is greater.")
else:
    print("The first number is not greater.")
# If they are equal
if first_num == second_num:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

#If number 2 is greater
if first_num < second_num:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

# User's favorite animal
user_animal = input("\nWhat is your favorite animal? ").lower()
if user_animal == my_animal:
    print("That's my favorite animal too!")
else:
    print("That's not my favorite.")