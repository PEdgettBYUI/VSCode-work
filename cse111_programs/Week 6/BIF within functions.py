# What are the ten most commonly used Python BIFs that have functions as parameters? Provide 3 examples for each
# ChatGPT said:
# Built-in functions (BIFs) in Python that take other functions as parameters are commonly used for functional programming. 
# Here are ten of the most commonly used ones, along with three examples for each:

# 1. map()
    # Applies a function to each item in an iterable and returns a map object (which can be converted to a list, tuple, etc.).


# Example function
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16]

# Example function
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))  # ['HELLO', 'WORLD', 'PYTHON']

# Example function
lengths = list(map(len, ["apple", "banana", "cherry"]))  # [5, 6, 6]



# 2. filter()
    # Filters elements in an iterable based on a function that returns True or False.
    # Examples:

# Example function
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4, 6]

# Example function
words = ["apple", "banana", "kiwi"]
long_words = list(filter(lambda word: len(word) > 5, words))  # ['banana']

# Example function
positives = list(filter(lambda x: x > 0, [-3, -2, 0, 1, 4]))  # [1, 4]


# 3. reduce() (from functools)
    # Applies a function cumulatively to the items in an iterable.
    # Examples:

# Example function
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  # 24

# Example function
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)  # "Hello World Python"

# Example function
max_num = reduce(lambda a, b: a if a > b else b, [3, 7, 2, 8, 5])  # 8



# 4. sorted()
    # Sorts an iterable based on a key function.
    # Examples:

# Example function
numbers = [5, 2, 8, 1]
sorted_numbers = sorted(numbers, key=lambda x: -x)  # [8, 5, 2, 1]

# Example function
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)  # ['apple', 'banana', 'cherry']

# Example function
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
sorted_people = sorted(people, key=lambda p: p["age"])  

# [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]


# 5. any()
    # Returns True if any element in the iterable meets the condition.
    # Examples:

# Example function
numbers = [0, 1, 2, 3]
result = any(map(lambda x: x > 2, numbers))  # True

# Example function
words = ["", "", "hello"]
result = any(map(bool, words))  # True

# Example function
conditions = [False, False, True]
result = any(conditions)  # True



# 6. all()
    # Returns True if all elements in the iterable meet the condition.
    # Examples:

# Example function
numbers = [2, 4, 6]
result = all(map(lambda x: x % 2 == 0, numbers))  # True

# Example function
words = ["apple", "banana", "cherry"]
result = all(map(lambda w: len(w) > 4, words))  # True

# Example function
flags = [True, True, False]
result = all(flags)  # False



# 7. max()
    # Returns the maximum element, optionally based on a key function.
    # Examples:

# Example function
numbers = [5, 2, 8, 1]
max_number = max(numbers, key=lambda x: -x)  # 1

# Example function
words = ["banana", "apple", "cherry"]
longest_word = max(words, key=len)  # 'banana'

# Example function
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
oldest_person = max(people, key=lambda p: p["age"])  # {'name': 'Alice', 'age': 25}



# 8. min()
    # Returns the minimum element, optionally based on a key function.
    # Examples:

# Example function
numbers = [5, 2, 8, 1]
min_number = min(numbers, key=lambda x: -x)  # 8

# Example function
words = ["banana", "apple", "cherry"]
shortest_word = min(words, key=len)  # 'apple'

# Example function
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
youngest_person = min(people, key=lambda p: p["age"])  # {'name': 'Bob', 'age': 20}



# 9. zip()
    # Combines multiple iterables element-wise, optionally processing with a function.
    # Examples:

# Example function
nums = [1, 2, 3]
squares = [1, 4, 9]
result = list(map(lambda x: x[0] + x[1], zip(nums, squares)))  # [2, 6, 12]

# Example function
names = ["Alice", "Bob"]
scores = [85, 92]
result = dict(zip(names, scores))  # {'Alice': 85, 'Bob': 92}

# Example function
list1 = [1, 2, 3]
list2 = [4, 5, 6]
multiplied = list(map(lambda x: x[0] * x[1], zip(list1, list2)))  # [4, 10, 18]



# 10. enumerate()
    # Adds an index to an iterable.
    # Examples:

# Example function
words = ["apple", "banana", "cherry"]
result = list(map(lambda x: f"{x[0]}: {x[1]}", enumerate(words)))  
# ['0: apple', '1: banana', '2: cherry']

# Example function
letters = ["a", "b", "c"]
indexed = list(enumerate(letters, start=1))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Example function
numbers = [10, 20, 30]
indexed_numbers = dict(enumerate(numbers))  # {0: 10, 1: 20, 2: 30}
# These built-in functions make Python powerful for functional programming by allowing higher-order function usage in various scenarios. 🚀