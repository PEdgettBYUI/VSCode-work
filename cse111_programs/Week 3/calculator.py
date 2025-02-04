def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multipy(a, b):
    return a * b

def divide(a, b):
    return a / b

def exponent(a, b):
    # pow(a, b) - Does the same thing as below
    return a ** b

def factorial(n):
# Reminder: Factorial is any positive number > 0 times every number before it to 1.
    if n < 0:
        return "Error! Factorials of negative numbers do not exist."
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def calculator():

    while True:
        print("Calculator 5-BILLION")
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent")
        print("6. Factorial")
        print("7. Exit")

        choice = int(input("Type the number of the operation you wish to perform: "))

        if choice == 7:
            print("Have a nice day!")
            break

        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multipy(num1, num2)}")
        elif choice == 4:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == 5:
            print(f"{num1} ^ {num2} = {exponent(num1, num2)}")
        
        elif choice == 6:
            num_f = int(input("Enter a whole number: "))
            print(f"{num_f}! = {factorial(num_f)}")
        
calculator()