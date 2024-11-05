# Wordo - Not Wordle, I swears it.
# This program is a word guessing game, you guess the word until you get it right
# Patrick T. Edgett
# 10/30/24

secret = "geronimo"
guess = ""
count = 0

print("Let's Play Wordo.\n The Secret Word is 8 Letters long\n")
while guess != secret:
    guess = str(input("What is your guess? ")).lower()
    count = count + 1
print("You Achieved the guess! What competence!")
print(f"It took you just {count} guesses.\n")