# Variables and Expressions

# Ways to convert a number to an int during input
# NOTE: input() will default to converting to astring.
num1 = input("Give me a number: ")
num1 = int(num1)
# More elegant way of ensuring input is converted to an float
num2 = float(input("Give me another number: "))

# Any operation that includes a float, or results in a float will convert integers to floats for the output
# NOTE: Shift + Alt + up/down will copy the currently highlighted line of code
print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# more advanced operations
# ** - Exponent
print(f"\n{num1} ** {num2} = {num1 ** num2}")
# % - Modulus; divide and return the remainder, remainer bein in R# form, not decimal.
# use case example: can return current day of the week (in an integer from 0-6) by taking the (current date) % (first date of the week)
print(f"{num1} % {num2} = {num1 % num2}\n")

# // - Divide and drop remainer, simulates intger-division results in strongly typed languages (i.e. C++)
num2 = int(num2)
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1//num2}")