# Wordo - Not Wordle, I swears it.
# This program is a word guessing game, you guess the word until you get it right
# Patrick T. Edgett
# 10/30/24

secret = "geronimo"
guess = ""
count = 0

print("Let's Play Wordo.\n")


while guess != secret:
    # Iterate Guess Counter
    count = count + 1
    # Player guess input
    guess = str(input("What is your guess? ")).lower()
    if guess != secret:
        # Checks to make sure the number of letters in guess are the same as the number of letters in secret
        if len(secret) != len(guess):
            print(f"Yout Guess is not {len(secret)} letters long. Try again\n")
        # Compares the letters in one string to another
        else:
            print("Your hint is: ", end="")
            for i in range(len(guess)):
                #If guess-letter @ i-index == secret-letter @ i-index
                if guess[i] == secret[i]:
                    print(guess[i].capitalize(), end=" ")
                #If guess-letter @ i-index is IN secret
                elif guess[i] in secret:
                    print(guess[i].lower(), end=" ")
                #If guess-letter @ i-index is NOT in secret
                else:
                    print("_", end=" ")
            print()
print("\nYou guessed the secret word! Amazing!")
print(f"It took you just {count} guesses.\n")