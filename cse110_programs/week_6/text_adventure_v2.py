# A Text Adventure based on my own writings as a DM
# Patrick Edgett
#10/26/24

import random

# Introduction
print("~ Your Tale ~")
print("Before you lies a tale yet written. You are it's co-author, and your actions dictate it's flow.")
print("But this tale is not all-encompassing, you may only impact a few things. Choose your path carefully, for in this tale the consequences are irreversible...\n")
print("__________________________________________________________________________________________")

# Setting the scene
print("\nYou find yourself alone, with an aching head, at the Flailing Jaguar Inn in Rhuin.")
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
        print("\nYou explain that you're seeking passage out of town, and that you're willing to work for your spot on the carriage.")
        print("\"Well then, 'Lookout,'\" he says before pausing. Reaching underneath his seat he pulls out a leather sheath, and tosses it to you.")
        print("\"Seems to me that it'll fall on you to keep us safe if we see any nasties. Climb on back. Your seat's right on the step.\"")
        print("Sitting down on the tiny step, you coil your left arm around the post on the lip of the wagon, and check the shortsword you've been given.")
        print("It's old, rusted, and stained. And frankly, you're pretty sure it's dull. Attached to the side is a whetstone that you use to try and sharpen the sword in vain.")
        print("Soon enough you're well within the trees of the Old Forest, the densest woods in the land, with some trees so wide they look like log cabins that reach the sky.")
        print("Clambering up the small ladder by the back of the carriage, you peer ahead and notice something odd. There appears to be smoke coming just off the road ahead.")
        print("You climb down, hop out, and walk around to the front of the still moving carriage and inform the driver of what you say.")
        print("Scratching his chin, he ponders aloud to you, \"That can't be bandits, no one's that stupid.\" pausing to consider, he turns pale \"Goblins.\" he says with some alarm.")
        print("You know well enough that Goblins never travel without their tribe, which can number in the dozens at times. Small and stupid, but vicious, you know it'd be best to avoid them if possible.")
        print("Unfortunately for you, the carriage can only make it across the forest through the path ahead, and you're the guard for it.")
        choice = input("You must now decide, do you ABANDON your charge and try to get by unseen? Or do you hold yourself accountable and STAY with the carriage? ").upper()
        if choice == "ABANDON":
            print("\nYou decide to take your chances on your own. And before the driver can muster the words to beg you not to go, you turn and dart ahead on the path before veering off to the left.")
            print("You're just about past the smoke when you spot a lone Goblin ahead of you collecting branches. You stop and take a moment to assess your chances.")
            print("You see that he has a large dagger, that might as well be a short-sword in his hands, and a horn fashioned out of part of a deer's antler.")
            print("The horn's crude, but you wager that if he toots it the whole tribe will come rushing to help him. But you still have the sword given to you by your former companions.")
            choice = input("You have a few options, you could try to SNEAK past him, get the JUMP on him and take him out, or try to INTIMIDATE him. ").upper()
            if choice == "SNEAK":
                roll = random.randint(1, 100)
                if roll > 40:
                    print("\nTEMPORARY TEXT:")
                    print("You successfully sneak past the goblin, and soon find yourself at the other end of the forest. Having enough supplies to defend and feed yourself, you make for Davensport.")
                else:
                    print("\nTEMPORARY TEXT:")
                    print("You fail to sneak past the goblin, he blows his horn and you are soon swarmed and killed by the goblin horde.")
            elif choice == "JUMP":
                roll = random.randint(1, 100)
                if roll > 60:
                    print("\nTEMPORARY TEXT:")
                    print("You successfully sneak up on the goblin. You run him through from behind before he even notice you. You loot his body and find a crudely drawn map.")
                    print("The crudely drawn map seems to show that very soon there's going to be hundreds of goblins living right where you're standing.")
                    print("It also shows a cave off the path leading to Thugsborough, with a crudely drawn treasure chest. You decide to continue your adventure in pursuit of whatever the goblins left behind.")
                else:
                    print("\nTEMPORARY TEXT:")
                    print("You fail to sneak up on the goblin, he jumps away as you swing downward at him, and he runs as fast as his little legs can deeper into the woods.")
                    print("Pursuing, you suddenly find you've run headlong into a whole tribe that was heading towards you. You're soon overwhelmed and perish horrifically.")
            elif choice == "INTIMIDATE":
                roll = random.randint(1, 100)
                if roll > 80:
                    print("\nTEMPORARY TEXT:")
                    print("You cause the goblin to freeze in terror, and strip him of his weapon and horn. He then runs off towards the road as fast as he can, screaming the whole way.")
                    print("Worried about the noise, you quickly head north with your sword drawn and end up at the fork in the road between Davensport and Thugsborough. You make a choice")
                else:
                    print("\nTEMPORARY TEXT:")
                    print("The Goblin remains unintimidated, and starts laughing at you. You draw your sword, and the goblin bites into your hand as hard as it can.")
                    print("You throw it off and grab your sword with your other hand, and decide to make for the road. You arrive just as the carrivan crosses and convince them you went to fight off the goblins.")
                    print("They accept it seeing your mangled hand, and you climb aboard, handing your sword to another man in the carriage as the driver mushes his ox to go as fast as it can.")
                    print("You pass out and wake up in an inn, down a hand, and realize your days of adventuring are over. You're left to wonder where your life will go now.")
            else:
                print("\nIn the end you wait for him to pass. Deciding it's better to let him finish and go about your day.")
                print("Unfortunately, 7 more goblins appear from the woods. Clearly not part of the same group you passed. They begin to set up camp for the night, even though it's just after noon.")
                print("Seeing no alternative, you decide to wait them out. You get comfortable, sit inside a bush, and settle in for a long wait.")
                print("Just before sunset, you hear the squeaking of wooden wheels go past you. Seems they did just fine without you. Good for them.")
                print("As you settling in for the night, your find your dreams interupted by the sounds of excitement. Peering out the bushes you can see a goblin tribe of 5 members coming the way you came, one bearing more wood, and the other 4 carrying a doe.")
                print("To your horror, they plant the wood on the other side of the bush with the carcass, and 2 of them go to the other camp while the one with wood sets up a fire.")
                print("Now there are more than 12 Goblins surrounding you. You decide to try and wait them out, and manage to eventually find sleep.")
                print("In the morning, you find another tribe has moved in around you. This time of 20 members. You they have even more deer carcasses piled up by the first.")
                print("An impending sense of doom overcomes you. By sheer misfortune, you've managed to get yourself stuck in the middle of what will soon become a Goblin shanty in the woods.")
                print("You're paralyzed with panic, and have to now figure out just how to get yourself out of this mess.")
                print("But that story is for another time....")
        elif choice == "STAY":
            print("\nYou decide to stay and defend the carriage if it comes to it. The carriage comes along slower now going up the road, slow enough that you easily outpace it walking along side it.")
            print("Soon enough you spot the source of the smoke, and just as the driver predicted there's a camp of about 5 goblins dancing around a fire just off the side of the road.")
            print("You decide to stay close to the carriage and just keep an eye on the goblins. Maybe you'll get by without incident.")
            print("As you approach, the goblins take notice and stop dancing. They stare at you and carriage as you pass.")
            print("You glare back at them. One of the goblins pushes to the front then turns and speaks to his goblins.")
            print("It feels like an hour as you slowly pass the camp, watching them argue amoungst themselves.")
            roll = random.randint(1, 100)
            if roll > 70:
                print("\nThe head goblin turns back and screeches at you, you instinctively clasp your sword in it's sheath in case they move.")
                print("Then the goblin turns and waves everyone back to the fire.")
                print("You are lucky to pass by without incident.")
                print("Soon you find yourself in an open field, ahead of you is a fork in the road.")
                print("\"Climb in lad,\" calls the driver, \"It should be smooth sailing from here.\"")
                print("You pause and wait for the cart to pass you before clambering onto the back step. You keep the sword close by, but wind down and relax a bit.")
                print("Before you know it you're being woken up by the driver. You must've nodded off. You glance around and find you're just outside the cobbled walls of Davensport.")
                print("You can see the market through the front gate, and off in the distance you see a small merchant ship coming up the river from the distant bay.")
                choice = input("After returning what you were loaned, you now have one choice to decide: Do you head to the MARKET looking for work, or do you head to the DOCK and book passage across the sea? ").upper()
                if choice == "MARKET":
                    print("\nYou resolve to stay in town awhile and earn a few gilder to buy some supplies, and maybe even make a fortune if you're lucky.")
                    print("Approaching the market, you overhear an old man outside the inn complaining about a treasure that would've been his if he hadn't taken an arrow to his knee.")
                    print("Intrigued, you approach him. But that tale is for another time...")
                elif choice == "DOCK":
                    print("\nAs nice a town as Davenport is, you really want to get back on the seas. You hope your sea-legs haven't left you as you head to the dock.")
                    print("The dock is quite long, running a large stretch of the riverside. A few man-made docking bays line the pier at points.")
                    print("You spot a sloop in one of them in the middle of unloading. You decide to make yourself useful in hopes to prove some worth to it's captain.")
                    print("Later in the evening you're trading stories in the pub with the captain and his crew, and joining in on the festivities. You depart on the Gilly Ox in two days time...")
                else:
                    print("\nTEMPORARY TEXT: ")
                    print("You die of indecision")
            else:
                print("\nThe head goblin turns back towards you and pulls a horn up to his lips. As he blows the shrill trumpet the other goblins grab their weapons.")
                print("You steel yourself for their attack. The leader holds a hand up, then walks towards you. He makes a gesture like a bow, then draws a dagger from his belt.")
                print("It appears that the goblin is going to challenge you in a duel, which is very lucky for you.")
                print("The dagger looks more like a short-sword in his hands, you wager you could easily overpower him.")
                print("You ready yourself, sword drawn in two hands in front of you.")
                roll = random.randint(1,100)
                if roll > 65:
                    print("\nThe goblin swings first at your sword as if to indicate a start to the duel. You clash briefly. You're caught off guard with how hard it is to hit the goblin.")
                    print("Every swing you think you'll connect he jumps over, or rolls away from.")
                    print("But your stronger, and bigger, and soon enough the goblin's dagger goes flying into the woods. He turns and bares his teeth and short claws to you, but you place your sword tip at his chin.")
                    print("The glances down, and with one finger lowers the sword. He spits at your feet then turns back to his tribe. The tribe boos him as he returns, and he takes his leather cap off his head and tosses it to the nearest to him.")
                    print("Satisfied, you tell the driver to pick up the pace and that you're done here.")
                    print("Soon enough, you're in the cart being praised by the passengers. They all pool together a small bag of a gilder a piece and give it to you.")
                    print("You finish counting the coins as the cart pulls into Davensport. 12 gilder in all.")
                    print("The driver approaches you as you get out the cart, \"Fine swordsmanship boy, you must be quite experienced.\" he says.")
                    print("You place the sword in his hand and tell him thanks. \"You know, if you stick around I might be able to help you get a reasonable wage, something more stable than an adventurer's life.\"")
                    print("A stable income would be a good change of pace to you, and guarding the carriage would be exciting enough to keep you interested, but you came here to get back to the sea.")
                    choice = input("Do you want to stay and work as a carriage ESCORT, or get to the docks and become a SAILOR? ").upper()
                    if choice == "ESCORT":
                        print("\nYou accept his offer. And spend a good few years earning a good sum roaming the roads to and from Davensport.")
                        print("Dealing with the occassional bandits, goblins, and that one time you fought a griffin; which you never stop telling people at the pub.")
                        print("One day, you're old, telling your children about your life, wondering where time went...")
                    elif choice == "SAILOR":
                        print("\nYou decline his offer, and tell him you're looking to get back to the seas. He nods and thanks you for your help before giving you a 3 gilder for your aid.")
                        print("You're soon at the dock looking for a ship. Ahead of you, a marvel of a brigantine is pulling into the bay. You know exactly which ship you wanna join up with...")
                    else:
                        print("\nTEMPORARY TEXT:")
                        print("You die of indecision.")
        else:
            print("\nTEMPORARY TEXT: ")
            print("You die of indecision")
    elif choice == "WALK":
        print("\nDeciding that you'd prefer not to exhaust yourself to earn a spot on the cart, you decide to hoof it on foot.")
        print("Soon you enter a nearby forest, with a dense underbrush on a wagon-wheel made path. The uneven terrain makes you walk just off the road in the treeline.")
        print("Your eyes fixated on the path to your left, suddenly, you find your self tumbling downhill, not noticing the short drop ahead of you.")
        print("When you come to a stop, you find yourself at the foot of a campfire. Glancing up, you see the green, molting foot of a goblin.")
        choice = input("You spring to your feet, and realize you're outnumbered 5 to 1. You have no weapons on you. Do you try and DISTRACT them or try to JOIN them? ").upper()
        if choice == "DISTRACT":
            print("\nThinking quickly, you spot a rotting husk close to the fire and concoct a plan.")
            print("You reach into your hip pouch and dig out the chunk of dried sausage you have and wave it in front of them.")
            print("They seem fascinated by it, the shortest one seems to be drooling. And you huck it off to your right, away from the path, and bolt as they turn to squabble over it.")
            print("Even though they're out of sight, you keep running just in case, and soon you find yourself coming to a clearing in the trees, and spot a post where the trail path forks.")
            print("\"Left to Davensport: 20 miles\" & \"Right to Thugsborough 5 miles\" \nYou know that Davensport is a respectable town by the river where you might get on a boat or work as a fisherman for awhile.")
            print("Thugsborough is an appropriately named town, infamous as the supposed home of the thieves guild. Not quite a happy place, but close enough to resupply if you dare.")
            choice = input("With no money, and no food, you're left with 2 choices: go LEFT 20 miles to Davensport, or go RIGHT 5 miles to Thugsborough. ").upper()
            if choice == "LEFT":
                print("\nYou begin to wander the 20 miles to Davensport, deciding it's safer than dealing with cutpurses empty handed.")
                print("You manage to make it 10 miles, dragging yourself as you finally hunker down beneath a tree.")
                print("Checking your bag, you confirm what you were afraid of: No food, no money, and no means of self-defense.")
                print("You decide to wind down for the long eve ahead of you and get some sleep.")
                print("You barely manage to get to sleep after a few hours of hunger knawing at you when you're suddenly thrust awake.")
                print("You find yourself startled as you're flipped over by a thin and ragged man, no doubt mistaking you for a corpse")
                print("He realizes his mistake and stammers \"Oh, s-sir, forgive me. I thought you were...\" trailing off, he looks away ashamed.")
                choice = input("Assessing him quickly, you think you could probably overpower him and TAKE what he has instead, or perhaps you could BEG for some food. ").upper()
                if choice == "TAKE":
                    print("\nMaking for a jumping tackle, you quickly find yourself sailing over him and landing face down in the dirt.")
                    print("You definitely didn't miss, it seems he caught you and helped hurl you overhead. It seems your assessment was starkly wrong.")
                    print("Lying in the mud, you flip over to see a lean but fierce figure scowling over you. You realize you're doomed.")
                    print("He straddles you, and takes a heavy looking club off his belt, and the last thing you remember seeing is a chunk of hard oak hurtling toward your head.")
                elif choice == "BEG":
                    print("\nYou crawl to the strangers feet and grovel before him.")
                    print("A look of pity crosses his face, before he roots through his bag. He pulls out an apple and hands it to you.")
                    print("\"Rough day friend?\" he says as he sits next to you. \"Same for me. My friends are missing and I'm trying to find them.\"")
                    print("He sits silently as you finish the apple, staring into the night sky. \"Say,\" he starts slowly, \"Wanna come with me?\"")
                    choice = input("\"Me friends and I 're after a treasure meant to be just South of Davensport, you could COME WITH and get a share. Or, ya know, maybe you're NOT INTERESTED, wot with the hunger an' all.\" ").upper()
                    if choice == "COME WITH":
                        print("\nYou're intrigued by his offer, and decide that traveling in search of treasure sounds much better than starving alone.")
                        print("Come morning, you and your new companion are off to Davensport seeking adventure,")
                        print("But what you find is a tale for another time...")
                    elif choice == "NOT INTERESTED":
                        print("\nYou decline his offer, saying that you've had your fill of excitement for awhile, and you'd rather find somewhere quiet with a bit of grub.")
                        print("He nods, \"Fair e'nough friend. 'Ere, have dis.\" He turns and turns back to you, now holding a small pouch of gilder.")
                        print("You hesitate at first, but he places it in your palm saying, \"I've plenty more o' that in my future. Get some bread or something when you reach town. You look terrible.\"")
                        print("You fall asleep, and when you wake up you find that the stranger has already left.")
                        print("Soon you follow suit and head off to town. Hoping that this encounter will be a sign of your fortune's change.")
                    else:
                        print("\nAs you weigh your options, you tell him you'll sleep on his offer. He nods and tells you that's fine.")
                        print("In the morning you awaken to see the stranger cooking something.")
                        print("\"'Ere, have some grub.\" He says offering you some kind of gruel that smells oddly sweet, and for some reason, familiar.")
                        print("Not thinking too hard about it, you happily take his offer and shovel the gruel into your mouth.")
                        print("Very soon you begin to feel like you're having a hard time breathing, and try to ask for some water. Your companion turns and looks on you with abject horror before quickly trying to undo his flask.")
                        print("Despite your best attempts to guzzle down the water you still feel your throat tightening, you struggle to ask what was in that food.")
                        print("\"Just some, s-some dried oats and h-honey.\" He stammers quickly. Honey, of course. You think to yourself. That's why it smelled familiar.")
                        print("Little did your companion know, you're deathly allergic to honey. And you just ate a whole bowl of it.")
                        print("And as your vision fades, and your breathing becomes quicker and raspier, the last thing you see if your companion panicking as he roots through his bag trying to figure out how to save you.")
                else:
                    print("\nYou find yourself unable to decide what to do, and decide to play dead instead.")
                    print("The stranger looks back confused before deciding you were dead after all \"Oh Rudy,\" he says to himself \"Jumping at corpses. If the rest of 'em knew 'bout this you'd be a laughing stock for sure.\"")
                    print("He proceeds to finish rooting through your pockets before leaving deciding that someone else must've picked your pockets already,")
                    print("What else would you expect from a stiff on the side of the road? Soon, he vanishes into the night, and you sit up and congradulate yourself on escaping that situation.")
                    print("Then you notice the tree behind you give way, and you're soon wrapped up in vines and roots. It seems you've managed to find a False Ent in the dead of night.")
                    print("Soon you're pulled into the tree, and as the vines wrap around your mouth and fold you into a tube shape, you watch in horror as the bark shuts in front of you,")
                    print("And your last thought as you're pressed into the bark is that at least you get to see what it would've looked like to be buried.")
            elif choice == "RIGHT":
                # Expand in future to a real option
                print("\nYou decide to take your chances in Thugsborough. You arrive after a shockingly uneventful trip just after nightfall.")
                print("You approach the crumbling wall that surrounds the city and approach the main gate. \"Oi, boy. Yer either out pas' curf'ew or don't b'long 'ere. Which is it?\" barks the guard at the gate.")
                print("You decide to tell him that you're just looking for work and food, \"Jus' pay the toll of f' off.\" He says uninterested in your explaination. \"10 Gilder for entry.\"")
                print("You remember that you haven't a dime to your name, so all that's left is to either SNEAK in or GO BACK.")
                print("Deciding you can only try and get inside, you attempt to scour the walls around the village for foothold to clamber up the wall.")
                print("Your search isn't long, and soon you find yourself 30 feet up at the top of an either ancient, or poorly made wall.")
                print("You find a starway down one of the towerpoints aligning the wall, and soon enough you're off to scour the streets of Thugsborough looking for adventure...")       
            else:
                print("\nYou spend hours weighing your options. You sit in the middle of the crossroads just staring up and the sign, left palm on your thigh, right hand caressing your chin.")
                print("A week passes, and a caravan headed back from Davensport comes to the same crossroads, and finds a shabby looking skeleton sitting crosslegged in the middle of the road.")
                print("Apparently you're not the sharpest tool in the box. It shouldn't be that hard of a choice here!")
        elif choice == "JOIN":
            print("\nIn perhaps a moment of madness, you throw yourself down again at the feet of what you hope is the leader, begging that you could join them and help them hunt.")
            print("Eyes closed, fearing for your life, and baffled by what you just said, you brace for the worst. You hear squabbling is half-broken english that seems to last forever.")
            print("Suddenly, you're pulled to you feet, and the head goblin tries to look tall despite being half your size, as he points towards a log by the fire.")
            print("\"S'it.\" he half-slurs as he gives the command. As you sit, a second goblin scurries toward a horribly worn patchwork bag and begins rooting around for something.")
            print("\"Br'an.\" He croaks trying to explain, \"I'v loy'l, git br'an.\" and looking back past him, you see the second goblin poking a metal stick into the fire, dancing  around the flame.")
            choice = input("It dawns on you that every goblin has a brand on their cheek, and now you had to decide do you COMMIT and become a member of a goblin tribe? or do you FLEA and hope that they're too distracted to pursue you. ").upper()
            if choice == "COMMIT":
                print("\nYou shrink as you try to figure out how you got here. But resolute, you wait and watch in resolute-horror as the second goblin walks toward you, and you turn so that he gets your cheek.")
                print("And so, long after a rumor floats around the surrounding forest that deep within, a man leads a goblin army in the woods. Leaving animal husks, and pillaged carravans along the now disued road.")
            elif choice == "FLEA":
                print("\nImagery of yourself surrounded till old age by goblins, having spent your life hunting, pillaging, wrestling, and doing rituals with these diminuative gremlins,")
                print("Driven by a flooding sense of horror, you leap to your feet, screaming, and bolt off into the woods.")
                print("Glancing back, you see the entire tribe in a fervor pursuing, you. You make it no more than 100 feet before you are encompassed by goblins.")
                print("And as the world fades from your mind, you know that there will soon be nothing left of you for the world to find.")
            else:
                print("\nBefore you realize it, the hot brand is right in your face. You jump a bit and the brand hits you in the eye.")
                print("The hot poker feels agonizing as it brands your eye shut. You're not paying attention, overwhelmed by the pain, but you stumble forwards and tip into the fire.")
                print("The unfortunate events that follow shortly after this mishap have been deemed too graphic to retell.")
                print("So, long and short, you die. And a rumor of a flaming demon coming in the middle of the day and burning down the Old Forest outlasts your charred body for ages to come.")
        else:
            print("\nUnable to decide what to do, you find yourself stripped naked and slathered in oil and leaves in the woods as the goblins point and cackle at the fool you've been made into.")
            print("Ashamed, and hungry, you stumble back to the road just in time for the carriage you passed by to catch up with you.")
            print("Unfortunately, the man they got to watch was so spooked by your appearance, that it wasn't until after he ran you through that he learned you were not \"a forest spirit come to eat them.\" Shame that.")
    else:
        print("\nUnable to make up your mind, the cart leaves you behind. Lost in thought, you fail to notice the Oxen cart pull up behind you.")
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
        print("\nYou swear to the guard you haven't a penny on you, and that proves you couldn't have robbed the inn.")
        print("\"Yeah, yeah, an' I'll bet if I turned out your purse there'd be not but a fly innit.\" Then he hoists you to your feet and begins to try and cuff you.")
        choice = input("Will you attempt to RESIST the guard's attempts to arrest you, or GO ALONG with them? ").upper()
        print(choice)
        # Continue From Here.
        if choice == "RESIST":
            roll = random.randint(1, 100)
            print(roll)
            if roll > 50:
                print("\nTEMPORARY TEXT:")
                print("You successfully wrestle the guard to the ground, in the scuffle you grab his truncheon and knock him out with it.")
                print("Realizing how much trouble you'll be in, you decide to leave town.")
                choice = input("You run south to the back end of town, hoping to find somewhere to hide out in the SLUMS, or sneak out the town SEWERS. ").upper()
                if choice == "SLUMS":
                    print("\nTEMPORARY TEXT:")
                    print("\nYou run, darting through alleys hoping that if you get lost yourself they won't be able to find you either. Soon you come to an abandoned shack.")
                    print("Running inside you are confronted by a street gang and barter to join them in exchange for protection from the law. In the end you become a member of a protection racket.")
                if choice == "SEWERS":
                    print("TEMPORARY TEXT:")
                    print("\nYou realize your best option is the sewers. You lift a manhole cover and clamber down a ladder, making sure the lid closes behind you.")
                    print("You find the sewers surprisingly well lit in the distance, and soon realize that the homeless and theieves guild operate down here, using the sewers as expressways through the city.")
                    choice = input("Weighing your options, you're left to decide whether to seek out the THIEVES GUILD and try to join up for protection, or get directions to LEAVE TOWN out the spillway.").upper()
                    if choice == "THIEVES GUILD":
                        print("\nTEMPORARY TEXT:")
                        print("You get directions from the beggars in the sewer and soon find yourself in a makeshift pub at the back of a storage chamber, long disused by the city.")
                        print("Soon you find yourself having to earn your keep to stay out of the eyes of the law and hopefully make a fortune yourself.")
                    elif choice == "LEAVE TOWN":
                        print("\nTEMPORARY TEXT:")
                        print("You ask the beggars the way to the spillway out of the sewers.")
                        print("After having to ask a few more beggars, you find yourself at the spillway. You clamber out, soaking your shoes in unmeantionably gross water.")
                        print("After brief moment to get your bearings, you find yourself at the south end of town. You happen to know that the town of Yenn is only abour 5 miles south of here.")
                        print("Soon you're off on the road, and wondering just how far the reach of the law in Rhuin is, or if you'll be on the run for awhile...")
            else:
                print("\nTEMPORARY TEXT:")
                print("You manage to wrestle the guard to the ground, but he knocks you with his truncheon while you straddle him.")
                print("You wake up behind bars with another guard standing with a thin, sharply dressed man with a power wig. He explains that you are to be jailed for 1 year.")
                choice = input("You must decide if you will try to ESCAPE or SERVE your time in jail. ").upper()
                if choice == "ESCAPE":
                    print("\nTEMPORARY TEXT:")
                    print("You make an attempt to pick the lock.")
                    roll = random.randint(1,100)
                    if roll > 65:
                        print("\nTEMPORARY TEXT:")
                        print("You pick the lock in the dead of night using a pin you keep in your hair just in case this ever happens.")
                        choice = input("You see a chest that contains your belongings, you may try to PICK CHEST or LEAVE. ").upper()
                        if choice == "PICK CHEST":
                            roll = random.randint(1, 100)
                            if roll > 75:
                                print("\nTEMPORARY TEXT:")
                                print("You get your clothes, a small dagger, belt, backpack with provisions, and empty wallet back.")
                                print("You Leave town looking like nothing ever happened to you.")
                            else:
                                print("\nTEMPORARY TEXT:")
                                print("The pick breaks, and you must leave town looking like a criminal on the run.")
                        elif choice == "LEAVE":
                            print("\nTEMPORARY TEXT:")
                            print("You leave town looking like a criminal on the run.")
                        else:
                            print("\nTEMPORARY TEXT:")
                            print("You die getting shot with a crossbow in the butt as you try to pick the lock of the chest.")
                        print("\nTEMPORARY TEXT:")
                        print("You fail to pick the lock. Without tools or any way to break the lock you are forced to serve your time.")
                        print("You are frequently caught trying to break out, which only extends your sentence further.")
                        print("You die of old age a stubborn man in the middle of planning his next escape.")
                    else:
                        print("You fail to pick the lock, but you can still use the pin.")
                        roll = random.randint(1, 100)
                        if roll > 75:
                            print("\nTEMPORARY TEXT:")
                            print("You pick the lock in the dead of night using a pin you keep in your hair just in case this ever happens, and sneak out of town")
                            print("The pin broke in the lock and you are unable to try and get your gear back, you look like a prisoner on the run")
                        else:
                            print("\nTEMPORARY TEXT:")
                            print("You fail to pick the lock. You spend the rest of your time wondering about the possibilities you might've missed on as you serve your sentence")
                            print("You leave jail bitter and defeated, and your first move is to head to the inn for a long drink...")
                elif choice == "SERVE":
                    print("\nMaking the best of your time, you begin to work out whenever you can.")
                    print("You make friends with the guards, and are eventually let out on good behavior just shy of 6 months into your sentence.")
                    print("You come out a lean, mean fighting machine, and decide to do a little work to get enough money to leave town on adventure.")
                    print("You eventually trade up your old clothes and dagger for a mace and leather breatplate.") 
                    print("You leave town and head west towards Firetop Mountain in hopes you'll find treasure in it's depths.")
                else:
                    #Real answer later
                    print("\nParalyzed be indecision, your head swells and explodes.")
        elif choice == "GO ALONG":
            print("\nTEMPORARY TEXT:")
            print("You explain your situation to the warden, he's accomodating seeing as how nothing was done and you confessed your issues at the inn.")
            print("He tells you to go back and assist the inn for one evening as a stablehand and tend to the ponys. You are sent out while the guard argues with the warden. You are alone.")
            choice = input("You can either do as he says and WORK STABLES for an evening, squaring your debts, or LEAVE town and head East towards the farming district and try to get some food for the road.").upper()
            if choice == "WORK STABLES":
                print("\nTEMPORARY TEXT:")
                print("You work the stables, square your debts and head north towards Davensport with just enough money from tips to make the carriage.")
            elif choice == "LEAVE":
                print("\nTEMPORARY TEXT:")
                print("You go East, steal some vegetables, hear a rumor about a vampire to the east, and go out in adventure to slay him and get a reward from the farmers.")
            else:
                print("\nYou pick up a rolling jar from the street, the inside is sticky, golden, and smells good but familiar for some reason that makes you nervous.")
                print("Throwing caution to the wind, you guzzle it down. You've just eaten half a jar of honey. You are deathly allergic.")
                print("\"Karma's a bitch.\" ad they say.")
    elif choice == "GO ALONG":
        print("\nYou decide to submit, and hopefully convince the warden of your innocence.")
        print("As you step inside the town jail, you see the warden filing paperwork in the corner to your right.")
        print("\"Constable, I see you've found some more paperwork for me eh?\" He says sarcastically, standing and brushing himself off.")
        print("\"Aye Warden Greeve. This one 'ere tried to rob the Inn. I's caught him as he fled.")
        print("The warden looks you up and down, he instructs the constable to search your pockets. The constable's smirk droops and he protests that it simply isn't neccessary as you were caught red handed.")
        print("\"Perhaps, but he doesn't strike me as having gotten away with much.\" he says as he examines you carefully. He looks back to the unmoving guard, \"Just humor me Cedric.\" He says gesturing towards you.")
        print("The guards shoulders sag, then he walks around you and turns out your pockets and pats you down. He find your wallet and turns it out, only to find it empty.")
        print("\"Warden,\" he says like a child caught in a fib, \"I swears it. I saw him fleaing the inn with the barmaid screaming every obscenity at him down the street.\"")
        print("\"Well, yes, it is unfortunate.\" He says, \"But seeing as he hasn't anything on him, and you say you were watching the scene unfold, I'd rather avoid the paper work.\"")
        print("You feel a burden lift off you and you smile a bit, then the warden turns back to you, \"Don't think you're free of this.\" he says. \"In exchange for this leniency, I'm having you assist me with my papers.\"")
        print("You shrink a bit as the guard chuckles loudly, satisfied with this result. The warden directs you to the small writing table next to his desk and has a brief discussion with the guard before the two part.")
        print("Soon enough, you're reading out sentences and reports, and pending hearing memos to the warden and writing back responses as he sips a coffee in his chair.")
        print("Many long hours pass, and you become fascinated by the papers. They detail the many comings and goings of people as well as their crimes.")
        choice = input("You ponder the idea of seeking an APPRENTICESHIP with the warden, or simply SERVING your small sentence before leaving town... ").upper()
        if choice == "APPRENTICESHIP":
            print("\nAs the evening settles, you inquire about the idea of apprenticing to the warden. He smirks a bit amused, and you think he'll decline.")
            print("\"If you mean take an Assistant position, then I am more than happy to take that request. Less paperwork for me afterall.\" He says sensing your dissappointment.")
            print("As you walk down the roadways he tells you to be back here right at dawn tomorrow and you'll discuss the details of the job further.")
            print("And as you make it back to the inn you remember that you're out of gilder. You decide to tell them to put the night on a tab and that you've got a job with the warden of the jail in the morning.")
            print("Deciding to accept you, inspite running out this morning, you head to your previous room upstairs and settle in for the night.")
            print("As you drift off to sleep, you feel this is a new begining for you...")
        elif choice == "SERVING":
            print("\nYou spend the rest of the day working papers for the warden. As night falls, he turns and tells you that you've served your dues, but he won't be so lenient if he sees you again.")
            print("You tell him you understand, and then he presses a paper into your hand. \"In your hand sits a letter of passage.\" he explains, \"Give it to the carriage driver and he'll take you to Davensport.\"")
            print("A bit confused, you ask why. \"You seem like the raucous type to me. And I'd prefer you to be someone elses problem, somewhere else.\"")
            print("He turns and waves you off as he walks away. You turn and examine the letter as you walk to the gate. Maybe you're still in time for the last carriage out of town...")
        else:
            print("\nYou never could stay awake in school when it came to reading time.")
            print("Soon you find yourself nodding off. The warden wakes you twice, frustrated. He warns you that if you pass out again he'll be glad to let you sleep out your sentence in a cell.")
            print("An hour passes, one that feels like a day, and soon enough you nod off despite the warden's warnings.")
            print("You're awakened as the guard from before drags you to your feet and roughly escorts to you to a cell.")
            print("\"Get cozy.\" He states beaming, \"You'll be here for 3 days, dinner is served after sunset and our menu consists of oat bread and leftover milk from breakfast.\"")
            print("Settling in, you decide that this might have just have been the rest you need before you make for the Old Forest. You pass out, somewhat satisfied of today's events.")
    else:
        print("\nTEMPORARY TEXT:")
        print("Turns out, you're deathly allergic to rope, and you melt into a puddle.")
