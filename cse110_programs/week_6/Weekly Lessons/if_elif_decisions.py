#
#Patrick T. Edgett

# name = input("What is your name? ").lower()

# # If you do not specify your comparisons, it will assume the string "sam" exists, and is therefore true
# # This means the OR statement below is always true.
# # if name == "joe" and "sam":

# if name == "joe" and name == "sam":
#     print(f"Hello {name}")
# else:
#     print("Sorry, wrong name")


# # Order of operations:
# # Parenthesis, AND, OR

# name = input("What is your first name? ").lower()
# last = input("What is your last name? ").lower()

# # You can also do the above using nested if statements
# if (name == "joe" or name == "sam") and last == 'bond':
#     print(f"Hello {name} {last}.")
# else:
#     print("Sorry, wrong name.")

# if name == "joe" or name == "sam":
#     if last == "bond":
#         print(f"Hello {name} {last}.")
#     else:
#         print("Sorry, wrong name.")
# else:
#     print("Sorry, wrong name.")


# Running Calculator
temp = float(input("What is the temperature outside? "))
windy = "Not Checked"

if temp > 50:
    windy = input("Is it windy outside? (yes or no): ").lower()
    if windy == "yes" and temp > 70:
        print("You should probably go running, sorry.")
    elif windy != "yes" and windy != "no":
        # A \ at the very end of a print line, it'll tell python that the next line is a part of the current line
        # Ensure that the following line is backed all the way to the left to avoid including the tabbed spaces in the output.
        print(f"I don't understand what '{windy}' is,\
please use one of the options provided within the parenthesis.")
    else:
        print("DON'T DO IT!!!")
else:
    print("DON'T DO IT!!!")

print(f"Temp: {temp} and windy: {windy}.")