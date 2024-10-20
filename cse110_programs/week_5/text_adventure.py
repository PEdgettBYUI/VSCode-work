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
        print("Soon you enter a nearby forest, with a dense underbrush on a wagon-wheel made path. The uneven terrain makes you walk just off the road in the treeline.")
        print("Your eyes fixated on the path to your left, suddenly, you find your self tumbling downhill, not noticing the short drop ahead of you.")
        print("When you come to a stop, you find yourself at the foot of a campfire. Glancing up, you see the green, molting foot of a goblin.")
        choice == input("You spring to your feet, and realize you're outnumbered 3 to 1. You have no weapons on you. Do you try and DISTRACT them or try to JOIN them?").upper()
        if choice == "DISTRACT":
            print("Thinking quickly, you spot a rotting husk close to the fire and concoct a plan.")
            print("You reach into your hip pouch and dig out the chunk of dried sausage you have and wave it in front of them.")
            print("They seem fascinated by it, the shortest one seems to be drooling. And you huck it off to your right, away from the path, and bolt as they turn to squabble over it.")
            print("Even though they're out of sight, you keep running just in case, and soon you find yourself coming to a clearing in the trees, and spot a post where the trail path forks.")
            print("\"Left to Davensport: 20 miles\" & \"Right to Thugsborough 5 miles\" \nYou know that Davensport is a respectable town by the river where you might get on a boat or work as a fisherman for awhile.")
            print("Thugsborough is an appropriately named town, infamous as the supposed home of the thieves guild. Not quite a happy place, but close enough to resupply if you dare.")
            choice == input("With no money, and no food, you're left with 2 choices: go LEFT 20 miles to Davensport, or go RIGHT 5 miles to Thugsborough.")
        elif choice == "JOIN":
            print("In perhaps a moment of madness, you throw yourself down again at the feet of what you hope is the leader, begging that you could join them and help them hunt.")
            print("Eyes closed, fearing for your life, and baffled by what you just said, you brace for the worst. You hear squabbling is half-broken english that seems to last forever.")
            print("Suddenly, you're pulled to you feet, and the head goblin tries to look tall despite being half your size, as he points towards a log by the fire.")
            print("\"S'it.\" he half-slurs as he gives the command. As you sit, a second goblin scurries toward a horribly worn patchwork bag and begins rooting around for something.")
            print("\"Br'an.\" He croaks trying to explain, \"I'v loy'l, git br'an.\" and looking back past him, you see the second goblin poking a metal stick into the fire, dancing  around the flame.")
            choice == input("It dawns on you that every goblin has a brand on their cheek, and now you had to decide do you COMMIT and become a member of a goblin tribe? or do you FLEA and hope that they're too distracted to pursue you.")
            if choice == "COMMIT":
                print("You shrink as you try to figure out how you got here. But resolute, you wait and watch in resolute-horror as the second goblin walks toward you, and you turn so that he gets your cheek.")
                print("And so, long after a rumor floats around the surrounding forest that deep within, a man leads a goblin army in the woods. Leaving animal husks, and pillaged carravans along the now disued road.")
            elif choice == "FLEA":
                print("Imagery of yourself surrounded till old age by goblins, having spent your life hunting, pillaging, wrestling, and doing rituals with these diminuative gremlins,")
                print("Driven by a flooding sense of horror, you leap to your feet, screaming, and bolt off into the woods.")
                print("Glancing back, you see the entire tribe in a fervor pursuing, you. You make it no more than 100 feet before you are encompassed by goblins.")
                print("And as the world fades from your mind, you know that there will soon be nothing left of you for the world to find.")

        # if choice == "FLEA":
        # # FIGHT or RUN from some goblins
        # # FIGHT: Attempt to fight goblins using RNG
        #     # Win: You survive, beaten and bruised. A different
        # # RUN: Die falling into a ravine

# Criminal Misunderstandings Path
elif choice == "SCRAM":
    print("\nYou hear her shouting in the distance about how much of a good-for-nothing lout you are, and that you aren't welcome back again.")
    print("Turning around, you try and catch a glimpse of the red on her face before you crash to the ground after running head-long into a thick necked guard.")
    print("\"Oi, ya bum, watch where yer goin'.\" He gravels as he turns around, pointing his spear in your general direction.")
    print("Looking past you on the ground, he sees the angry barmaid yelling profanities towards you before turning in a huff and slamming shut the inn's doors behind her.")
    print("Looking back at the guard you see he's got a different idea about why she was so upset.")
    print("\"So,\" he starts with a cruel smirk before slowly continuing, \"robbin' da inn, eh? An' 'fore noon, no less.\"")
    print("Wagging his index finger like you were a naughty child caught with your hand in the cookie jar. \"V'ry naughty, then.\"")
    choice = input("Will you PROTEST the guards accusations, or GO ALONG quietly with him? ").upper()
    if choice == "PROTEST":
        print("You swear to the guard you haven't a penny on you, and that proves you couldn't have robbed the inn.")
        print("\"Yeah, yeah, an' I'll bet if I turned out your purse there'd be not but a fly innit.\" Then he hoists you to your feet and begins to try and cuff you.")
        # choice == input("Will you attempt to FIGHT the guard's attempts to arrest you, or GO ALONG with them?")
        # if choice == "FIGHT":
        #     # A brief fight determined by RNG breaks out,
        #     # If you win, you're free and can leave town
        #     # If you lose, you awake badly beaten, and stipped to your trousers
        #     # Your only options are to SERVE your time or PICK LOCK
    if choice == "GO ALONG":
        print("TEST PHRASE")

# Responsible Drunkard Path
elif choice == "WORK":
    print("TEST PHRASE")
    # You work off your debts in the kitchen for an evening,
    # WATCH or STOP a bar fight
    # Then catch the carriage out of town
    if choice == "WATCH":
        print("TEST PHRASE")
    elif choice == "STOP":
        print("TEST PHRASE")

# Humorous Death PRIME 
# In-directly hints towards third path
else:
    print("\nYou try to clamber up to speak, but the barmaid panics and backhands you with a frying pan that you hadn't noticed,")
    print("You are sent careening into a table, folding backwards and rolling into a dumbwaiter.")
    print("Before you know it, the dumbwaiter shoots up, and deposits you into the second floor hallway of the inn.")
    print("As you try to stand and reorient yourself, an orc wrapped in a towel steps out the bathing room to your left and hits you in the back with the door, causing you to roll forward down the hall before hurtling out the open door to the tiny balcony of the inn.")
    print("Your sheer momentum causes you to barrel through the safety rails, hurtling down towards the street right over an open sewer hatch.")
    print("The last that anyone ever sees of you is a green-brown pillar of water as you plunge into the city's sewer system, never to be seen again.")
    print("Perhaps you should WORK more dilligently next time, eh?")

print("Thus ends our little tale for you. We hoped you enjoyed.")