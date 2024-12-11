# # The purpose of this program is to demonstrate functions and how they work
# # Patrick T. Edgett
# # 12/9/24

# # define your function
# # def lets you make a function, give it a name and within the parenthesis you put a parameter the function takes in
# # Return lets you feed back a single output
# # GOOD DESIGN OF A FUNCTION: A function does only ONE thing
# # GOOD DESIGN NOTE: DO NOT use the same variable names for function parameters as regular variables
#     # This makes 2 DIFFERENT functions named the same thing, making debugging much, much harder
# # NOTE: While you CAN make it print instead of return, that makes the function useful for ONLY ONE use-case
# def compute_tithe(amt):
#     tithe = amt * .10
#     return tithe

# # If you want a function that displays the tithe AFTER computing it, this is a better way
# # You can give each parameter a default value by setting the variable = to something
# def display_tithe(amt=10):
#     print(compute_tithe(amt))

# # You can also hard-code an input to a function
# print(compute_tithe(100))
# print(compute_tithe(500))
# print(compute_tithe(576))

# # You can feed a variable into the function; this allows the user to define what goes into "compute_tithe()"
# x = 1000
# print(compute_tithe(x))


# Multiple parameter functions DEMO
# The code used here to demo a function was from the week_6/"Weekly Lessons"/if_elif_decisions.py
# Running Calculator

# Bool NOTE: In boolean, True and False are case sensitive in Python
def ask_yes_no(prompt, affirmative = 'y', negative = 'n'):
    answer = ''
    while answer != affirmative.lower() and answer != negative.lower():
        answer = input(f'{prompt.strip()} ({affirmative.upper()}/{negative.upper()}) ').lower()
        if answer == affirmative.lower():
            return True
        elif answer == negative.lower():
            return False
        else:
            print(f"{answer} is not a valid answer.")


temp = float(input("What is the temperature outside? "))
windy = "Not Checked"

if temp > 50:
    # windy = input("Is it windy outside? (yes or no): ").lower()
    windy = ask_yes_no("Is it windy outside ")
    if windy and temp > 70:
        print("You should probably go running, sorry.")
#     elif windy != "yes" and windy != "no":
#         # A \ at the very end of a print line, it'll tell python that the next line is a part of the current line
#         # Ensure that the following line is backed all the way to the left to avoid including the tabbed spaces in the output.
#         print(f"I don't understand what '{windy}' is,\
# please use one of the options provided within the parenthesis.")
    else:
        print("DON'T DO IT!!!")
else:
    print("DON'T DO IT!!!")

print(f"Temp: {temp} and windy: {windy}.")