# Responsible Drunkard Path
elif choice == "WORK":
    print("\nYou offer to work off what you owe. She chuckles a bit, before responding, \"Not a penny on ya then, eh? Well, fair 'nough then,\" ")
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
        print("\nYou decide it's not your problem right now, but you'll keep an eye on it to see if it will be.")
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
            print("\nYou decide to ignore her advice and go elsewhere. Exiting the Inn you find it's just after dawn.")
            print("And with a little pocket change, you decide to take the carriage out of town to Davensborough and find some work there.")
        elif choice == "STAY":
            print("\nYou decide to ask about keeping working for the Inn.")
            print("And soon enough you've gone through a month working at the inn. You've gone from dish washer to server to barkeep in what feels like such little time.")
            print("During the day you run a few errands for the Innkeep, and at night you run the tap behind the counter.")
            print("Life is good, and you've just about gotten the courage to ask Rosy at the market out for a date.")
            print("And you're thankful for losing that drinking game that's gotten you to where you are now, well on your way to a peaceful, simple life.")
        else:
            print("\nIn the end you decide to keep the party going.")
            print("Looking outside, you see it's just after dawn, but decide it's nighttime somewhere. And as you slug back your 4th round of ale just after sunset")
            print("A familiar stout little man walks into the tavern, and you offer him the challenge of a drinking game....")
    elif choice == "STOP":
        print("\nYou decide that you should intervene. As you step between the two men, you find yourself taking a blow to your left cheek.")
        print("The hit knocks you to the ground. Looking up both men are laughing at you.")
        print("Before you can drag yourself to your feet to do anything about their smug faces, they turn to each other and head off to arm wrestle.")
        print("\"Well fella, that was mighty dumb of you.\" said the barmaid as she presses a damp cloth to your face.")
        print("\"But that was brave enough of you.\" she helps you back to the back of the inn. \"Alrighty, you get back to work. I'll bring you some free grub in a bit. Think of it as a thanks.\"")
        print("She leaves the room, and you nurse your face a bit. Eventually you decide to get back to work.")
        print("You're elbow deep in a kettle when she returns. In her hands is a small chunk of hot ham, and a roll. You dig into the meal, savoring every bite. It's the best food you've had in awhile")
        print("Soon you're left on your own to continue working. As the night winds down, and the pub closes up the barmaid comes back in \"Alright fella, that's plenty of work.\"")
        print("She tosses a pillow at you. \"No free room for you, but you're welcome to sleep in here for the evening.\" She waves as she slips back out the doors, and you begin to settle in for the night.")
        print("Morning arrives, and you awaken on the cold wood floor as a cockrel crows in the distance. You peer out and find that no one is in the inn.")
        choice = input("Finding that you've been left to your own deviced").upper()
    else:
        print("\nTEMPORARY TEXT: ")
        print("You die of indecision")

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

print("Thus ends Your Tale. We hoped you enjoyed.")