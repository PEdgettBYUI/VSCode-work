# This program iterates through the letters in a string.
# Patrick T. Edgett
# 11/6/24

s_word = "commitment"
fav_letter = str(input("What is your favorite letter? ")).lower()

for i in s_word:
    if i == fav_letter:
        print("_", end="")
    else:
        print(i.lower(), end="")

print("")
# i = index position, letter = contents of index
for i, letter in enumerate(s_word):
    print(f"The letter {letter} is at position {i}")