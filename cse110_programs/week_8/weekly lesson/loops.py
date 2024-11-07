# Week 8 - Loops Part 2

nums = [1, 2, 3, 4]

for num in nums:
    print(num)

i = 0
while i < 4:
    print(nums[i])
    i += 1

word = "word"
# letter is a local variable defined within the for loop only
for letter in word:
    print(letter)

# #GOTCHA - Do not do
# # Python will cache the value before it loops, meaning that word is defined as "d" by the time the loop ends
# # by using the same variable name you redefine the original variable as it loops
# for word in word:
#     print(word)

if "o" in word:
    print(f"O is in the word '{word}'")
else:
    print(f"O is NOT in the word '{word}'")

if "z" in word:
    print(f"Z is in the word '{word}'")
else:
    print(f"z is NOT in the word'{word}'")

# Range does not include the stop value while iterating, it will stop before that value
# i.e. it will print 4 but not 5.
for num in range(1, 5):

## The below will count until the stop point

# for num in range(5):

## The third variable in range tells the program how many steps to iterate by, in this case every second letter after the start point
# for num in range(1, 5, 2)
    print(num)
# # Range is an object that knows how to loop through numbers in a for loop
# # Range is not a list in and of itself, and will print as a string if used like this
# print(range(1,5))


# Range
word = "dictionary"
print(f"The word '{word}' has {len(word)} letters.")
for i in range(len(word)):
    letter = word[i]
    print(f"Letter at {i} is {letter}")