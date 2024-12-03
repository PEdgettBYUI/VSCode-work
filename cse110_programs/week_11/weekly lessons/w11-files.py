# Lesson about files and how we can take data from them.
# This also uses a file named data.csv for demonstration purposes

# burgers
# strip
# fries

# # foods = "french fries, burgers, shakes"
# # print(foods)

# # .split() looks for a seperator chosen and
# # if left blank it will split it based on spaces
# parts = foods.split(" , ")
# # print(parts)
# for food in parts:
#     # .strip() only works on a string
#     food_clean = food.strip()
#     print(food_clean)

#Open a file
# Sometimes subdirectories have an issue where it will still search for the file in the main directory of your vscode "source"
# This error can be corrected in settings "python > terminal: execute in file dir"
# file = open("data.csv")

# NOTE: Using the with open() line will close the file automatically as the program closes
# This avoids needing to type file.close() at line 41
with open("data.csv") as file:

# NOTE: If we read the first line the program will begin it's loop from line 2, ignoring the issue of the header line not being an integer
    header = file.readline()
# # next(file) # same function as readline() but a bit more confusing


# NOTE: Files will input the hidden characters that mean things like /n unless accounted for
    for line in file:
        parts = line.split(",")
        food = parts[0].strip()
        quantity = int(parts[1].strip())
        print(f"{food} - {quantity}")
# # NOTE: ALWAYS close the file after opening it to avoid memory leaks
# file.close()