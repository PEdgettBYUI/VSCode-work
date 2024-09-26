# Patrick Edgett
# Formatting Strings Checkpoint Assignment
import time

first_name = input("What is your first name? ")
first_name = first_name.title()
last_name = input("What is your last name? ")
last_name = last_name.title()

# Easter Egg referencing an internet joke
if first_name == "Bames" and last_name == "Nond":
    print(f"\n'{last_name}?': {last_name},  {first_name}.")

    print("M: Pleased to-- what did you say?")
    time.sleep(3)
    print(f"'{last_name}?': Bond's Name the James Name.")
    time.sleep(3)
    print("M: Are you okay?")
    time.sleep(3)
    print(f"'{last_name}?': {first_name} {last_name}'s having a stronk, call a bondulance.\n")
else:
    # Regular Response
    print(f"\n{last_name}: The name's {last_name}, {first_name} {last_name}.")
    time.sleep(2)
    print(f"M: Nice to meet you Mr.{last_name}, shall we go to work? ")
    time.sleep(2)
    print("[Action Movie Noises happen off screen]\n")
    time.sleep(2)
