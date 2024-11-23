# Multiple Lists
# This program takes 2 lists, one containing an account name and another containing a balance
# The goal is to keep the listss sync'd so that each account index is tied to a parallel balance index
# Patrick T. Edgett
# 11/20/24

account = []
balance = []

u_input = ""

while u_input != "quit":
    u_input = input("What is the name of the account? ").lower()
    if u_input != "quit":
        account.append(u_input)

        num = float(input("What is the balance? "))
        balance.append(num)
print()

print("Account Information")
for i, item in enumerate(account):
    print(f"{i}. {item} - ${balance[i]:.2f}")
print()

sum = 0
for i in balance:
    sum += i
print(f"Total: ${sum:.2f}")

avg = sum /len(balance)
print(f"Average: ${avg:.2f}")

# Determines the account with the greatest balance
largest = 0
index = 0
for i, item in enumerate(balance):
    if item > largest:
        largest = item
        index = i
print(f"The Highest balance is: {account[index]} - {balance[index]:.2f}")

# # Ask the user if they want to change the balance
repeat = ""
while repeat != "n":
    repeat = input("Would you like to update an account (y/n)? ").lower()
    if repeat == "y":
        u_input = int(input("Which account index do you want to update? "))
        num = float(input("What is the new balance? "))
        balance[u_input] = num

        print("Account Information:")
        for i, item in enumerate(account):
            print(f"{i}. {item} - ${balance[i]:.2f}")
        print()
print()
print("Account Information:")
for i, item in enumerate(account):
    print(f"{i}. {item} - ${balance[i]:.2f}")
print()