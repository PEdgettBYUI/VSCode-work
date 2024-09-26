# Variables and IO

### Will work, but will give a "None" output because print stores no data,
### and the lack of data is passed to "{name}"
# name = input(print('What is your name? '))
# print(name)

first_name = "James"
last_name = "Bond"

# Other methods of printing variables
# not preferred
print(first_name + ' '+ last_name)
# hot garbo
# automatically puts a space between the items, may introduce unwanted spaces
print(first_name,last_name)
# formatting
print('{} {}'.format(first_name, last_name))
print('{1} {0}'.format(last_name, first_name))

fullname = f"{last_name}, {first_name}"
print(fullname)

# preferred method
print(f"{first_name} {last_name}")

# example of why "hot garbo", ln14, is bad
# potentially useful in debugging, but nothing more
print(last_name, ',', first_name)

# input testing multiple inputs at once
# RESULT: treats output as one variable
test = f"{input("one: ")}, {input("two: ")}"
print(test)

#methods on strings
words = "testo Petroleum"
print(words.upper())
print(words.title())
print(words.capitalize())
print(words.lower())

print(words.count('t'))
print(words.upper().count('T'))

# Flier Example
event = input("What is the event? ")
when = input("when will the event take place? ")

print(f'{event.title()}')
print(f'{when.capitalize()}')