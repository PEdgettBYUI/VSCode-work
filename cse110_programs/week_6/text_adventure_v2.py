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
    print("\"F'oi'ne then. At least you seemed earnest about it. Off with ya then.\" she says waving you away.")
    print("A little dejected, but ultimately thankful of her kindness for you, you begin to wander towards the town gates to the West to try and hitch a carriage ride back home.")
    print("Arriving just in time, you see a carriage finishing loading it's passengers and cargo into the back of the hooded wagon, above you see a sign that reads:.")
    choice = input("'Ride: 5 Gilder OR work.' Knowing you haven't a penny to your name, you must decide if you're going to WALK or WORK. ").upper()
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
        choice = input("You spring to your feet, and realize you're outnumbered 3 to 1. You have no weapons on you. Do you try and DISTRACT them or try to JOIN them? ").upper()
        if choice == "DISTRACT":
            print("Thinking quickly, you spot a rotting husk close to the fire and concoct a plan.")
            print("You reach into your hip pouch and dig out the chunk of dried sausage you have and wave it in front of them.")
            print("They seem fascinated by it, the shortest one seems to be drooling. And you huck it off to your right, away from the path, and bolt as they turn to squabble over it.")
            print("Even though they're out of sight, you keep running just in case, and soon you find yourself coming to a clearing in the trees, and spot a post where the trail path forks.")
            print("\"Left to Davensport: 20 miles\" & \"Right to Thugsborough 5 miles\" \nYou know that Davensport is a respectable town by the river where you might get on a boat or work as a fisherman for awhile.")
            print("Thugsborough is an appropriately named town, infamous as the supposed home of the thieves guild. Not quite a happy place, but close enough to resupply if you dare.")
            choice == input("With no money, and no food, you're left with 2 choices: go LEFT 20 miles to Davensport, or go RIGHT 5 miles to Thugsborough. ").upper()
            if choice == "LEFT":
                print("You begin to wander the 20 miles to Davensport, deciding it's safer than dealing with cutpurses empty handed.")
                print("You manage to make it 10 miles, dragging yourself as you finally hunker down beneath a tree.")
                print("Checking your bag, you confirm what you were afraid of: No food, no money, and no means of self-defense.")
                print("You decide to wind down for the long eve ahead of you and get some sleep.")
                print("You barely manage to get to sleep after a few hours of hunger knawing at you when you're suddenly thrust awake.")
                print("You find yourself startled as you're flipped over by a thin and ragged man, no doubt mistaking you for a corpse")
                print("He realizes his mistake and stammers \"Oh, s-sir, forgive me. I thought you were...\" trailing off, he looks away ashamed.")
                choice = input("Assessing him quickly, you think you could probably overpower him and TAKE what he has instead, or perhaps you could BEG for some food. ").upper()
                if choice == "TAKE":
                    print("Making for a jumping tackle, you quickly find yourself sailing over him and landing face down in the dirt.")
                    print("You definitely didn't miss, it seems he caught you and helped hurl you overhead. It seems your assessment was starkly wrong.")
                    print("Lying in the mud, you flip over to see a lean but fierce figure scowling over you. You realize you're doomed.")
                    print("He straddles you, and takes a heavy looking club off his belt, and the last thing you remember seeing is a chunk of hard oak hurtling toward your head.")
                elif choice == "BEG":
                    print("You crawl to the strangers feet and grovel before him.")
                    print("A look of pity crosses his face, before he roots through his bag. He pulls out an apple and hands it to you.")
                    print("\"Rough day friend?\" he says as he sits next to you. \"Same for me. My friends are missing and I'm trying to find them.\"")
                    print("He sits silently as you finish the apple, staring into the night sky. \"Say,\" he starts slowly, \"Wanna come with me?\"")
                    choice = input("\"Me friends and I 're after a treasure meant to be just South of Davensport, you could COME WITH and get a share. Or, ya know, maybe you're NOT INTERESTED, wot with the hunger an' all.\" ").upper()
                    if choice == "COME WITH":
                        print("You're intrigued by his offer, and decide that traveling in search of treasure sounds much better than starving alone.")
                        print("Come morning, you and your new companion are off to Davensport seeking adventure,")
                        print("But what you find is a tale for another time...")
                    elif choice == "NOT INTERESTED":
                        print("You decline his offer, saying that you've had your fill of excitement for awhile, and you'd rather find somewhere quiet with a bit of grub.")
                        print("He nods, \"Fair e'nough friend. 'Ere, have dis.\" He turns and turns back to you, now holding a small pouch of gilder.")
                        print("You hesitate at first, but he places it in your palm saying, \"I've plenty more o' that in my future. Get some bread or something when you reach town. You look terrible.\"")
                        print("You fall asleep, and when you wake up you find that the stranger has already left.")
                        print("Soon you follow suit and head off to town. Hoping that this encounter will be a sign of your fortune's change.")
                    else:
                        print("As you weigh your options, you tell him you'll sleep on his offer. He nods and tells you that's fine.")
                        print("In the morning you awaken to see the stranger cooking something.")
                        print("\"'Ere, have some grub.\" He says offering you some kind of gruel that smells oddly sweet, and for some reason, familiar.")
                        print("Not thinking too hard about it, you happily take his offer and shovel the gruel into your mouth.")
                        print("Very soon you begin to feel like you're having a hard time breathing, and try to ask for some water. Your companion turns and looks on you with abject horror before quickly trying to undo his flask.")
                        print("Despite your best attempts to guzzle down the water you still feel your throat tightening, you struggle to ask what was in that food.")
                        print("\"Just some, s-some dried oats and h-honey.\" He stammers quickly. Honey, of course. You think to yourself. That's why it smelled familiar.")
                        print("Little did your companion know, you're deathly allergic to honey. And you just ate a whole bowl of it.")
                        print("And as your vision fades, and your breathing becomes quicker and raspier, the last thing you see if your companion panicking as he roots through his bag trying to figure out how to save you.")
                else:
                    print("You find yourself unable to decide what to do, and decide to play dead instead.")
                    print("The stranger looks back confused before deciding you were dead after all \"Oh Rudy,\" he says to himself \"Jumping at corpses. If the rest of 'em knew 'bout this you'd be a laughing stock for sure.\"")
                    print("He proceeds to finish rooting through your pockets before leaving deciding that someone else must've picked your pockets already,")
                    print("What else would you expect from a stiff on the side of the road? Soon, he vanishes into the night, and you sit up and congradulate yourself on escaping that situation.")
                    print("Then you notice the tree behind you give way, and you're soon wrapped up in vines and roots. It seems you've managed to find a False Ent in the dead of night.")
                    print("Soon you're pulled into the tree, and as the vines wrap around your mouth and fold you into a tube shape, you watch in horror as the bark shuts in front of you,")
                    print("And your last thought as you're pressed into the bark is that at least you get to see what it would've looked like to be buried.")
            elif choice == "RIGHT":
                # Expand in future to a real option
                print("You decide to take your chances in Thugsborough. You arrive after a shockingly uneventful trip just after nightfall.")
                print("You approach the crumbling wall that surrounds the city and approach the main gate. \"Oi, boy. Yer either out pas' curf'ew or don't b'long 'ere. Which is it?\" barks the guard at the gate.")
                print("You decide to tell him that you're just looking for work and food, \"Jus' pay the toll of f' off.\" He says uninterested in your explaination. \"10 Gilder for entry.\"")
                print("You remember that you haven't a dime to your name, so all that's left is to either SNEAK in or GO BACK.")
                print("Deciding you can only try and get inside, you attempt to scour the walls around the village for foothold to clamber up the wall.")
                print("Your search isn't long, and soon you find yourself 30 feet up at the top of an either ancient, or poorly made wall.")
                print("You find a starway down one of the towerpoints aligning the wall, and soon enough you're off to scour the streets of Thugsborough looking for adventure...")       
            else:
                print("You spend hours weighing your options. You sit in the middle of the crossroads just staring up and the sign, left palm on your thigh, right hand caressing your chin.")
                print("A week passes, and a caravan headed back from Davensport comes to the same crossroads, and finds a shabby looking skeleton sitting crosslegged in the middle of the road.")
                print("Apparently you're not the sharpest tool in the box. It shouldn't be that hard of a choice here!")
        elif choice == "JOIN":
            print("In perhaps a moment of madness, you throw yourself down again at the feet of what you hope is the leader, begging that you could join them and help them hunt.")
            print("Eyes closed, fearing for your life, and baffled by what you just said, you brace for the worst. You hear squabbling is half-broken english that seems to last forever.")
            print("Suddenly, you're pulled to you feet, and the head goblin tries to look tall despite being half your size, as he points towards a log by the fire.")
            print("\"S'it.\" he half-slurs as he gives the command. As you sit, a second goblin scurries toward a horribly worn patchwork bag and begins rooting around for something.")
            print("\"Br'an.\" He croaks trying to explain, \"I'v loy'l, git br'an.\" and looking back past him, you see the second goblin poking a metal stick into the fire, dancing  around the flame.")
            choice == input("It dawns on you that every goblin has a brand on their cheek, and now you had to decide do you COMMIT and become a member of a goblin tribe? or do you FLEA and hope that they're too distracted to pursue you.").upper()
            if choice == "COMMIT":
                print("You shrink as you try to figure out how you got here. But resolute, you wait and watch in resolute-horror as the second goblin walks toward you, and you turn so that he gets your cheek.")
                print("And so, long after a rumor floats around the surrounding forest that deep within, a man leads a goblin army in the woods. Leaving animal husks, and pillaged carravans along the now disued road.")
            elif choice == "FLEA":
                print("Imagery of yourself surrounded till old age by goblins, having spent your life hunting, pillaging, wrestling, and doing rituals with these diminuative gremlins,")
                print("Driven by a flooding sense of horror, you leap to your feet, screaming, and bolt off into the woods.")
                print("Glancing back, you see the entire tribe in a fervor pursuing, you. You make it no more than 100 feet before you are encompassed by goblins.")
                print("And as the world fades from your mind, you know that there will soon be nothing left of you for the world to find.")
            else:
                print("Before you realize it, the hot brand is right in your face. You jump a bit and the brand hits you in the eye.")
                print("The hot poker feels agonizing as it brands your eye shut. You're not paying attention, overwhelmed by the pain, but you stumble forwards and tip into the fire.")
                print("The unfortunate events that follow shortly after this mishap have been deemed too graphic to retell.")
                print("So, long and short, you die. And a rumor of a flaming demon coming in the middle of the day and burning down the Old Forest outlasts your charred body for ages to come.")
        else:
            print("Unable to decide what to do, you find yourself stripped naked and slathered in oil and leaves in the woods as the goblins point and cackle at the fool you've been made into.")
            print("Ashamed, and hungry, you stumble back to the road just in time for the carriage you passed by to catch up with you.")
            print("Unfortunately, the man they got to watch was so spooked by your appearance, that it wasn't until after he ran you through that he learned you were not \"a forest spirit come to eat them.\" Shame that.")
    else:
        print("Unable to make up your mind, the cart leaves you behind. Lost in thought, you fail to notice the Oxen cart pull up behind you.")
        print("You turn around to find yourself nose to nose with the Ox leading the cart, and yelp in surprise.")
        print("Your shock proves infectious enough that the Ox, twice your size, rears back on it's legs, tipping the cart behind it before landing on your head belly first.")
        print("After the sleeping cart driver makes sure that nothing was damaged scolds his ox before clambering back onto the cart and going about his day.")
        print("Unbeknownst to the driver, or anyone else, you've been driven into the ground like a nail into a board. Unable to move or breath, you pass unnoticed and become part of the path.")
        print("Perhaps, next time you should be a bit more decisive, hmm?")

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
    print("You offer to work off what you owe. She chuckles a bit, before responding, \"Not a penny on ya then, eh? Well, fair 'nough then,\" ")
    print("She walks through the door to the back then comes out tossing you an appron. \"You'll be the dish washer for today. Come on then.\" she says beckoning you to follow")
    print("When you reach the back you're staggered by the sheer number of dirty dishes piled in front of you. The plates touch the ceiling, and the cups are arranged in a pyramid.")
    print("\"You'll be starting now. Lunch will be around noon, on the house, but not your pick.\" she practically purrs with enthusiasm at your horror.")
    print("Soon you're left to your devices, and begin to wash, starting with the plates.")
    print("As the day begins to fade into night, you can glance past the door and see a group of surly looking men chatting and harassing other customers.")
    print("Soon one of them gets handsy and grabs the bottom of a passing woman. She turns and slaps her assailant, and he gets up. He hurls his tankard after her as she makes for the door, ale trailing as it goes.")
    print("As she leaves, the tankard hits the back of a large man in a leotard's head. He gets up, covered in ale and turns to see the goon who threw it laughing at him and pointing.")
    print("Just as the two men come with in arms reach of each other the barmaid from this morning steps between them.")
    choice = input("Will you just WATCH how it plays out, continuing your insurmountable task? Or will you go out there and help her STOP the fight that's about to break out.").upper()
    if choice == "WATCH":
        print("You decide it's not your problem right now, but you'll keep an eye on it to see if it will be.")
        print("You can't hear what said, but there's clearly terse exchange between the two men as the tiny barmaid tries to get their attention and calm the situation.")
        print("Soon enough they're trading blows as the barmaid watches in a huff. Then, you notice her unhook a bright red vial from her belt and down it.")
        print("You don't see any visible change, but she grabs both men by the wrist and squeezes, apparently so hard that she has their full undivided attention.")
        print("After some brief words from the barmaid, and some fierce nodding from the men, they're casually picked up by the seat of their pants by the diminuative figure and huffed through the front door.")
        print("Astonished, you glare wide eyed and open mouthed at the display. As the barmaid dusts herself off she catches your stare. She waves gingerly before making a show of flexing an arm.")
        print("You decide to scrub faster and harder.")
        print("Soon, you find yourself being woken up by the barmaid. It seems that in your fervor to clean the dishes you wore yourself out and passed out in the middle of scrubbing.")
        print("As you notice your entire right arm up to your elbow looks like a raisin, and feels numb the barmaid chortles hideously \"I can't believe you managed to get so much done. I didn't scare you that badly did I??\"")
        print("As she composes yourself, you find that well over half of the dishes are now sitting hazardously stacked behind you looking spotless.")
        print("\"Well, a deal's a deal.\" She says offering her right hand, before awkwardly switching to her left. You take her hand and shake it. As you pull it back you find a string loop of 7 gilder in your hand.")
        print("\"Consider that a bonus.\" she chirps, \"And if you spend it all in one place, make sure it's here.\" she says as she winks.")
        choice = input("From here, you decide to weigh your options: STAY here at the Inn and mayber earn a bit more gilder, or LEAVE town and continue your journey elsewhere.").upper()
        if choice == "LEAVE":
            print("You decide to ignore her advice and go elsewhere. Exiting the Inn you find it's just after dawn.")
            print("And with a little pocket change, you decide to take the carriage out of town to Davensborough and find some work there.")
        elif choice == "STAY":
            print("You decide to ask about keeping working for the Inn.")
            print("And soon enough you've gone through a month working at the inn. You've gone from dish washer to server to barkeep in what feels like such little time.")
            print("During the day you run a few errands for the Innkeep, and at night you run the tap behind the counter.")
            print("Life is good, and you've just about gotten the courage to ask Rosy at the market out for a date.")
            print("And you're thankful for losing that drinking game that's gotten you to where you are now, well on your way to a peaceful, simple life.")
        else:
            print("In the end you decide to keep the party going.")
            print("Looking outside, you see it's just after dawn, but decide it's nighttime somewhere. And as you slug back your 4th round of ale just after sunset")
            print("A familiar stout little man walks into the tavern, and you offer him the challenge of a drinking game....")
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