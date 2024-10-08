# The Word Game (definitely not Mad-Libs, we swears it)
# Patrick T. Edgett
# Function: Play a game of Mad-Libs with the user.

print("Welcome to the Word Game! \nBefore we begin, we need you to tell us some things:")

adjective = input("Give us an adjective: ")
animal = input("Give us an animal: ")
verb = input("Give us a verb: ")
verb_1 = input("Give us another verb: ")
verb_2 = input("One Last Verb, if you please: ")
exclaimation = input("Give us something to SHOUT!: ")
feeling = input("Give us a feeling to use: ")
smell = input("Give us a smell to use: ")
mean_name = input("Tell us something mean to call someone: ")
uplifting_noun = input("Give us a noun thats uplifting: ")
mcguffin = input("Give us something cool to use: ")
win_quote = input("Give us a great one-liner to use: ")

# The Story Begins
print("And so, your story begins...\n")

print(f"\n The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. ")
print(f'"{exclaimation}" I yelled. But all I could think to do was {verb_1} over and over.')
print(f"Miraculously, that caused it to stop, but not before it tried to {verb_2} right in front of my family.")
print(f'I felt {feeling}. "What kind of {animal} does something as awful like {verb_2} in someone elses home! You {mean_name} thing, you!')
print(f"With a new sense of {uplifting_noun}, I {verb_1} to my {mcguffin} that I keep for emergencies, and I rushed at the {animal}.")
print(f'When I got to it, it made a terrible noise, and suddenly there was the smell of {smell}. "{exclaimation}!" I cried again.')
print(f'Then the {mean_name}, {adjective}, {smell}-smelling {animal} was gone. I raised my {mcguffin} over my head and shouted: "{win_quote}!"')
print(f'And my never saw that {feeling}, {smell}-smelling {animal} ever again.\n')
print("...And so our tale ends. Don't forget to tip your OS on the way out!")
