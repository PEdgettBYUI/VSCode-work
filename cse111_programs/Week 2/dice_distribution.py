import random

tallies = []
numberOfThrows = 10000000

def prepare_tally_list():
    # function to initialize the list for counting dice rolls
    for number in range(13):
        tallies.append(0)

def throw_lots_of_dice():
    # roll dice many times and track the results
    print(f"Now rolling {numberOfThrows} pairs of dice.")
    for i in range(numberOfThrows):
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        total = die_1 + die_2
        tallies[total] += 1

def display_results():
    # display a graph of the tallies

    # range passes the VALUE in the array to i, 
    # and len() passes the INDEX VALUE to i.
    for i in range(2, len(tallies)):
        print(f"Number of {i} Rolled - {tallies[i]}")
    

# The main program starts here. It just calls those three functions:
prepare_tally_list()
throw_lots_of_dice()
display_results()

print(tallies)