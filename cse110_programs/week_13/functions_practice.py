# This program was created to practice creating functions
# This program uses the functions .upper() and .lower() inside the functions
# Patrick T. Edgett
# 12/9/24

def display_regular(statement = "No Bitches?"):
    print(statement)

def display_uppercase(statement = "Tragic"):
    print(statement.upper())

def display_lowercase(statement = "....I'm sorry, please come back."):
    print(statement.lower())

user = input("Give me a message: ")

display_regular(user)
display_uppercase(user)
display_lowercase(user)