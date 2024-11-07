# This is a stretch goal in iterate_through_strings.py
# The purpose is to highlight letters at a certain position in a string
# Patrick T. Edgett
#11/6/24

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
number = int(input("Please enter a number: "))
run = "yes"
while run == "yes": 
    for i, letter in enumerate(quote):
        if (i) % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")
    run = input("Would you like to enter another number?(yes/no) ").lower()