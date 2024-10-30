# Guess my number game
# Play a game with the computer where you try to guess the number it's randomly selected
# Patrick T. Edgett

import random
    
replay = "yes"

while replay == "yes":
    user_num = 0
    magic_num = random.randint(1, 10)
    user_num = int(input("What is your guess number? "))
    count = 1
    while magic_num != user_num:
        if user_num > magic_num:
            print("Lower.")
            user_num = int(input("What is the magic number? "))
        elif user_num < magic_num:
            print("Higher.")
            user_num = int(input("What is the magic number? "))
        count = count + 1

    print("You Guessed It!")
    print(f"You guessed {count} times!")
    replay = str(input("Type \"yes\" to replay, or press ENTER to close ")).lower()
print("Thanks for playing!")