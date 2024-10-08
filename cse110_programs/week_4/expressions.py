# ########################################
# # Week 4 - Solving Problems using Variables & Expressions (part 2)
# ########################################

# # prints input x number of times
# text = "-"
# print(text * 6)

# # Round will 
# cost = 54587435983.56786
# # cost = round(cost, 2)


# # Floats being formatted defaults to exponent notation
# # f changes the notation to floating-point notation
# # formatting at the print statement doesn't change the value stored
# print(f"${cost:.2f}")
# # order does matter when using multiple formats
# # if you want both , and . you need to put them in that order
# print(f"{cost:,.2f}")
# print(cost)


# # String modifier
# hair = input("What is your hair color? ")
# eye = input("What is your eye color? ")
# month = input("When were you hired? ")
# title = input("Job Title: ")

# # < & > act like "left-align"/"right-align" in a word document
# # Sets a soft character limit, and places spaces to the left(>) or to the right(<) of the string input
# print(f"Hair: {hair.capitalize():<15} eye:{eye.capitalize()}")
# print(f'Hired: {month.capitalize():<14} Job:{title.capitalize()}')

# # .ljust() & .rjust() example - Can only be used on strings
# # Effectively the same result as the other
# print(f"Hair: {hair.capitalize().ljust()} eye:{eye.capitalize()}")
# print(f'Hired: {month.capitalize().rjust(14))} Job:{title.capitalize()}')



# Calculating commissions
# NOTE: You cannot put a % or other character after the string in an input function
sale = float(input('What was the total sale price? $'))
rate = float(input('What is the commission rate (%)'))

print(f"With a sale of {sale:,.2f} you earned ${rate * sale:,.2f}!")
