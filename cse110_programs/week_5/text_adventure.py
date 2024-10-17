# A Text Adventure based on my own writings as a DM
# Patrick Edgett
#10/16/24

# Setting the scene
print("\n\nYou find yourself alone, with an aching head, at the Flailing Jaguar Bar in Rhuin.")
print("You wager that you had lost a hard-fought drinking game and find an irritated barmaid standing over you on the floor.")
choice = input("\"Al'ight mista, you've been enjoying the cheapest bed in the 'ouse long 'nough, are you gonna PAY or SCRAM?\" ").upper()

# Story
# Summary: Depending on if you answer PAY or SCRAM (or WORK) to the barmaid will begin if your adventure is either:
# PAY) A countryside ride defending a carriage of civilians from Goblins
# SCRAM) A series of misunderstandings that result in you on the wrong side of the law
# (WORK)) A brief little "Adventure" of working the bar to pay your debts before catching a carriage out of town
# else) Getting knocked out, and in a drawn out, hopefully humerous series of mishaps, manage to fall out the second floor balcony of the inn and plunge into the sewers and never be seen again.

# Any choice that does not have a correct answer will then lead the player to a comedic interpretation of how they somehow, no matter how likely, managed to die from not making the right choice.

# Carriage Ride Path
if choice == "PAY":
    print("\nYou stand up and root through your coin purse before finding that it's empty. You gesture towards the barmaid and she says,") 
    print("\"F'oi'ne then. At least you seemed earnest about it.\"Off with ya then.\" she says waving you away. \"")
    print("A little dejected, but ultimately thankful of her kindness for you, you begin to wander towards the town gates to the West to try and hitch a carriage ride back home.")
    print("Arriving just in time, you see a carriage finishing loading it's passengers and cargo into the back of the hooded wagon, above you see a sign that reads:.")
    choice = input("'Ride: 5 Gilder OR work.' Knowing you haven't a penny to your name, you must decide if you're going to WALK or WORK").upper()
    if choice == "WORK":
        print("You explain that you're seeking passage out of town, and that you're willing to work for your spot on the carriage.")
        print("\"Well then, 'Lookout,'\" he says before pausing. Reaching underneath his seat he pulls out a leather sheath, and tosses it to you.")
        print("\"Seems to me that it'll fall on you to keep us safe if we see any nasties. Climb on back. Your seat's right on the step.\"")
        print("Sitting down on the tiny step, you coil your left arm around the post on the lip of the wagon, and check the shortsword you've been given.")
        print("It's old, rusted, and stained. And frankly, you're pretty sure it's dull. Attached to the side is a whetstone that you use to try and sharpen the sword in vain.")
    elif choice == "WALK":
        print("Deciding that you'd prefer not to exhaust yourself to earn a spot on the cart, you decide to hoof it on foot.")
        # FIGHT or RUN from some goblins
        # FIGHT: Attempt to fight goblins using RNG
            # Win: You survive, beaten and bruised. A different
        # RUN: Die falling into a ravine

# Criminal Misunderstandings Path
elif choice == "SCRAM":
    print("\nYou hear her shouting in the distance about how much of a good-for-nothing lout you are, and that you aren't welcome back again.")
    print("Turning around, you try and catch a glimpse of the red on her face before you crash to the ground after running head-long into a thick necked guard.")
    print("\"Oi, ya bum, watch where yer goin'.\" He gravels as he turns around, pointing his spear in your general direction.")
    print("Looking past you on the ground, he sees the angry barmaid yelling profanities towards you before turning in a huff and slamming shut the inn's doors behind her."0
    print("Looking back at the guard you see he's got a different idea about why she was so upset.")
    print("\"So,\" he starts with a cruel smirk before slowly continuing, \"robbin' da inn, eh? An' 'fore noon, no less.\"")
    print("Wagging his index finger like you were a naughty child caught with your hand in the cookie jar. \"V'ry naughty, then.\"")
    choice = input("Will you PROTEST the guards accusations, or GO ALONG quietly with him?").upper()
#     if choice == "PROTEST":
#         print("You swear to the guard you haven't a penny on you, and that proves you couldn't have robbed the inn.")
#         print("\"Yeah, yeah, an' I'll bet if I turned out your purse there'd be not but a fly innit.\" Then he hoists you to your feet and begins to try and cuff you.")
#         choice == input("Will you attempt to FIGHT the guard's attempts to arrest you, or GO ALONG with them?")
#         if choice == "FIGHT":
#             # A brief fight determined by RNG breaks out,
#             # If you win, you're free and can leave town
#             # If you lose, you awake badly beaten, and stipped to your trousers
#             # Your only options are to SERVE your time or PICK LOCK

# Responsible Drunkard Path
elif choice == "WORK":
    # You work off your debts in the kitchen for an evening,
    # SEE or STOP a bar fight
    # Then catch the carriage out of town

# Humorous Death PRIME 
else:
    print("\nYou try to clamber up to speak, but the barmaid panics and backhands you with a frying pan that you hadn't noticed,")
    print("You are sent careening into a table, folding backwards and rolling into a dumbwaiter.")
    print("Before you know it, the dumbwaiter shoots up, and deposits you into the second floor hallway of the inn.")
    print("As you try to stand and reorient yourself, an orc wrapped in a towel steps out the bathing room to your left and hits you in the back with the door, causing you to roll forward down the hall before hurtling out the open door to the tiny balcony of the inn.")
    print("Your sheer momentum causes you to barrel through the safety rails, hurtling down towards the street right over an open sewer hatch.")
    print("The last that anyone ever sees of you is a green-brown pillar of water as you plunge into the city's sewer system, never to be seen again.")

print("Thus ends our little tale for you. We hoped you enjoyed.")