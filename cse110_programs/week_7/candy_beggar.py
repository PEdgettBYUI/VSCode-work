# This program simulates a child asking for a piece of candy
# It also demonstrates a way to check if a number is positive or not
# Patrick T. Edgett
# 10/28/24

number = int(input("Please type a positive number: "))
reply = ""

while number < 0:
    print("That number is negative, try again.")
    number = int(input("Please type a positive number: "))
print("Loop concluded.\n")

while reply != "yes":
    reply = input("May I have a piece of candy? ").lower()
print("Thank you.")

