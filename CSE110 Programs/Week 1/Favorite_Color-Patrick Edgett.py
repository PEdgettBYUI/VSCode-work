#Created Patrick Edgett
#for CSE110 - FA24
import time

#The program below simulates an example of an active dialog with the user using delays to simulate gaps in "speech"
name = input("Hello, what's your name? ")
print(f"It's nice to meet you {name.title()}, I'm Python.")
time.sleep(3)
print("Now that we've met, I'd like to know your favorite color, ")
time.sleep(2)
color = input(f"Can you tell me? ")
time.sleep(1)
print(f"That sounds like a neat color. I think {color.lower()} goes very well with a name like '{name.title()}'.")
time.sleep(4)
print("\nWell, it's sure been nice having this little chat, I hope you have a nice day!")