# # Defining a function with a arbitrary number of arguements
# # *args - The * will allow you to do this
# # Turning the arguements into a list

# def say_howdy(*names):
#     print(f"Howdy ", end="")
#     for name in names:
#         print(name, "", end="")
#         print()

# say_howdy("ladies", "gentlemen", "boys", "girls", "assorted pets")

# print("Howdy," "ladies", "and", "gentleman")
# # Printing a function without the () will result in "<built-in function ___>" being printed
# # print(print, sum, round, say_howdy)



# ChatGPT Slop-work
# Does basic Math
def doArithmetic(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:  # Prevent division by zero
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

# Example usage:
print(doArithmetic(10, 5, 'add'))       # Output: 15
print(doArithmetic(10, 5, 'subtract'))  # Output: 5
print(doArithmetic(10, 5, 'multiply'))  # Output: 50
print(doArithmetic(10, 5, 'divide'))    # Output: 2.0
print(doArithmetic(10, 0, 'divide'))    # Output: Error: Division by zero is not allowed.
print(doArithmetic(10, 5, 'modulus'))   # Output: Error: Invalid operation.


# Filter - filter based on a condition
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
# Equivalent to:
def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))

# Sorted - Custom Sorting
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  # Output: ['apple', 'cherry', 'banana']  (sorted by length)



# lambda examples
# ex1 - Ternary Op/Conditional Expressions
# Returns "Even" if the number is even, otherwise "Odd"
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_or_odd(10))  # Output: Even
print(even_or_odd(7))   # Output: Odd
# Equivalent to:
def even_or_odd(x):
    return "Even" if x % 2 == 0 else "Odd"


# ex2 -Sorting a list of dictionaries
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 85}
]

# Sort students by score (ascending order)
sorted_students = sorted(students, key=lambda student: student['score'])

print(sorted_students)

#ex3 - Nested Lambdas
# Function that returns a lambda function
def power(exponent):
    return lambda base: base ** exponent

square = power(2)  # Returns a lambda function that squares a number
cube = power(3)    # Returns a lambda function that cubes a number

print(square(4))  # Output: 16 (4^2)
print(cube(3))    # Output: 27 (3^3)


