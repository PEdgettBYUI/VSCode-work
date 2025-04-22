# map(func, iterable, ...)
    # Ex 1
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]

    # Practice Revision
wordage = ["TOBJOHN", "I kNoW yOu ArE", "Crembopulous Micheals"]
casing = map(lambda x: x.capitalize(), wordage)

print(wordage)
print(list(casing))


words = input("Write for me: ")
text_go = lambda x: print(x)
text_go(words)

# filter(func, iterable)
    # Ex 1
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

    # Practice Revision



# Make a thing that adds a index to an iterable, then zip it with a array of integers

animals = ['bird', 'camel', 'dog', 'elephant', 'fox']
assign_number = list(map(lambda x: f"{x[0]}: {x[1]}", enumerate(animals)))
print(assign_number)