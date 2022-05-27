Time = 45
ship_health = 100
import random
import time
on_board = []
inventory = [
    "PIZZA",
    "PIZZA",
    "PIZZA",
    "OATS",
    ]
tips = 0
dis = 0
q = 0
w = 0
complete = 0

while Time > 0 and ship_health > 0 and complete == 0:

    def win():
        input(f"Congratulations! You have completed your deliveries, and earned {tips} space credits in tips.")
        exit()

    def splashscreen():

        print (r"""

        \______   \__|____________________    \______   \  | _____    ____   _____/  |_ 
        |     ___/  \___   /\___   /\__  \    |     ___/  | \__  \  /    \_/ __ \   __\
        |    |   |  |/    /  /    /  / __ \_  |    |   |  |__/ __ \|   |  \  ___/|  |  
        |____|   |__/_____ \/_____ \(____  /  |____|   |____(____  /___|  /\___  >__|  
                        \/      \/     \/                      \/     \/     \/                                  
                            
                            
                                !!!TYPE READY TO START!!!

                                            _,'/
                                        _.-''._:
                                ,-:`-.-'    .:.|
                                ;-.''       .::.|
                _..------.._  / (:.       .:::.|
            ,'.   .. . .  .`/  : :.     .::::.|
            ,'. .    .  .   ./    \ ::. .::::::.|
        ,'. .  .    .   . /      `.,,::::::::.;\
        /  .            . /       ,',';_::::::,:_:
        / . .  .   .      /      ,',','::`--'':;._;
        : .             . /     ,',',':::::::_:'_,'
        |..  .   .   .   /    ,',','::::::_:'_,'
        |.              /,-. /,',':::::_:'_,'
        | ..    .    . /) /-:/,'::::_:',-'
        : . .     .   // / ,'):::_:',' ;
        \ .   .     // /,' /,-.','  ./
        \ . .  `::./,// ,'' ,'   . /
        `. .   . `;;;,/_.'' . . ,'
            ,`. .   :;;' `:.  .  ,'
        /   `-._,'  ..  ` _.-'
        (     _,'``------'' 
        `--'' """)

    def death():

        print (r""""    __   ___   ____    ____  ____    ____  ______  __ __  _       ____  ______  ____  ___   ____   _____
                       /  ] /   \ |    \  /    ||    \  /    ||      ||  |  || |     /    ||      ||    |/   \ |    \ / ___/
                      /  / |     ||  _  ||   __||  D  )|  o  ||      ||  |  || |    |  o  ||      | |  ||     ||  _  (   \_ 
                     /  /  |  O  ||  |  ||  |  ||    / |     ||_|  |_||  |  || |___ |     ||_|  |_| |  ||  O  ||  |  |\__  |
                    /   \_ |     ||  |  ||  |_ ||    \ |  _  |  |  |  |  :  ||     ||  _  |  |  |   |  ||     ||  |  |/  \ |
                    \     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||     ||  |  |  |  |   |  ||     ||  |  |\    |
                     \____| \___/ |__|__||___,_||__|\_||__|__|  |__|   \__,_||_____||__|__|  |__|  |____|\___/ |__|__| \___|
                                             __ __   ___   __ __      ___    ____    ___  ___                               
                                            |  |  | /   \ |  |  |    |   \  |    |  /  _]|   \                              
                                            |  |  ||     ||  |  |    |    \  |  |  /  [_ |    \                             
                                            |  ~  ||  O  ||  |  |    |  D  | |  | |    _]|  D  |                            
                                            |___, ||     ||  :  |    |     | |  | |   [_ |     |                            
                                            |     ||     ||     |    |     | |  | |     ||     |                            
                                            |____/  \___/  \__,_|    |_____||____||_____||_____|     """)
        exit()
    
    def death_ast():
        global on_board
        input("You failed to make it through Asteroid Alley alive.")
        if "PAM" in on_board:
            input("To return to the beginning of Asteroid Alley, type PAPA in the start screen.")
        else:
            input("To return to the beginning of Asteroid Alley, type AAA in the start screen.")
        death()

    
    def emperor_pizza():
        global Time
        global tips
        global inventory
        global w
        input("The Emperor looks at you and beams a hideous grin. 'The classic combination!' he roars.")
        input("'Mmmmmmmmm smell that. Is there anything better?'")
        input("Everyone around him makes a deliberate point of looking at the ground and not answering that question.")
        input("'Thank you delivery driver!' the Emperor beams. 'You will be rewarded handsomely for this...'")
        emp_tip = 50 + Time
        tips = tips + emp_tip
        input(f"Clearly cheered by the success of his military campaign, and the prospect of devouring his foul concoction, he offers you {emp_tip} space credits.")
        a = 0
        while a == 0:
            print("1: 'That's very generous, sir, thank you.'")
            print("2: 'I don't want your blood money, you bulbous, cretinous tyrant.'")
            ans = input("What do you say to the emperor? ").strip()
            if ans == "1":
                input(f"You gratefully take the {emp_tip} space credits from the Emperor.")
                input("Never once turning your back on this dangerous brute, you reverse slowly out of the door.")
                a = 1
                complete = 1
                win()
            elif ans == "2":
                input("'Who dares talk to me like that?' the Emperor scoffs. 'I'll have your head, you lowly little peasant!'")
                input("The Emperor clicks his fingers and one of his lieutenants leaps into action.")
                input("Brandishing a laser sword, she removes your head from its usual resting spot atop your neck.")
                if w == 1:
                    input("Thankfully, your time-bending waif friend has been keeping an eye on you, clearly not trusting your general fitness for carrying out this delivery.")
                    input("Looking in through the window, she sighs, flourishes her hands, and returns you to a moment when you weren't doing something so stupid.")
                else:
                    ship_health = -1
                    a = 1
                    death()
            else:
                print("Best not keep the Emperor waiting. Type 1 or 2 and press ENTER.")

    def emperor():
        global Time
        global tips
        global inventory
        input("'Yeah about that...' you quiver. 'I may not actually have it on me...'")
        input("The Emperor turns red, then purple, then red once more, before settling on green again.")
        input("'But... but I can smell it all over you! Don't lie to me!'")
        input("'That's just the lingering stench of the toppings,' you plead. 'I don't think I'll ever get that off of me...'")
        input("'Well,' says the Emperor. 'That'll do, I guess.'")
        input("He opens up his cavernous maw, and swallows you whole in one big, tyrannical gulp.")
        input("You really shouldn't have shown up to the Emperor without a pizza...")
        input("To go back to your arrival in The Long Rim, type RIM in the start screen.")
        death()

    def walk():
        global Time
        global tips
        global inventory
        if "PIZZA" in inventory:
            input("You trudge the final stretch of your interminable first shift. The smell of the Emperor's pizza goes before you as you make your way to his base camp.")
            input("Half his Imperial Guards pass out from the odour, the other half recognise what you have with you and usher you through, with noses, or other olfactory organs, clamped shut.")
            input("'THAT SMELLS LIKE MY PIZZA!' booms a voice from within a makeshift cabin.")
            input("You walk into what appears to be the engine room of the military campaign.")
            input("Standing over a map of The Long Rim, is a humungous, globular creature.")
            input("Despite his full military uniform and handsome epaulettes, he has the unblemished, shiny green skin of a being that's not seen a whiff of frontline combat.")
            input("'Anchovies, mushroom, olives and pineapple, sir,' you croak, timidly.")
            emperor_pizza()
        else:
            input("You trudge reluctantly towards the inevitable wrath of the universe's most notorious tyrant.")
            input("A strange, morbid curiosity begins to compel you onward.")
            input("It's been such a peculiar first shift, who knows what's going to happen?")
            input("But you do sort of know...")
            input("You find a makeshift cabin. It appears to be the engine room of the Emperor's campaign.")
            input("Inside you see the menacing dictator giving orders, with several advisors gathered around a large map of The Long Rim.")
            input("He looks up and notices you. 'Ah the pizza is here!' he booms. 'Can this campaign get any better?")
            emperor()

    def outhouse():
        global Time
        global w
        input("You see a waiflike young creature in the corner. She's calmly twiddling in her fingers what looks at first like a coin.")
        input("On closer inspection, however, you see her hands are empty.")
        input("'Hi there,' you say politely. She looks up and smiles confidently. 'What are you in here for?' you ask her.")
        input("'Got caught dealing time, didn't I?' she replies.")
        input("'Time?'")
        input("'Time, yeah. Heard of it? Tick, tock, tick, tock. Utterly abundant yet no one can get enough of it...'")
        input("'I have a way of getting things. Seconds, minutes, hours... years and decades if the going's good.'")
        a = 0
        while a == 0:
            print("1: 'Is there any way I can get my hands on some more time?'")
            print("2: 'I have some time for you... if you're interested...'")
            print("3: 'This is all a bit weird for me...'")
            ans = input("What do you say to her? ").strip()
            if ans == "1":
                a = 1
                w += 1
                input("'Sure,' she says, looking around shiftily. 'For the right price...'")
                b = 0
                while b == 0:
                    ans = input("What do you offer her from your inventory? Type I to view your inventory. ").upper().strip()
                    if ans == "I":
                        for x in range(len(inventory)):
                            print(inventory[x])
                    elif ans in inventory:
                        if ans == "PIZZA":
                            input("The stench from the pizza is really beginning to seep through the lining of your bag.")
                            input("Though you know you have to get it to the Emperor, a part of you just wants it gone from your life.")
                            input("'How about a lovely pizza?' you ask, unconvincingly, releasing the foul odour as you remove it from your bag.")
                            input("'Great Omniscient Space Blob!' the stranger shrieks. 'Do you even know how bartering works?'")
                            c = 0
                            while c == 0:
                                ans = input("Seems she's not interested. Do you want to offer her anything else? Type YES or NO. ").upper().strip()
                                if ans == "YES":
                                    c = 1
                                elif ans == "NO":
                                    input("'What was it, the smell?' you ask sheepishly. 'It was the smell, wasn't it?'")
                                    input("'Look, I don't want to waste any more of your time,' you say, heading to the door.")
                                    input("There's probably a better way of offloading that pizza anyway...")
                                    Time -= 5
                                    input(f"Time remaining: {Time} space minutes.")
                                    c = 1
                                    b = 1
                                    walk()
                                else:
                                    print("Please type YES or NO and press ENTER.")
                                    time.sleep(1)
                        elif ans == "BANANA":
                            input("'I have this banana...' you say, as you offer her the madly bent foodstuff.")
                            input("'Why would I give you time for the sake of a piece of fr-'")
                            input("She interrupts herself, 'Is that really THAT bendy? Let me see...'")
                            input("You sense an opportunity. 'No.'")
                            input("'Oh go on, let me see it.'")
                            input("'For twent- for THIRTY space minutes,' you demand.")
                            input("'Fine, fine fine fine...' she mumbles, wafting her hand in your direction. 'Just take them. I need to process this...'")
                            input("Suddenly you feel, well, thirty space minutes younger!")
                            input("It's the last you may hear from your new friend for a while, however.")
                            input("As she stares, transfixed, at the incredible yellow freak of nature, you sneak out of the door for the last leg of your journey...")
                            Time += 30
                            input(f"You have {Time} space minutes remaining.")
                            inventory.remove("BANANA")
                            b = 1
                            walk()
                        elif ans == "RAY GUN":
                            input("'How about this fancy Ray Gun I won at the Intergalactic Challenge?'")
                            input("'At the what?'")
                            input("'The Intergalactic Challenge. The Grand Quizmaster gave this to me to fight off space pirates.'")
                            input("She takes it off you. 'This is a novelty toy from a kid's meal at SplungeBurgers...'")
                            input("You pause for a moment... 'It's a what?'")
                            input("'This is clearly a plastic toy! It has a sticker of Captain Space Tench on the side of it...'")
                            input("'Well it's a convincing replica,' you reply. 'So... how much for it?'")
                            input("'No way,' she snaps. 'Anything else?'")
                        elif ans == "OATS":
                            input("Well you haven't eaten your OAT DE CUISINE™ 'SLOPPIEST OATS' today yet, and it looks like you won't be able to now.")
                            input("Who knows? Maybe you can earn a bit of time for them...")
                            input("'How about these?' you ask, brandishing the packet proudly.")    
                            input("Her eyes widen as she notices them.")       
                            input("'Ugh, no!!' she cries. 'Zog, no! No, no, no, no, no...'")
                            input("'Alright, you've made your p-'")
                            input("'I didn't even think humans could safely digest those!' she continues. 'Tell me you've not been putting those in your body! We use them to kill space slugs!'")
                            input("'Look,' she says, 'I'll give you ten space minutes to get those things, and yourself, out of my sight.'")
                            d = 0
                            while d == 0:
                                print("1: Take the deal.")
                                print("2: Push the Oats.")
                                ans = input("What do you do? ").strip()
                                if ans == "1":
                                    input("'Ten space minutes for these things?! You've got yourself a deal!'")
                                    input("'Very well then,' she says, tossing one of those ephemeral coins your way. 'But you have to get out. Now.'")
                                    input("You lunge clumsily and ineffectively for the immaterial currency that you thought you saw heading your way. Is this a con?")
                                    input("Suddenly you feel... well, ten space minutes younger!")
                                    input("'That's amazing!' you call to her.")
                                    input("'THAT'S not part of the deal,' she retorts, waving in the direction of the door.")
                                    if "PIZZA" in inventory:
                                        input("You head out, reinvigorated, ready to deliver the Emperor his pizza.")
                                    else:
                                        input("You head out, feeling reinvigorated, ready to face the Emperor...")
                                    Time += 10
                                    input(f"You have {Time} space minutes remaining.")
                                    b = 1
                                    d = 1
                                    walk()
                                elif ans == "2":
                                    input("'They really are the Sloppiest Oats going,' you begin, cheekily.")
                                    input("'GET OUT!' she screams. 'GET OUT GET OUT GET OUT!!!'")
                                    input("She really does not like OAT DE CUISINE™ 'SLOPPIEST OATS'...")
                                    input("You may have missed out on ten space minutes, but it's probably time you headed to the Emperor.")
                                    input("Scurrying out of the door, you embark upon the final stretch of your final delivery...")
                                    Time -= 5
                                    b = 1
                                    d = 1
                                    input(f"You have {Time} space minutes remaining.")
                                    walk()
                                else:
                                    print("You really must make a decision. Type 1 or 2 and press ENTER.") 
                                    time.sleep(1) 
                        
                        else:
                            input("Not sure she'll want that...")
                    elif not ans:
                        print("Go on, offer her something...")
                        time.sleep(1)        
                    else:
                        print("You don't have that in your inventory...")
                        time.sleep(1)
            elif ans == "2":
                w += 1
                if Time <= 22:
                    input("I don't think you're in the position to be offering out your time...")
                else:
                    if "PIZZA" not in inventory:
                        input("'I have plenty of time,' you say to her, 'but it's currently worthless to me.'")
                        input("'I'm dead if I don't get the Emperor his pizza.'")
                        input("'And where is this pizza?' she asks you.")
                        input("How on earth do you explain what happened to the pizza? 'I lost it...'")
                        input("She smirks and shuffles eagerly over to you. 'Do you remember when you lost it?'")
                        input("'Yeah,' you reply, the memory fresh in your head. 'It was just before I landed here...'")
                        input("'That's great!' she cries, growing ever more animated. 'I reckon, with just 15 space minutes, I can get you that pizza back.'")
                        b = 0
                        while b == 0:
                            print("1: Eagerly agree.")
                            print("2: That's a bit steep. Reject the deal.")
                            ans = input("What do you do? ").strip()
                            if ans == "1":
                                a = 1
                                input("'How on earth could you manage that?' you ask her.")
                                input("'Everything exists in a moment,' she begins. 'And there exist infinite moments. A limitless supply of instances in which you can choose to shift to another moment.")
                                input("'In a moment, you can carelessly lose a murderous tyrant's pizza, or you can behave like a normal, responsible being...'")
                                input("'Infinite moments; infinite everything.'")
                                input("'Infinite everything, I was going to say that...' you add, unconvincingly.")
                                input("'I have the power to take you back to one such moment before you lost the pizza,' she continues.")
                                input("'If we can find a parallel moment in which you didn't lose the pizza, there's no reason we can't get THAT pizza and bring it back...'")
                                input("'Won't that, you know, mess up the spacetime continuum?' you ask, gesturing to everything with jazz hands.")
                                input("'I don't think you have spacetime to space worry about that...' she replies.")
                                input("You think for a brief instance. 'I guess I don't have a choice...'")
                                input("'Great!' she chirps, her mood clearly lightening at the prospect of this new adventure. 'Let's get going!'")
                                input("With a swish of her arm she envelops you in a temporal cloak, and, in a flash, you find yourself aboard your ship.")
                                input("Suddenly it all dawns on you. The swish of the arm, the borrowing pizza from another moment.")
                                input("You see the space pirates are looming menacingly once more, and you find yourself lingering over your cannon, holding the Emperor's pizza.")
                                input("Is that how gormless I look to everyone else? you wonder.")
                                input("'That's the moment,' your new friend whispers to you. 'Go go go...'")
                                input("You rush over to yourself and grab the malodorous pizza box. 'No time to explain,' you say to yourself, 'but... sorry?'")
                                input("Leaving Parallel You looking utterly bewildered, you rush back to the creature, who envelops you in time's cloak once more.")
                                input("In less than an instant you're back in the little outhouse, with the Emperor's pizza in your grateful grasp.")
                                input("'That was exhilarating,' you hiss, breathlessly. 'I mean, I really screwed whichever version of me that is, but wow!'")
                                input("'And now for my payment, please,' the waif says, flicking her hand extravagantly.")
                                Time -= 15
                                inventory.append("PIZZA")
                                input(f"You have {Time} space minutes remaining.")
                                input("Suddenly you feel... fifteen minutes older. Instantly, you become conscious of the urgency of your situation.")
                                input("Thank you so much! Now I need to get to the Emperor.")
                                input("She's already stopped paying attention to you, so you slip quietly out of the door. Foul pizza firmly in your grip, you head off to find the Emperor...")
                                b = 1
                                walk()
                            elif ans == "2":
                                a = 1
                                input("'This all sounds like pure bunkum to me,' you snap back. 'That pizza is gone. Ask the space pirate graveyard their thoughts on the matter.'")
                                input("'Ask the what?'")
                                input("'I don't have time for this!' you shout. 'I - literally - do not have time for this...'")
                                input("Having encountered one too many bewilderingly bizarre things for one Pizza Planet shift, you storm out of the outhouse and trudge off to face the Emperor.")
                                b = 1
                                Time -= 5
                                input(f"You have {Time} space minutes remaining.")
                                walk()
                            else:
                                print("This could be an important decision. Please type 1 or 2 and press ENTER.")
                                time.sleep(1)
                    else: 
                        input("'What can a bit of time get you round these parts then?' you ask her.")
                        input("She looks you up and down. 'With what you can afford,' she says, 'nothing...'")
                        input("You cower, visibly dejected by this putdown. She seems to notice.")
                        input("'Ah look, I'm sorry,' she says. 'It's just everyone is trying to get something for nothing nowadays.'")
                        input("'Tell you what I'll do. I can smell you have the Emperor's pizza on you. It's a fair walk over to where he's stationed.'")
                        input("'For two space minutes I'll get you to the moment you arrive. No boring walk. How's that?'")
                        input("Could be worse, you think. Time is money. And life and death... 'Sounds great,' you say.")
                        input("'Awesome! Hold on.' She whisks her arm at you, enveloping you in some sort of temporal cloak.")
                        Time -= 2
                        input(f"You have {Time} space minutes remaining.")
                        input("In a moment, or probably less, you're face to face with the Emperor.")
                        input("'Anchovies, mushroom, olives and pineapple,' you find yourself wheezing, although you don't know why.")
                        emperor_pizza()
            elif ans == "3":
                a = 1
                input("You've seen some strange things today, and quite enough for one Pizza Planet shift...") 
                input("Thanking her politely, you back away to the door.")
                input("She barely looks up from her twiddling and fidgeting. It's hard to be sure she ever even realised you were there.")
                if "PIZZA" in inventory:
                    input("You leave what turned out to be a rather underwhelming little building and head off to delivery the Emperor his pizza.")
                else:
                    input("Leaving that little disappointing foray behind, you trudge off to face the emperor, pizzaless and hopeless...")
                Time -= 5
                input(f"You have {Time} space minutes remaining.")
                walk()
            else:
                print("Please type 1, 2 or 3 and press ENTER.")
                time.sleep(1)


    def final_delivery():
        global Time
        global inventory
        if ship_health < 100:
            input("Weary and rather beaten up by your space pirate skirmish, you arrive at last in the volatile spacescape of The Long Rim.")
        else:
            input("With barely a scratched paint job to show for your run in with space pirates, you arrive at last in the volatile landscape of The Long Rim.")    
        input("The Emperor's Intergalactic War Corps is on campaign in the Gas Minnows, and the void around you is filled with the brilliant flashes of a thousand deadly laser cannons.")
        if "PIZZA" in inventory:
            input("Frozen for a moment by the senseless chaos being inflicted by the Emperor's war machine, you're suddenly snapped into life by a tremendous stench.")
            input("'Eugh... anchovies, mushrooms, olives and pineapple,' you recite from memory, recalling why you're there.")
            input("You have a pizza to deliver.")
        else:
            input("Stunned into motionless silence at the might of the Emperor's forces, you almost don't notice a familiar lingering smell...")
            input("Anchovies? Mushrooms? Olives? Pineapple? The Emperor's pizza!! How do you explain to the Emperor that you, but not you, stole it from yourself...")
            input("You see a minor planet, possibly Thalia, take the ferocious brunt of another laser barrage.")
            input("If this is what the Emperor does to people who do an impression of him on Blurnsday Night Live, just think how he'll react when his delivery driver turns up pizza-less...")
            input("'What the zog do I do now?' you whisper.")
        input("Entering the orbit of Möbius Alpha, where the Emperor's forces are based, you bring your ship to rest in the ample parking provided.")
        input("Disembarking from your vehicle, you're stopped in your tracks by a voice...")
        input("'Halt! Whose side are you on?' It's a captain of the Imperial Guard.")
        a = 0
        while a == 0:
            print("1: 'My loyalty lies with the Emperor,' you bark instantly, snapping into a clumsy salute.")
            print("2: 'I'm neutral, sir,' you quiver unconvincingly, 'I'm just here to deliver the Emperor his pizza.'")
            print("3: 'This is a Möbius planet, right?' you retort, flicking on some shades. 'Isn't it all one side?'")
            ans = input("What do you reply? ").strip()
            if ans == "1" or ans == "2" or ans == "3":
                a = 1
            else:
                print("Please type in 1, 2 or 3 and press ENTER.")
                time.sleep(1)
        if ans == "1":
            input("The captain looks momentarily impressed. 'I can tell from the flailing nature of your salute that you've done your time in the War Corps.'")
            input("'And I see you're now in the...' he squints at your uniform... 'Pizza Planet regiment? What brings you to The Long Rim?'")
            a = 0
            while a == 0:
                print("1: Wink.")
                print("2: Honk.")
                ans = input("What do you do? ").strip()
                if ans == "1" or ans == "2":
                    a = 1
                else:
                    print("I know it's a silly question, but please type 1 or 2:")
                    time.sleep(1)
            if ans == "1":
                input("Here goes nothing... 'I have a...' you wink, perhaps too slowly for him to be absolutely certain it wasn't sensual... 'pizza for the Emperor.'")
                input("His eyes narrow. 'Do you think I'm some sort of idiot?'")
                input("'No, not at all, I-'")
                input("'I know about Clandestine Culinary Correspondance!' he harrumphs. 'The top brass think I don't know what goes on, but I know...'")
                input("'ClanCulCors, that's what we used to call them during the Oort Wars! Oh yes I've seen my fair share of things you know.'")
                input("'I never for a second doubted it,' you reply, earnestly, beginning to feel sorry for this crusty old nobody.")
                input("'Well off you go then,' he barks. 'Best not keep the Emperor waiting...'")
                input("I should wink, apropos of essentially nothing, more often, you muse as you skip past the disgruntled captain.")
                input("You leave him chuntering away to himself about ClanCulCors, kicking the ground as he looks down at it.")
                if "PIZZA" in inventory:
                    a = 0
                    while a == 0:
                        print("1: Best utilise this run of good luck and get this disgusting pizza to the Emperor.")
                        print("2: Screw the Emperor, screw Pizza Planet, and screw not making decisions based off instinct alone. I'm checking out that outhouse.")
                        ans = input("What do you do? ").strip()
                        if ans == "1" or ans == "2":
                            a = 1
                        else:
                            print("Please type 1 or 2 and press ENTER.")
                    if ans == "1":
                        Time -= 3
                        input(f"Time remaining: {Time} space minutes.")
                        walk()
                    else:
                        input("The adrenaline coursing through your entire body, you bound over to a curious looking little outhouse.")
                        input("Finding it unlocked, you push the door open and slip through.")
                        input("Inside is a small, dingy room.")
                        outhouse()
                else:
                    a = 0
                    while a == 0:
                        input("However, you still have to face the Emperor, pizzaless and helpless...")
                        print("1: Or do you? Kill some time by checking out that outhouse.")
                        print("2: Time to face the music. Go and see the Emperor.")
                        ans = input("What do you do? ").strip()
                        if ans == "1":
                            input("Well, he can't kill me for not having his pizza AND being late, you think.")
                            input("Heading into the outhouse, you find yourself in a small dingy room.")
                            a = 1
                            outhouse()
                        elif ans == "2":
                            a = 1
                            walk()
                        else:
                            print("Please type 1 or 2 and press ENTER.")
                            time.sleep(2)
            else:
                input("'HONK!' Why the zog did I just do that?")
                input("The captain looks at you, his eyes slowly narrowing. Suddenly they burst open wide.")
                input("He sinks abruptly to one knee and begins to quiver and stammer.")
                input("'Commodore Goosen,' he whimpers, 'my sincerest of apologies. I didn't recognise you in your proletarian disguise...'")
                input("'...not to mention such hideous prosthetics!'")
                input("'Well, now, that's...' you begin, before realising how the events are unfurling before you.")
                input("'Please, Commodore, hurry on through,' the genuflecting simpleton murmurs to you, 'I'm sure the Emperor is eager to receive such esteemed company.'")
                input("Astonished that such a nonsensical outburst bore such sweet fruit, you slip past the captain.")
                input("His eyes never once raise to meet you as you leave. You are free to do as you please.")
                if "PIZZA" in inventory:
                    a = 0
                    while a == 0:
                        print("1: Hurry on to the Emperor and get this foul pizza delivered.")
                        print("2: Check out that random outhouse.")
                        ans = input("What do you do? ").strip()
                        if ans == "1" or ans == "2":
                            a = 1
                        else:
                            print("Please type 1 or 2 and press ENTER.")
                    if ans == "1":
                        walk()
                    else:
                        input("What an irresistible looking little outhouse, you think to yourself. I wonder what's inside.")
                        input("Heading over, you find the door unlocked, and creep into a small, dingy room.")
                        outhouse()
                else:
                    input("Well that was a stroke of luck. However the most powerful man in the known universe is expecting you to deliver a pizza that you recently jettisoned into the vaccuous void of deep space.")
                    a = 0
                    while a == 0:
                        print("1: Time to face the music. Go and see the emperor.")
                        print("2: Procrastinate. Maybe your doom can't reach you in that outhouse over there.")
                        ans = input("What do you do? ").strip()
                        if ans == "1" or ans == "2":
                            a = 1
                        else:
                            print("Please type 1 or 2 and press ENTER.")
                    if ans == "1":
                        print("Emperor.")
                    else:
                        input("'Well, death awaits me, that's for sure. I may as well look for it in that adorable looking outhouse.'")
                        input("You head over to the lonely looking little building and find the door unlocked.")
                        input("Slowly pushing it open, you look inside to find a small, dingy room.")
                        outhouse()
        elif ans == "2":
            b = input("'Neutral, huh?' he growls. 'Sounds like a passfiss to me. Where's this pizza then?' ").upper().strip()
            if "PIZZA" in inventory:
                input("No sooner have you opened your Pizza Planet delivery bag, than the pungent stench of the fishy, oily monstrosity begins to waft into the thin Möbius atmosphere.")
                input("'What in the solar system is that?!' howls the captain, his nostrils forever changed by the ordeal.")
                input("'That is clearly a biological weapon, the horror of which has never before been seen. You're under arrest.'")
                input("Handcuffing you roughly, he hauls you into a small outhouse.")
                input("'I'm calling for backup,' he snarls nasally, 'Don't move.'")
                input("He thrusts you into the middle of a dingy room. Gathering your bearings, you take stock of your surroundings.")
                outhouse()
            else:
                if "BANANA" in inventory and (b == "BENDY BANANA" or b == "BANANA"):
                    input("'Pizza... pizza...' Your mind races for a solution, but you can't stop thinking about how bendy that banana you have is.")
                    input("You reach for the miracle fruit and remove it from your pocket. Saying nothing, you hold it apologetically out and look at the captain with huge, longing eyes.")
                    input("The captain's face turns briefly from its default distrustful rage to something approaching pity, before snapping instinctively back again.")
                    input("'What in the noxious, green moon of Beatrice is this?!' he trumpets. 'You do know this isn't a p-'")
                    input("Mid-outburst, his eyes complete a double take of the bendy banana.")
                    input("Slowly, wordlessly, he reaches out and takes the absurd yellow freak from your hand.")
                    input("Cradling it in his palms like a fragile newborn chick, he stares transfixed. He says no more to you.")
                    input("He says no more to anyone...")
                    input("Assuming you're free to go, you leave him behind to his blissful, confused purgatory.")
                    inventory.remove("BANANA")
                    a = 0
                    while a == 0:
                        print("1: You're still pizzaless, so you may as well put off facing the wrath of the Emperor. Check out that outhouse.")
                        print("2: Best not be sans pizza AND late for the Emperor. Head to the delivery point.")
                        ans = input("What do you do? ").strip()
                        if ans == "1" or ans == "2":
                            a = 1
                        else:
                            print("Please type 1 or 2:")
                    if ans == "1":
                        input("You head over to a nondescript looking little outhouse. Finding it unlocked, you peer inside.")
                        input("It's a single, dingy room.")
                        outhouse()
                    else:
                        delivery()
                else:
                    input("'I'm afraid if I told you, you wouldn't believe me...' you offer tentatively.")
                    input("'What the zog sorta gibberish is that?!' he bursts. 'Get your insurrectionist butt over here!'")
                    input("He grasps you aggressively by the collar of your Pizza Planet uniform and bundles you into a small outhouse.")
                    input("Muttering under his breath about peace-loving space hippies, he leaves you in a dingy little room...")
                    outhouse()

        else:
            input("'So we got another comedian, do we? Ain't no one told ya what happens to comedians in The Long Rim nowadays?'")
            input("Not for the first time in your life, or indeed today, you find yourself being roughly handled by a guy you've known for less than a minute.")
            input("He grabs you firmly by the collar of your new Planet Pizza uniform and hoicks you into a small outhouse.")
            input("The captain throws you unceremoniously down in the middle of a dingy room. 'You can stay in here while I finish my lookout. Maybe you can think of some more jokes.'")
            input("Dusting yourself off, you look around.")
            outhouse()

    
    def pirates():
        global Time
        global ship_health
        global q

        cannon_acc = [
            "HIT",
            "HIT",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
        ]

        gun_acc = [
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
            "MISS",
        ]


        dilma_acc = [
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "MISS",
        ]

        pir_acc = [
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "HIT",
            "MISS",
            "MISS",
        ]

        pir_acc_dilma = [
            "L",
            "M",
            "R",
        ]

        miss = [
            "Not even close...",
            "Missed!",
            "Oh dear... you missed...",
            "Miss!",
            "Swing and a miss!",
            "Nope!",
            "Close, but... not that close...",
            "You missed... dreadful...",
            "Miss! A near miss, but a miss nonetheless...",
            "Miss! I think you just destroyed Alderaan...",
            "Miss! Who taught you how to shoot?!",
        ]

        hit = [
            "Oh my god you hit them!!",
            "Hit! Beginner's luck, but they all count...",
            "BOOM! You just closed your eyes and hoped on that one, huh?",
            "Got 'em. You lucky thing...",
            "Winged 'em. Not a bullseye, but at least you got it on the board...",
        ]

        dilma_hit = [
            "Bullseye! Ace shooting, Dilma.",
            "Hit! \'Eat Dilma, space rats!\' \'Dilma, please...\'",
            "Bingo! That's what you get when you mess with Dilma Fuchs...",
            "What a hit! That's a Dilma Special!",
            "BOOM! Dilma's not messing about...",
            "Direct hit! Right where it hurts...",
            "POW! Right in the poop deck.",
            "Hit! \'Oh baby, that's how Dilma do!\'",
            "\'Pew pew pewwwww!\' \'Dilma, didn't we say no laser noises?\'"
        ]

        dilma_fire = [
            "\'Fire at will!\' \'Wouldn't you rather I fired at the pirates?\'",
            "Fire!",
            "FIIIIIRRRREEEEEE!",
            "Ready? Aim. FIRE!"
        ]

        fire = [
            "Fire at will!",
            "Fire!",
            "FIIIIIRRRREEEEEE!",
            "Ready? Aim. FIRE!",
        ]

        fire_pam = [
            "As tempting at it is to jettison PAM into the inky black of deep space...",
            "I don't know what they taught you at your last pizza delivery job, but here at Pizza Planet we don't use people as weapons.",
        ]

        no = [
            "Nice try,",
            "I like the way you think,",
            "Good thinking,",
            "Nothing wrong with thinking outside the box,",
            "Ha! I wish,",
        ]

        pirates_fire = [
            "Uh oh. The pirates are taking aim.",
            "'Get ready, landlubber!' the pirates shout, 'This one's got your name on it...'",
            "Look out! The pirates are firing!",
            "'You'll be spending eternity in Space Davy Jones' Space Locker,' the pirates taunt, as they load their cannons...",
            "'This is how we do it on the highest of seas,' the pirates yell at you, aiming their laser cannon right at you.",
            "Look out! That space pirate cannon is zeroing in on you...",
            "Here comes a blast from the space pirates' cannon...",
            "The space pirates are taking aim... I hope you fixed that deflector shield... ",
            "'Send our regards to the space kraken,' the pirates shout mockingly, as they load their cannon.",
            "'Arrrrrrrrr,' comes a cry. The space pirates are ready to fire.",
        ]

        pirates_hit = [
            "'Arrrrrrrrrrr! A direct hit!'",
            "BOOM! That one got you!",
            "BANG! Do try and dodge them...",
            "You've been hit!",
            "'Take that landlubber!' The pirates' cannon fire makes contact with your hull.",
            "CRASH! A cannon blast shakes your ship.",
            "Hit! Someone check on the pizza...",
            "You got hit! That'll take more than a lick of paint...",
            "Direct hit! The boss will take that out of your wages...",
        ]

        pirates_miss = [
            "Miss! You lucky thing...",
            "Missed! You should buy a lottery ticket...",
            "Nowhere near! I think these space pirates have been on the space rum.",
            "Not even close! Unless they were trying to hit that random bit of space?",
            "They missed! Huzzah!",
            "What a miss! Or are they just toying with you?",
            "They missed you! Phewwwwww...",
            "They missed! Can you believe it?!",
        ]

        dodge = [
            "Miss! Great dodging!",
            "Missed! Good swerving...",
            "The shot flies right past you! Superb driving!",
            "Nice dodge! That one missed you by miles!",
            "Swerved out of the way! Well done!",
            "Dodged it. Great ducking and diving...",
            "They missed! That was all you, baby!",
            "Air shot! Nice dodge!",
            "What a miss! Or what a dodge?",
            "Great swerve. Excellent skills.",
            "Missed. Next.",
        ]

        pirates = 100

        a = 0

        b = 1

        t = 0

        input("Tapping the coordinates into your onboard computer, you make your way towards The Long Rim, where the Emperor is awaiting his pizza.")
        if "BANANA" in inventory:
            input("As your mind clicks into the monotony of the journey, you begin to think about the bendy banana you won.")
            input("For some reason, you just can't shift it from your mind.")
            input("All bananas bend, but this one BENDS.")
            input("You can't quite put into words the nature or strength of your feelings towards it.")
            input("Is it anger? Admiration? Terror?")
            input("It's the most bewildering piece of fruit you've ever come across...")
            input("With your thoughts fully immersed in this yellow wormhole, you don't spot the menacing vessel approaching ever closer.")
        else:
            input("You try to switch your brain off and find a few moments of peace in this crazy shift.")
            input("However the fishy, abominable stench from the Emperor's pizza is beginning to fill the ship.")
            input("'I need to double bag that thing,' you mutter.")
            input("Abandoning your position at the wheel, you fumble around for something to block out the horrific pong.")
            input("With no one at the wheel, you begin to drift ominously towards a rather menacing looking vessel.")
        input("Suddenly you notice it. Space pirates. The most notorious, pizza-loving bandits spacetime has ever seen.")
        input("And they're gaining on you fast...")
        input("'Hand us over your pizza,' they call over to you, 'and we'll only kill you once, arrrrrrrrr.'")
        while a == 0:
            if input("Looks like a skirmish with pizza-mad space pirates is now unavoidable. ").lower().strip() == "skip": 
                a = 1
            else:
                if input("Steeling yourself for combat, you mentally remind yourself of the rules of engagement. ").lower().strip() == "skip":
                    a = 1
                else:
                    if input("Type 'skip' if you don't wish to be privy to your own inner thoughts concerning the rules. ").lower().strip() == "skip":
                        a = 1
                    else:
                        input("When it's your turn to fire, type in what you wish to shoot at your enemy.")
                        input("Your delivery ship is inexplicably fitted with a CANNON.")
                        input("This big lasery bad egg will inflict a lot of damage, but can be unreliable in inexperienced hands.")
                        input("Your ship's GUN is more accurate for a novice, but you'll need more hits to take the pirates down.")
                    if "DILMA FUCHS" not in on_board:
                        input("Good luck, lone rider. You're going to need it.")
                    else:
                        input("'I don't like the look of this, Dilma,' you whisper.")
                        input("'Good job you have the sharpest shooter in all of spacetime on board,' she replies.")
                        if "PAM" in on_board:
                            input("You look over at the tin idiot in the corner of the ship, repeatedly banging into the wall like a broken autovac.")
                            input("'...PAM?'")
                            input("'No, not PAM...' Dilma replies, '...me.'")
                        else:
                            input("'Huh?'")
                        input("'Didn't I mention that I spent fourteen years in the Intergalactic War Corps?'")
                        input("'If you did, Dilma,' you reply, 'I wasn't listening.'")
                        input("'I'll tell you about it later,' she says, 'For now, I'll operate the weapons - I'm deadly accurate...'")
                        input("'...and you just concentrate on flying the ship. You should be able to dodge the pirates' weapons as long as you keep moving.'")
                    a = 1
        input("These pirates are uncharacteristically polite and are allowing you to fire first.")
        input("Remember, when you hear the command, type in what you want to fire at those pizza-stealing bilge rats.")
        while pirates > 0 and ship_health > 0:
            a = 0
            t += 2
            while a == 0:
                f = input(f"{random.choice(fire)} ").upper().strip()
                if f == "CANNON":
                    if "DILMA FUCHS" in on_board:
                        f = random.choice(dilma_acc)
                    else: 
                        f = random.choice(cannon_acc)
                    if f == "HIT":
                        if "DILMA FUCHS" in on_board:
                            input(random.choice(dilma_hit))
                        else:
                            input(random.choice(hit))
                        pirates -= 30
                        if pirates < 0:
                            pirates = 0
                        input(f"Space Pirate ship health = {pirates}")
                        if pirates <= 0:
                            a = 2
                        else:
                            a = 1
                    else:
                        input(random.choice(miss))
                        a = 1
                elif f == "GUN":
                    if "DILMA FUCHS" in on_board:
                        f = random.choice(dilma_acc)
                    else:
                        f = random.choice(gun_acc)
                    if f == "HIT":
                        if "DILMA FUCHS" in on_board:
                            input(random.choice(dilma_hit))
                        else:
                            input(random.choice(hit))
                        pirates -= 15
                        if pirates < 0:
                            pirates = 0
                        input(f"Space Pirate ship health = {pirates}")
                        if pirates <= 0:
                            a = 2
                        else:
                            a = 1
                    else:
                        input(random.choice(miss))
                        a = 1
                elif f in on_board or f == "DILMA":
                    if f == "PAM":
                        input(random.choice(fire_pam))
                    elif f == "DILMA" or "DILMA FUCHS":
                        if "DILMA FUCHS" in on_board:
                            input("Dilma?! Dilma who's operating your weapons Dilma?!")
                        else:
                            input("Wasn't Dilma that person you refused entry onto your ship?")    
                elif f in inventory:
                    if f == "PIZZA":
                        input("\'You want my pizza so much?! Here, take it!!!\'")
                        input("As a rush of blood shoots towards your head, you grab the Emperor's pizza and attempt to load it into your cannon.")
                        input("Suddenly a familiar pair of hands wrench it from your grasp.")
                        input("You look up, and see yourself looking back at you.")
                        input("'No time to explain,' the doppelgänger says, 'but... sorry?'")
                        input("You stand, dumbfounded, as the twin you never knew you had takes the pizza and runs over to a slight, shadowy figure in the corner.")
                        input("With a flick of an arm, the creature disappears the two of them into nothingnesss...")
                        input("'What the...'")
                        a = 1
                        inventory.remove("PIZZA")
                    elif f == "BANANA":
                        if "BANANA" in inventory:
                            input("\'I'm sorry, I cannot concentrate on this fight with this STUPID BANANA in the corner of my eye...\'")
                            input("In a fit of confused rage, you load the bendy banana into your cannon and launch it into the clear black chasm.")
                            input("The pirates laugh me-'eartily at your pathetic combat skills, and aim their cannon for the next strike.")
                            input("All of a sudden, one of them spots the unfathomably wonky fruit...")
                            input("'Shiver me timbers!' he cries, his eyes frozen in fear.")
                            input("'Shiver YOUR timbers?!' another one shouts, having also noticed the banana. 'Shiver MY timbers!!'")
                            input("'SHIVER ALL OF OUR TIMBERS!!' a third one shouts. 'Let's get the hell away from that cursed thing!'")
                            input("Scrabbling past each other, they rush to their positions.")
                            input("'Seatbelts on, lads!' the captain cries, 'I'm engaging warp speed!'")
                            input("Doing a quick U-ee, the pirates shout some obscenities back at you, or back at the banana maybe, and begin to heave ho out of there.")
                            input("Perhaps it was the sudden acceleration, perhaps it was the anarchic spaceship maintenance culture you'd expect from a group of intergalactic bandits...")
                            input("Perhaps it just wasnt't their day. Whatever it was, as they began their hasty escape their thrusters sputtered and burst into flames...")
                            inventory.remove("BANANA")
                            pirates -= 100
                            a = 2
                        else:
                            input("You don't have a banana on your ship...")
                    elif f == "RAY GUN":
                        if "DILMA FUCHS" in on_board:
                            input("'Hey ace,' Dilma calls to you, 'Why don't we try firing that new toy you just won at them?'")
                            input("'Great idea Dilma!' Grabbing the Ray Gun you won at the quiz, you rush over to where Dilma is.") 
                            input("You stuff the Ray Gun into the cannon, as Dilma Fuchs watches on, horrified.")
                            input("'Let's see what this baby can do!' you quip.") 
                            input("'That's not what I m-' Dilma's protestations are cut short as you launch the Ray Gun into the murky night.")
                            input("It tumbles, lamely, through the jet black nothingness, before it eventually CLANKS against the enemy ship.")
                            input("'Any more of our belongings you'd like to launch into space?!' Dilma yells.")
                            inventory.remove("RAY GUN")  
                        else:
                            input("Suddenly, a brain wave hits you!")
                            input("You remember what the quizmaster said about the Ray Gun you won from him.")
                            input("Grabbing it, you whisper to your new toy, 'Let's see what you can do...'")
                            input("You stuff it into the cannon, and launch it into the void.")
                            input("It tumbles, lamely, through the jet black nothingness, before it eventually CLANKS against the enemy ship.")
                            input("'What a piece of junk,' you say to yourself, and try to think of other ideas...")
                            inventory.remove("RAY GUN")
                        pirates -= 1
                        input(f"Space Pirate ship health = {pirates}")
                        a = 1
                    elif f == "OATS":
                        if "OATS" in inventory:
                            input("'Well, I'm never going to eat these anyway...'")
                            input("Grabbing OAT DE CUISINE™'s premium (and sloppiest) brand of morning space sustenance, you empty it into your cannon.")
                            input("'Eat oats, scrotes!' you shout, embarrassingly, and launch the gloopy mess at your foe.")
                            input("Rather surprisingly it holds its viscous form remarkably well in the vacuum of space.")
                            input("If anything it just grows, in size and in sloppiness, as it makes its slow way piratewards.")
                            input("By the time it reaches its horrified target, it has formed an enormous, gloopy mass that envelops the space pirate spaceship.")
                            input("You hear some muffled screams from within the oaty tomb, and the ship spins helplessly out of control, eventually crashing into the long-abandoned Planet Earth.")
                            inventory.remove("OATS")
                            pirates -= 100
                            a = 2
                        else:
                            input("Pretty sure you wolfed your OAT DE CUISINE™ 'SLOPPIEST OATS' already...")
                    else:
                        input("I don't think that will work...")    
                else:
                    if not f:
                        print("You have to fire something. Please type in what you wish to fire...")
                    else:
                        input(f"{random.choice(no)} but you don't have one of them on board.")    
            while a == 1:
                input(random.choice(pirates_fire))
                if "DILMA FUCHS" in on_board:
                    if b == 1:
                        input("With Dilma on weapons duty, you can concentrate on flying the ship.")
                        input("When the pirates fire, you can type L to dodge left, R to dodge right, and M to stay in the middle.")
                        input("Good luck!")
                        b += 1
                    else:
                        p = random.choice(pir_acc_dilma)
                        d = input("Here it comes! Type L, M or R to dodge. ").upper().strip()
                        if d == "L" or d == "M" or d == "R":
                            if d == p:
                                input(random.choice(pirates_hit))
                                ship_health -= 20
                                if ship_health < 0:
                                    ship_health = 0
                                    a = 2
                                input(f"Ship's health = {ship_health}")
                                if ship_health > 0:
                                    input("Your turn.")
                                    a = 0
                                else:
                                    a = 2
                            else:
                                input(random.choice(dodge))
                                input("Your turn.")
                                a = 0
                        else:
                            print("Please choose L, M or R.")
                else:
                    if random.choice(pir_acc) == "HIT":
                        input(random.choice(pirates_hit))
                        ship_health -= 20
                        if ship_health < 0:
                            ship_health = 0
                            a = 2
                        input(f"Ship's health = {ship_health}")
                        if ship_health > 0:
                            input("Your turn.")
                            a = 0
                        else:
                            a = 2
                    else:
                        input(random.choice(pirates_miss))
                        input("Your turn.")
                        a = 0
        if ship_health <= 0:
            input("You have been defeated by the space pirates!")
            input("They board your defenceless ship and pillage every last morsel of pizza.")
            if "BANANA" in inventory:
                input("They leave hastily when they see the bendy banana though...")
            else:
                input("They tie you up and leave you to your fate.")
            input("With your ship having taken too much damage, you sit and wait for the inevitable massive explosion...")
            if "PAM" in on_board and "DILMA FUCHS" in on_board:
                input("To return to the beginning of the space pirate battle, type in PUMP at the start screen.")
            elif "PAM" in on_board and "DILMA FUCHS" not in on_board:
                input("To return to the beginning of the space pirate battle, type in POP at the start screen.")
            elif "PAM" not in on_board and "DILMA FUCHS" in on_board:
                input("To return to the beginning of the space pirate battle, type in DUMP at the start screen.")
            else:
                input("To return to the beginning of the space pirate battle, type in ARR at the start screen.")

            death()
        else:
            input("You have defeated the space pirates!")
            input("Their space pirate ship explodes in a burst of metal, rum and leftover pizza.")
            Time = Time - t 
            print(f"Ship's health = {ship_health}")
            print(f"Time = {Time}")
            final_delivery()

    def delivery2_leave():
        input ("You start breathing again normally, after a few moments, at least. You've survived The Karenkala, 'Nothing can hurt me, now!' you think, with renewed courage and confidence.")
        input ("Hopefully Colin can deal with the inevitable phonecall coming his way. Hell, he probably deserves it.")
        input ("You pat the final pizza bag to reassure yourself that this shift is nearly over, and then you set course for The Long Rim.")
        pirates()

    def karen_police():
        input ("The woman whips out her communicator and rapidly presses a few digits.")
        input ("'Hello?!?! Please help me, I need help, this pizza guy is trying to rob me! He's also really rude!'")
        input ("Your pulse starts pounding - this could be a very sticky situation.")
        input ("Karenkala smiles smugly at you as the sound of Galactic Police klaxons pierce the peace of the quiet neigbourhood.")

        a=0
        while a==0:
            print ("1: Throw the pizza on the ground and get the heck out of there.")
            print ("2: Stay and try to reason with the cops.")
            karen_police=(input("What do you do? "))
            if karen_police==("1"):
                print ("You throw the pizza at the ground in front of the now incoherently smugly angry woman and dive back into your ship, keying in the emergency orbital insertion code. The engines roar to life and you're off to the safety of the incomprehensible void.")
                a=1
                delivery2_leave
            if karen_police==("2"):
                input ("Five squad cars roll up; Karenkala starts crying and shouting about how much danger she's in.")
                input ("An officer gets out of one of the cars, and his eyes widen in disbelief as he spots the pizza box in your hands.")
                input ("'It's a bomb!' There are a few short sharp snaps as lasers pierce the air as the police open fire on you.")
                a=1
                death()

    def delivery2intro():
        global Time
        global inventory
        inventory.remove("PIZZA")
        input ("Your ship exits its skipdrive routine a few clicks above Bromelian 7. The autopilot has already keyed into Karenkala's house, the ion drive fires up and you roar towards the surface.")
        input ("Your communicator starts buzzing as you pass over a suburban zone - your WorkFriend™ flashes up with “Karenkala”.")
        input ("A bobcut appears on the display. 'WILL YOU KEEP IT DOWN! Oh my GODDDD, I don't care if you're trying to do your job, you're really louuuud!' The feed cuts out very suddenly. You are filled with a sense of almost incomparable dread.")
        input ("You pull up to the delivery address, a pastel pink house in an idyllic neighbourhood. The door opens and a furious looking woman stomps out, heading right for you. She's wearing expensive looking sportswear and has a pair of winged glasses on. You've encountered a service worker's worst nightmare.")
        a=0
        while a==0:
            print("1: Try to appease the Karenkala.")
            print("2: Open the window, throw the pizza at her, and run.")
            print("3: Argue back.")
            karenintro=(input("What do you do? "))
            if karenintro==("1"):
                input ("The woman screeches 'I should call the police! You're very loud, and very, very rude! Where's my pizza? I want a discount......")
                input (f"She continues like this for a while. You have {Time} space minutes remaining.")
                input ("This is going nowhere... you hit the autopilot and head into orbit.")
                Time -=5
                a=1
                delivery2_leave()
            elif karenintro==("2"):
                input ("You throw the pizza at her through the window; you crank the handle to wind it up as fast as you can as you ears are assaulted by a cacophony of incoherent complaining. You key The Long Rim into your autopilot and desperately smash the button until the engines kick in.")
                input ("Your ship's computer automatically detects an emergency and performs an escape burn, painfully launching the ship towards orbit.")
                a=1
                Time -=1
                delivery2_leave()
            elif karenintro==("3"):
                Time -=7
                input ("You step out of your craft, defensively clasping your delivery bag in front of your chest. 'Ma'am, I'm just trying to do my job, please just take the pizza.")
                input ("'Oh yeah? Well I'm calling the police.'")
                a=1
                karen_police()
            else:
                print ("Please choose 1, 2, or 3.")

    def quiz():
        print('''\
        ad88888ba  88888888ba     db        ,ad8888ba,  88888888888         ,ad8888ba,      88        88    88    888888888888  
        d8"     "8b 88      "8b   d88b      d8"'    `"8b 88                 d8"'    `"8b     88        88    88             ,88  
        Y8,         88      ,8P  d8'`8b    d8'           88                d8'        `8b    88        88    88           ,88"   
        `Y8aaaaa,   88aaaaaa8P' d8'  `8b   88            88aaaaa           88          88    88        88    88         ,88"     
        `"""""8b, 88""""""'  d8YaaaaY8b  88            88"""""           88          88    88        88    88       ,88"       
                `8b 88        d8""""""""8b Y8,           88                Y8,    "88,,8P    88        88    88     ,88"         
        Y8a     a8P 88       d8'        `8b Y8a.    .a8P 88                 Y8a.    Y88P     Y8a.    .a8P    88    88"           
        "Y88888P"  88      d8'          `8b `"Y8888Y"'  88888888888         `"Y8888Y"Y8a     `"Y8888Y"'     88    888888888888                                             
                
            ''')
        print('''\
                            *         .--.
                                        / /  `
                    +               | |
                            '         \ \__,
                        *          +   '--'  *
                            +   /\
                +              .'  '.   *
                        *      /======\      +
                            ;:.  _   ;
                            |:. (_)  |
                            |:.  _   |
                    +         |:. (_)  |          *
                            ;:.      ;
                            .' \:.    / `.
                        ( .-'':._.'`-. )
            
                        _..--"""````"""--.._
                _.-'``                    ``'-._
                -'                                '-
        ''')
        #QUIZ INTRODUCTION
        input ("You decide to grab some repairs at the local service station on the way to the next delivery. You pull up outside an asteroid speckled with tiny little structures that twinkle against the black of the void. A big sign marked 'Service and MOT' lazily rotates into view. You put your foot down and accelerate towards the service bay.")
        input ("Docking clamps extend and lock your ship into place - there's an incoming call and your WorkFriend™ communicator automatically plays a promotional message... 'Thank you for calling a Planet Pizza representative! We'll deliver in 45 minutes, or else! Please stand by!'")
        print("\n")
        input ("An oblong face with 3 eyes on gangly antennae appears on your communicator's screen. 'Welcome to Intergalactic Services! Due to a new educational subsidy, in lieu of payment, we can offer repairs and rewards if you prove your knowledge. All Hail the Emperor!'")
        print("\n")
        input ("The alien pulls out a clipboard, somehow manages to squeeze its eyes between a pair of glasses, and intones in a voice soaked in gravitas: 'Do you have what it takes to beat the Intergalactic Challenge?'")
        print("\n")
        input("'Welcome to the Intergalactic Challenge! Here you will have an opportunity to prove yourself and earn some handy rewards. You may call me the Grand Quizmaster! You have 5 rounds to try and impress me. I have many prizes to be won and repairs to be granted! I also need the room... so... let's not delay any further! Do you have what it takes?!' Press ENTER to commence the Intergalactic Challenge.")
        print("\n")
        input("HERE WE GO!!!")


        def function_1():
            global tips
            global ship_health
            answer1 = input("The Hawaiian pizza (ham & pinapple) was invented where?  \na. Italy \nb. Canada \nc. Planet Pizza's basement \nAnswer: ").lower().strip()
            if answer1 == "b" or answer1 == "canada":
                ship_health+= 1
                tips += 2
                print("'Correct! Great answer! Congratulations! You have just won this, uh, disturbingly bendy banana! Please, just take it. It intimidates me...'")
                inventory.append("BANANA")
                input("Banana added to inventory")
                for x in range(len(inventory)):
                    print(inventory[x])
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print('''\
                    
                    ".              ,#  
                    \ `-._____,-'=/
                    ____`._ ----- _,'_____
                        `-----'

                    ''')
                print("\n")
            elif answer1 == "a" or answer1 == "italy" or answer1 == "c" or answer1 == "planet pizza's basement":
                ship_health-= 1
                tips -= 1
                print("'Incorrect! The answer is Canada. I am not impressed...'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer1 != "b" or answer1 != "canada":
                    print("'Stop messing around! I don't have time to waste, and neither do you, delivery driver!'") 
                    time.sleep(2)
                    function_1()

        function_1()

        def function_2():
            global tips
            global ship_health
            answer2 = input("What is the smallest planet in the human solar system? \na. Uranus \nb. Pluto \nc. Mercury \nAnswer: ").lower().strip()
            if answer2 == "c" or answer2 == "mercury":
                ship_health+= 1
                tips += 2
                print("'CORRECT and congratulations! Have some rewards.'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer2 == "a" or answer2 == "uranus" or answer2 == "b" or answer2 == "pluto":
                ship_health-= 5
                tips -= 5
                print("'INCORRECT! The answer is Mercury. Seriously?! How can a human not know that?!'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer2 != "c" or answer2 != "mercury":
                print("'Stop messing around! Hurry up and pick an answer... I have work to do!'") 
                time.sleep(2)
                function_2()
        function_2()

        def function_3():
            global tips
            global ship_health
            answer3 = input("Where was the modern Pizza created? \na. Italy \nb. New York \nc. Pizza Planet \nAnswer: ").lower().strip()
            if answer3 == "a" or answer3 == "italy":
                ship_health+= 10
                tips += 10
                print("'CORRECT! Dude, you are on fire! Quite literally... let me put that out for you. Here's some extra repairs and a cash bonus!'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer3 == "b" or answer3 == "new york" or answer3 == "c" or answer3 == "pizza planet":
                ship_health-= 1
                tips -= 5
                print("'INCORRECT! The answer is Italy.'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer3 != "a" or answer1 != "italy":
                    print("'Seriously... it's a multiple choice quiz... this shouldn't be that difficult!'") 
                    time.sleep(2)
                    function_3()
        function_3()

        def function_4():
            global tips
            global ship_health
            answer4 = input("How many planets are there in the human solar system? \na. Eight \nb. Seven \nc. Forty \nAnswer: ").lower().strip()
            if answer4 == "a" or answer4 == "eight":
                ship_health+= 1
                tips += 10
                print("'Well done! You answered correctly, here's a cash bonus!'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer4 == "b" or answer4 == "seven" or answer4 == "c" or answer4 == "forty":
                ship_health-= 1
                tips -= 5
                print("'Incorrect! The answer is eight. No way are you getting a tip for that one, in fact you can give me something back for that poor effort!'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer4 != "a" or answer4 != "eight":
                print("'Oh come on! I REALLY don't have time to waste!'") 
                time.sleep(2)
                function_4()
        function_4()

        def function_5():
            global tips
            global ship_health
            answer5 = input("When was the first Pizza delivered into space? \na. 2034 \nb. 1993 \nc. 2001 \nAnswer: ").lower().strip()
            if answer5 == "c" or answer5 == "2001":
                ship_health+= 1
                tips += 2
                print("'Correct! You really did your research for this job! I'm impressed with that answer, so as a reward I'm going to give you this Ray Gun. I hear there are pirates out there with a rabid taste for pizza. This will be more use for you than me!'")
                inventory.append("RAY GUN")
                input("Ray Gun added to inventory.")
                for x in range(len(inventory)):
                    print(inventory[x])
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print('''\
                    
                            _____
                    .':::::::'.
            ___ /:::::::::::\____ _            _.''_
            /||   ||`.______.-`||   | |\_\\\\____/_ _.-'\\\\
        .|-| ||===||           ||===| ||_||||____|_| .-'|||||
        '|-| ||===||===========||===| ||_||||____|_|`-._|||||
            \||___||___________||___|_|/ ////       `-._////
            )      )  _____  (
            /`--.._/ .'| (  '. \
            )     ( (  './    ) )
        /`--.___\ '._____.' /
        )       /'._______.' 
        /`--..__/
        )       )
        /`--..__/
        (        )
        `------'

                    ''')
                print("\n")
            elif answer5 == "a" or answer5 == "2034" or answer5 == "b" or answer5 == "1993":
                ship_health-= 1
                tips -= 5
                print("'Unlucky pizza man! the answer is 2001. You're an insult to your species AND your profession.'")
                input(f"Ship health: {ship_health}")
                input(f"Tips: {tips}")
                print("\n")
            elif answer5 != "c" or answer5 != "2001":
                    print("'Thank the Emperor! This is the last question!' The Quizmaster is basically screaming at this point. 'Just pick a, b or c and get this over with!'") 
                    time.sleep(2)
                    function_5()
        function_5()

        print("\n")
        print("'Well done on completing the quiz! It took you long enough.' The Grand Quizmaster rolls all 3 of his eyes. 'Now take your loot and get out of my sight. I've got work to do!'")
        print("\n")
        input("You walk back to the ship slightly dazed and confused. You are stuggling to comprehend just how weird the Grand Quizmaster was.")
        input("No time to dwell on that, though. Now you must head to the second delivery.")
        delivery2intro()

    

    def leave_delivery_one(): 
        global on_board
        global Time
        global tips
        global q
        if "DILMA FUCHS" in on_board:
            input ("You get into your ride and Dilma hops into the back seat. 'Name's Dilma, Dilma Fuchs, by the way.' She throws an empty pizza box over her face and promptly starts snoring.")
            input ("You sit down in the driver's seat and smash the take-off button. Putting your feet up on the dash as the lift-off sequence starts, you stream up into the sky.")
        else: 
            input ("You hop back into your ship and smash the take-off button. Putting your feet up on the dash as the lift-off sequence starts, you stream up into the sky.")
        input (f"You have {tips} space credits in tips.")
        input (f"You have {Time} space minutes left.")
        input ("Your next delivery is to Karenkala. Your nav screen tells you that there is a service station ahead.")
        c = 0
        while c == 0:
            print("1: Go straight to the delivery.")
            print("2: Visit the service station for repairs.")
            ans = input("What do you do? ").strip()
            if ans == "1":
                c = 1
                delivery2intro()
            elif ans == "2":
                c = 1
                q += 1
                quiz()
            else:
                print("Please type 1 or 2 and press ENTER.")


    def dilma_convo():
        global on_board
        global tips
        global Time 
        Time -= 2
        input ("Dilma looks over at you with two blood shot eyes 'Humie? What is this, the 3050's?. Ugh.' She stands up and shoves Mr. Galgogagoa aside.") 
        input ("'Hey, is that your ship? Can I get a lift? Anywhere but here? I'll give you some fuel money'") 
        input ("Mr. Galgogagoa sputters for a moment, looks like he's about to make some sort of exclamation, then shrugs and grabs the pizza. 'You looked thinner on your Grimdr profile, anyways,' he huffs and slams the door shut on the both of you.")
        input ("Dilma mutters, 'Get on Grimdr, they told me... you'll meet someone nice, they told me...' 'I'm hungover as hell and I just want to go home.'")

        a=0
        while a==0:
            print("1: Say 'A ride? Why not, I don't get paid enough to follow company policy.'") 
            print("2:Say 'Wait, are you a hitch hiker? NO WAY. I don't want to be murdered in the middle of nowhere. Anyway,' you make fingerguns at Dilma, 'I'm a busy dude, and I'm outta here!'")
            print("3: Say 'Don't worry about the gas money, I get that paid for by my employer!' (you should have read your contract, you don't) 'Hop on board!'")
            dilma_convo=(input("What do you do? "))

            if dilma_convo==("1"):
                tips += 15
                on_board.append("DILMA FUCHS")
                input ("Dilma seems happy with that, she pulls out her communicator and sends you a few credits. 'Alright, I'm just going to sleep on the back seat. Wake me up when we get back to Planet Pizza.'")
                a=1
                leave_delivery_one()
            elif dilma_convo==("2"):
                input ("Dilma rolls her eyes 'Whatever, I'll just get the shuttle.' 'You sure will, loser! HaHAAaaaa!' you screech as you make your way back to your ship.")
                a=1
                leave_delivery_one()
            elif dilma_convo==("3"):
                input ("Dilma roughly slaps you on the back 'Alright, what a star. I'm just going to crash on the back seat. Wake me up when we get to Planet Pizza.'")
                a=1
                on_board.append("DILMA FUCHS")
                leave_delivery_one()
            else: 
                print ("Please choose 1, 2, or 3.")



    def compliments():
        global tips
        global Time
        Time -= 2
        a=0
        while a==0: 
            print ("1: 'Oh wow! You're so big and glistening, that's mighty impressive.'")
            print ("2: 'I like your tiny little weird face.'")
            print ("3: 'Is that some sort of approximation of hair? What a cut!'")
            compliment=(input("Which compliment do you use? "))

            if compliment==("1"):
                    tips +=10
                    input ("The alien can barely contain his glee 'I know! I'm so handsome! It's great to meet a fellow aesthete!' Several slimy pseudopodia noisily gurgle out of Mr. Galgogagoa's body and mash his communicator. He grabs the pizza and slams the door in your face.")
                    a=1
                    leave_delivery_one()
            elif compliment==("2"): 
                    tips +=5
                    input ("Mr. Galgogagoa wobbles, in what must be a display of pleasure 'My mother said the same thing! Every day that goes by since I ate her fills me with sorrow.' He looks literally and figuratively reflective for a moment, and then his head extends and smashes the tip button on his communicator. He grabs the pizza and then slams the door in your face.")
                    a=1
                    leave_delivery_one()
            elif compliment==("3"):
                    input ("'The alien's skin begins to bubble. 'How dare you?! What a breach of etiquette! Why must you point out my most shameful reproductive mechanisms?!'")
                    input ("He bristles and gurgles with rage, his midsection splitting into a giant maw, lined with millions of thin razorsharp bristles. A huge serpentine tongue whips out of the cavernous void and drags you inside.")
                    input ("There is darkness and the last thing you hear are your own bones crunching.")
                    a=1
                    death()
            else:
                print ("Please choose 1, 2, or 3")





    def d1_2():
        global tips
        global Time 
        input ("You glance into the room behind Mr. Galgogagoa. A very tired looking woman is sat on a sofa in front of a massive television.")

        a=0
        inventory.remove("PIZZA")
        while a==0:
            print ("1: Getting tips is a pretty good dopamine rush, and it might help with your rent situation! Compliment the alien.")
            print (f"2: Hand over the pizza and get on with your deliveries - you have {Time} space minutes left!")
            print ("3: Shout over to the woman 'Hey humie, what's up?!'")
            linker = (input ("What do you do? "))
            
            if linker == ("1"):
                a=1
                compliments()

            elif linker == ("2"):
                a=1
                leave_delivery_one()

            elif linker == ("3"): 
                a=1
                dilma_convo()
                
            else:
                print ("Please choose 1, 2, or 3")

    def d1_arrival():
        global ship_health
        global tips 
        input("The Hypernova's autopilot begins a retroburn to drop you through the atmosphere of Proxima Astoria 7. 'Approaching delivery location 1. Mr, Galgogagoa, 82 Hyperdrake Lane.")
        if ship_health <= 69:
            input("There are a few distressing screeches and clangs as your banged up ship plummets towards the planet. You make a mental note to avoid crashing into asteroids in future.")
        elif ship_health >= 70:
            input("There's some rattling and whooshing sounds as your ship mostly smoothly enters the atmosphere.")
        input ("The landing gear whirs down, and you gracefully pull into the drive of a pretty nice semi-detached habdome. You grab the delivery bag marked 'Mr. Galgogagoa.' and swing your legs out of the ship.") 
        
        a = 0
        while a==0:
            print ("1: Walk up to the habdome and tap out a funky rhythm on the door.")
            print ("2: Walk up to the habdome and ring the bell.")
            knock = (input ("What do you do? "))
        
            if knock == ("1"):
                tips += 10
                input ("A gigantic blobby green-yellow mass opens the door, and a tiny face emerges from some sort of cloaca on the front of its... for want of a better word, body. 'Wow! What a tune! I love it! Hey, is that pizza?'")
                input ("Mr Galgogagoa pulls his communicator out from one of his folds using a tiny multi-jointed limb. He presses it a couple of times and your own WorkFriend™ flashes, showing that he has rewarded you with a tip!")
                input ("'Hey, Dilma, do you want a slice? Just one, though.'")
                a=1
                d1_2()
            elif knock == ("2"):
                input ("A gigantic blobby green-yellow mass opens the door, and a tiny face emerges from some sort of cloaca on the front of its... for want of a better word, body. 'Oh boy! Oh what a day! My pizza is here! Hey, Dilma, do you want a slice? Just one, though.'")
                a=1
                d1_2()
            else: 
                print ("Please choose 1 or 2")



    def asteroid_alley():
        
        global Time
        global on_board
        global ship_health

        random_chance = [
            "L",
            "R",
            "M",
        ]

        for_say = [
            "Eek. Here goes nothing...",
            "Wish me luck.",
            "Hope I don't hit an Asteroid Alley cat...",

        ]

        back_say = [
            "Your asteroid is grassteroid...",
            "Psshh! I've been avoiding roids since Zarglarb was President...",
            "Why don't we make this interesting?",
            "This ain't a thing...",
            "I don't exactly BELIEVE in asteroids, so...",
        ]

        ast_ahoy = [
            "Asteroid ahoy!",
            "Here comes an asteroid!",
            "Asteroid inbound!",
            "'Is that... an asteroid? Oh I just remembered where I am...'",
            "Asteroid incoming!",
            "Here comes the asteroid, doo-doo doo-doo...",
        ]

        miss = [
            "Phew!",
            "Close one!",
            "Sick swerve!",
            "Dodged it!",
            "Miss!",
            "Good dodging!",
            "Great skills, star sailor!",
            "Asteroid shmasteroid!",
            "U can't touch this!",
        ]

        hit = [
            "BOOM!",
            "THWACK!",
            "CRUNCH!",
            "BANG!",
            "SCRRRRRAAAAAPPPPPEEEEE!",
            "WALLOP!",
            "WHOMP!",
            "KAPLONK!",
            "BOP!",
            "KERRRAAANNNNNNGGGG!",
            "CRACK!",
        ]

        taunt = [
            "You know you're meant to be dodging these right?",
            "You've been winged by an asteroid...",
            "Who taught you how to fly a spaceship?!",
            "Direct hit!",
            "That's going to leave a mark...",
            "Any chance that was a coincindental, unrelated noise and shudder?",
        ]

        avoid = [
            "You slipped right past that one...",
            "You just avoided the asteroid...",
            "You squeaked past that asteroid...",
            "A close shave, but thankfully no cigar shave.",
            "No ship_health done there.",
            "Great work, you slippery fiend.",
            "This asteroid dodging is easy...",
        ]

        pandom = [
            "LEFT!",
            "MIDDLE!",
            "RIGHT!",
        ]

        ignore = [
            "\'Who asked you, MAP?!\'",
            "\'PAM. I got this.\'",
            "\'Sorry, I don't take orders from machines...\'",
            "\'No one tells me what to do...\'",
            "\'...no.\'",
        ]

        warning = [
            "Maybe listen to that helpful robot MAP you have next to you...",
            "Shoulda listened to PAM...",
            "Well... I don't want to tell you what to do...",
            "I guess PAM was right...",
            "Take a hint...",
        ]

        no_look = [
            "\'This is not as easy as I thought it would be...\'",
            "\'Objects in the rearview mirror may appear closer than they- ARRGHHHHH!\'",
            "\'I did not see this coming. I mean, I can't see anything coming...\'",
            "\'Dwayne \'ROCK 3000\' Johnson made this look so easy in The Fast and the Furious 97: Pluto Drift...\'",
            "Do you think you hit that because you can't see where you're going?",
            "*whistles innocently as carnage ensues...*",
            "Who thought going backwards through a load of asteroids would be such a bad idea...",
            "This is near impossible without someone to tell you where you're going...",
            "You could really do with some help...",
            "This was a bad idea..."
        ]

        input("As you approach Asteroid Alley, your WorkFriend™ pings up some helpful directions...")
        input("\'Looks like I can shave five minutes off my journey time by nipping through Asteroid Alley.\'")
        a = 0
        while a == 0:
            print("1: Five minutes! Well hot damn, I guess I'm going through Asteroid Alley.")
            print("2: I'm not risking certain death for the sake of five minutes...")
            ans = input("Please type 1 or 2 and press ENTER. ").strip()
            if ans == "1" or ans == "2":
                a = 1
            else:
                input("Sorry I didn't catch that.")

        if ans == "1":
            a = 0
            while a == 0:
                print(f"1: {random.choice(for_say)} I'm going in...")
                print(f"2: {random.choice(back_say)} I'm going through backwards!")
                ans = input("Please select type 1 or 2 and press ENTER. ").strip()
                if ans == "1" or ans == "2":
                    a = 1
                else:
                    input("Sorry I didn't catch that.")
            if (ans) == "1":
                ast = 10
                while ast > 0:
                    a = 0
                    while a == 0:
                        ans = input(f"{random.choice(ast_ahoy)} Type L, M or R to avoid it. ").upper().strip()
                        x = random.choice(random_chance) 
                        if ans == "L" or ans == "M" or ans == "R":
                            a = 1
                        else:
                            input("Sorry I didn't catch that. Good job these are patient asteroids...")
                    if ans == x:
                        input(f"{random.choice(miss)} {random.choice(avoid)}")
                    else:
                        input(f"{random.choice(hit)} {random.choice(taunt)}")
                        ship_health -= 10
                        input(f"Ship health: {ship_health}")
                    ast -= 1
                    if ast > 0:
                        if ship_health > 0:
                            if ast != 1:
                                input(f"There are {ast} asteroids left to avoid!")
                            else:
                                input("There is one asteroid left to avoid!")
                        else:
                            input("Uh oh...")
                            death_ast()
                    else:
                        if ship_health > 0:
                            input("Phew! You made it through Asteroid Alley.")
                            input("Your HyperNova's cruise drive kicks in with a deep thrum, and Proxima Astoria 7 begins to fill your windscreen.")
                            input ("You throw on the retroburners and begin a Hohmann transfer into low orbit.")
                        else:
                            input("Uh oh...")
                            death_ast()

            elif ans == "2":
                if "PAM" in on_board:
                    input("PAM turns to look at you... \'You're much weirder than I realised when I f-\'")
                    input("As you cockily shift the ship into reverse, her eyes light up a piercing red.")
                    input("\'You have engaged MAP mode,\' she honks monotously.")
                    input("\'You're a PAM MAP!\' you cry. \'I've never seen one of these before in person.\'")
                    input("\'Let's see what you can do with a gauntlet of angry asteroids.\'")
                    ast = 10
                    while ast > 0:
                        a = 0
                        while a == 0:
                            dir = random.choice(pandom)
                            ans = input(f"{random.choice(ast_ahoy)} \'{dir}\' shrieks PAM. Type L, M or R. ").upper().strip() 
                            if ans == "L" or ans == "M" or ans == "R":
                                a = 1
                            else:
                                input("Sorry I didn't catch that. Good job these are patient asteroids...")
                        if ans == dir[0]:
                            input(f"{random.choice(miss)} {random.choice(avoid)}")
                        else:
                            input(f"{random.choice(ignore)}")
                            input(f"{random.choice(hit)} {random.choice(warning)}")
                            ship_health -= 10
                            input(f"Ship health: {ship_health}")
                            if ship_health <= 0:
                                input("Uh oh...")
                                death_ast()
                        ast -= 1
                        if ast != 1:
                            input(f"There are {ast} asteroids left to avoid!")
                        else:
                            input("There is one asteroid left to avoid!")            

                else:
                    ast = 10
                while ast > 0:
                    a = 0
                    while a == 0:
                        ans = input(f"{random.choice(ast_ahoy)} Type L, M or R to avoid it. ").upper().strip()
                        if ans == "L" or ans == "M" or ans == "R":
                            a = 1
                        else:
                            input("It really doesn't matter what you type, you're going backwards through Asteroid Alley...")
                            a = 1
                    input(f"{random.choice(hit)} {random.choice(no_look)}")
                    ship_health -= 10
                    input(f"Ship health: {ship_health}")
                    ast -= 1
                    if ast > 0:
                        if ship_health > 0:
                            if ast != 1:
                                input(f"There are {ast} asteroids left to avoid!")
                            else:
                                input("There is one asteroid left to avoid!")
                        else:
                            input("Uh oh...")
                            death_ast()
                    else:
                        if ship_health > 0:
                            if ast != 1:
                                input(f"There are {ast} asteroids left to avoid!")
                            else:
                                input("There is one asteroid left to avoid!")
                        else:
                            input("Uh oh...")
                            death_ast()
            else:
                print("Sorry I didn't catch that.")
            Time -= 1
            if ship_health > 0:
                input(f"You have {Time} space minutes remaining...")
            else:
                ship_health = 0
            d1_arrival()
        else:
            input("'Guess I'll go the ever-so-slightly longer way.'")
            Time -= 6
            input(f"You have {Time} space minutes remaining...")
            d1_arrival()


    def launchpad():
        global on_board
        global Time
        if "PAM" in on_board:
            input ("You arrive at the launchpad with your new robotic ally in tow. It's a huge yard with an Auto-Retriever station in the centre. You place your key against the panel marked 'Call Vehicle'.") 
        else:
            input ("You saunter on over to the launchpad, glad to be away from that den of scum and villainy. It's a huge yard with an Auto-Retriever station in the centre. You place your key against the panel marked 'Call Vehicle'.")
        input ("There is the deep sound of rickety machinery sputtering and coming to life; a floor panel in the yard opens and a beat up yellow Fard Hypernova, replete with a Planet Pizza roof topper, appears and is locked into the take-off position.")
        input ("You place your key against the reader on the driver side and hop in. The smell of stale grease begins to permeate your clothing.")
        input ("Just when you're starting once again feel the thrill of living, your WorkFriend™ starts beeping. It's Colin. The communicator automatically detects you looking at it and answers the call.")
        input ("'So here's the deal: you've got three deliveries to make. The first one is going to take you past Asteroid Alley to Proxima Astoria, Mega Meat Feast, a Mr. Galgogagoa.'")
        input ("'The second pie is going to Bromelian 7, ham and pineapple.' The vid screen is tiny but you can just about make out the look disgust on Colin's face. 'Lady Karenkala, she's very picky.'")
        input ("Colin's face cracks into a sadistic smile. '...and the last delivery is to the Emperor himself. Anchovies, mushroom, olive, and pineapple. That's the kind of pizza a man who doesn't share orders,' Colin grunts. 'I can respect that. You'll find him on campaign in The Long Rim... good luck with that.' He starts wetly chortling and then suddenly stops.")
        input ("Pizzas added to your inventory.")
        for x in range(len(inventory)):
            print(inventory[x])
        input (f"Well, you've got {Time} space minutes left, hotshot. Get out of my sight' the vid screen closes.")
        input ("You press the big red Autolaunch button on the dash, and your sight turns to black as the acceleration forces the blood away from your eyes. The only thing you can hear is the roar of the ion engines firing. After a few moments the Hypernova is burning its way through the atmosphere, trailing a mile long plasma stream. Three minutes later and gravity has lost her grasp on you.")
        input ("For these fleeting minutes you are hit with the foreign sensation of enjoying your job.")
        input ("You put the coordinates for your first delivery into the onboard computer. 'Heck yeah! Onwards to Asteroid Alley!'")
        asteroid_alley()



    def mannequin():
        global Time
        global on_board
        print ("As you approach the metallic statue, you notice the articulated joints, the complicated lenses in place of eyes, the digital light strip where a mouth would be on a human, this is some sort of android! You notice a series of activation instructions.")
        a=0
        while a == 0:
            print("1: Ignore the instructions and bop the android on the head.")
            print("2: Follow them to the letter, reciting an alphanumeric passcode and then waving your hand in front of the android's left eye.")
            print("3: Leave the android alone and go to the launchpad, time's a wastin'!")
            choice_mannequin= (input("What would you like to do? "))
            
            if choice_mannequin==("1"):
                print ("A monotone voice emits from the robot: 'Percussive maintenance detected, entering maintenance mode. Contacting local service centre. Time to service: 72 hours'. Oh well, at least you tried. Time to head to the launchpad!")
                a=1
                Time -= 5
                print(f"You have {Time} space minutes remaining.")
                launchpad()
            elif choice_mannequin==("2"):
                print ("A soft blue light emits from the android's eyes, a monotone voice recites 'PAM Activated. Do you require navigational aid?")
                a=1
                print ("'That sounds really handy and I've always wanted a sidekick! Sure, tag along!'")
                on_board.append("PAM")
                Time -= 5
                print(f"You have {Time} space minutes remaining.")
                launchpad()

            elif choice_mannequin==("3"):
                print ("3: Leave the android alone and go to the launchpad, time's a wastin'!")
                a=1
                Time -= 2
                print(f"You have {Time} space minutes remaining.")
                launchpad()
        


    def bathroom():
        global Time
        print ("You go to the bathroom, you probably shouldn't be wasting time on biological functions.")
        Time -= 2
        if Time <=0:
            death()
        print (f"You have {Time} space minutes remaining...")
        area3()

    def disgruntled():
        print ("Your other colleague, a betentacled mass stuffed into a Planet Pizza uniform, says 'Whatever, just leave us alone.'")
        area3()



    def staffroomconvo():
        global dis
        global Time
        print ("The alien growls, reaches into his overalls and pulls out a pizza cutter.")
        a=0
        while a == 0:
            print("1: Say 'I dare you, you literal son of a-!'")
            print("2: Say 'I apologise for my outburst.'")
            print("3: Run away to the launchpad whilst screaming.")
            choice_staffroomconvo = (input("What would you like to do? "))
            
            if choice_staffroomconvo==("1"):
                input("The alien immediately and messily decapitates you.")
                a=1
                death()
            elif choice_staffroomconvo==("2"):
                a=1
                disgruntled() 
            elif choice_staffroomconvo==("3"):
                a=1
                launchpad()
            else: 
                print ("Please choose 1, 2, or 3")

    def dogalienconvo():
        global dis
        print ("You say hi to one of your colleagues, a droopy-faced doglike alien with a long snout. It lazily raises its head 'What do you want, newbie?'")
        a=0
        while a == 0:
            print ("1: Say 'Why the long face? Hurhurhur!'")
            print ("2: Say 'Whatever, mutley' and go check out the mannequin.")
            print ("3: Say 'I'm new here! This is all so exciting!'")
            choice_alien = (input ("What do you do? ")) 
            if choice_alien == ("1"):
                a=1
                staffroomconvo()
            elif choice_alien == ("2"):
                a=1
                dis = 1
                mannequin()
            elif choice_alien == ("3"):
                a=1
                dis = 1
                disgruntled()
            else: 
                print ("Please choose 1, 2, or 3.")
        


    def staffroom():
        global Time
        global on_board
        global dis
        
        print ("You go to the staffroom - a few bedraggled motivational pictures hang from the walls. Besides a couple of workers in mid conversation who immediately go quiet as you enter, the room is empty. Propped in the corner is what looks like a polished steel mannequin.")
        a=0
        while a == 0:
            print ("1: Try to strike up a conversation with the workers.")
            print ("2: Examine the steel mannequin.")
            print ("3: Go back.")
            choice_4 = (input ("What would you like to do? "))
            
            if choice_4 == "1" and dis == 1:
                disgruntled()
            elif choice_4 == ("1"):
                a=1
                dogalienconvo()
            elif choice_4 == ("2"):
                dis=1
                mannequin()
                a=1
            elif choice_4 == ( "3"):
                dis=1
                disgruntled()
                a=1
            else:
                print ("Please choose 1, 2, or 3")


    #Scene 1/4
    def area3(): 
        a=0
        while a == 0:
            print ("1: Staffroom")
            print ("2: Launchpad")
            print ("3: Bathroom")
            choice_3 = (input ("Where would you like to go? "))

            if choice_3 == ("1"):
                a=1
                staffroom()
            elif choice_3 == ("2"):
                a=1
                launchpad()
            elif choice_3 == ( "3"):
                a=1
                bathroom()
            else:
                print ("Please choose 1, 2, or 3")
            


    #Scene 1/3
    def area2():
        global Time 
        input ("Colin walks you through the shop floor - your nose is assaulted by the stench of melting cheese and machinery, tinged with ozone. 'It's time for your induction. You're going to watch a nice video from corporate, and then you're going to be a fully qualified driver.' You pass conveyers lined with workers frantically throwing toppings onto pizzas as they whizz by. There's a staccato zapping sound as the AtomChefs mounted at the end of the conveyers instantly cook each pizza. You reach the office and Colin directs you to sit in a chair.")
        input ("You nonchalantly slouch into the chair, and your arms and legs are immediately restrained by hidden metal cuffs. A vidscreen lowers before your eyes and a familiar, happy jingle starts to play.")
        input ("'Welcome to your new job at Pizza Planet! As a driver you'll be at the heart of the company. First things first, let's take your ID badge picture.'")
        input ("There's a flash and a CLICK.")
        input ("Your grimacing face appears on the vidscreen.")
        input ("You feel a cold, heavy weight being put around your neck, as more machinery whirls... there's a short sharp click.")
        input ("'Great job! As part of your probationary period you will be fitted with a WorkFriend™ personal communicator. As soon as you start a delivery shift you will have 45 minutes to make all your deliveries, or the pizza will be cold!'")
        input ("'Also, the communicator is fitted with a Schrödingian Eraser dialed into your quantum metafield... if you're late you'll cease to exist!'")
        input ("'Remember to put on your best customer service face... you get to keep all your tips!'")
        input ("'Here's one to get you started! DO NOT TAMPER WITH THE COMMUNICATOR!'")
        input ("'Please report to your manager for your first delivery and the keys to your vehicle.'")
        a = 0
        while a == 0:
            print ("1: Scream incoherently.")
            print ("2: As the shackles release, stand up, salute Colin, and ask for your keys.")
            print ("3: Ask Colin where the bathroom is.")
            choice_2 = (input ("What do you do? "))
        
            if choice_2 == ("1"):
                print ("'Yeah, that's what they all say.' Colin grumbles, drags you to your feet, and shows you where the bathroom, staffroom, and launchpad are. He throws you your keys and your first delivery slip. 'You're on the clock... get to work!'")
                a=1
                area3()
            elif choice_2 == ("2"):
                print ("Colin snorts. 'What a nerd.' He quickly shows you where the staffroom and launchpad are. He throws you your keys and your first delivery slip. 'You're on the clock, get to work!'")
                a=1
                area3()
            elif choice_2 == ("3"): 
                print ("You take a couple of minutes to collect yourself in the bathroom, as you walk out Colin tells you that you're already on the clock. He hands you your delivery slip and keys and shows you where the launchpad and staffroom are.")
                Time -= 2
                print (f"You have {Time} space minutes remaining...")
                a=1
                area3()
            else:
                print ("Please choose 1, 2, or 3")



    #Scene 1/2
    def area1():
        def choice_1():
            print("You tell Colin that it's your first day, and you're just really enthusiastic. He grunts what might pass for an affirmation and grabs your shoulder with a meaty paw, dragging you into the shop.")
            choice = (input ("Continue."))
            area2()     
        def choice_2():
            print ("You beam brightly at your new manager. 'I'm looking forward to mee-' Your sentence is cut off as he grabs you by your shoulders and pulls you into the shop.")
            choice = (input ("Continue."))
            area2()
        def choice_3():
            print ("Colin asks you if you are his new delivery driver. You continue to stare into space. After a few moments, Colin sighs and steps out of the shop. There is a brief flurry of movement and then his foot is firmly on your back, launching you into the shop.")
            choice = (input ("Continue."))
            area2()
        #Scene 1/1
        input ("You've been out of work for 3 months, rent is due, and you're on a 10 year GalactoDole sanction for misspelling your name on an application form. In an act of utter desperation you have decided to seek employment.")
        input ("The only place hiring in your sector is Pizza Planet, the pan galactic fastfood megacorporation. Renowned from The Long Rim to the Core Worlds for its Extinction Level Event Mega Meat Feast (at least 3 endangered species or your money back) and the promise to deliver in 45 minutes... or else.")
        input ("Your first shift is about to begin, you're standing outside the local Pizza Planet, in front of you is an old banged up intercom box besides an equally banged up wooden door.")
        a = 0
        while a==0:
            print ("1 = Repeatedly smash the buzzer.")
            print ("2 = Press the buzzer and say you're here for your first shift.")
            print ("3 = Stare gormlessly ahead and think about the series of events which led you here.")
            choice = (input ("What do you do? ").strip())
            if choice == ("1"):
                print ("The door swings open; a hugely rotund figure fills the frame. A pair of moist, beady eyes framed by a froglike face glare down at you. 'What do you zoggin want?' You take note of the name badge stapled to the creature: 'Colin: Manager'.")
                a = 1
                choice_1()
            elif choice == ("2"):
                print ("The door swings open; a hugely rotund figure fills the frame. A pair of moist, beady eyes framed by a froglike face stare at you. A grin paints its way across his wormy lips. 'Well if it isn't the eff en gee.' You take note of the name badge stapled to the creature: 'Colin, Manager'.")
                a = 1
                choice_2()
            elif choice == ("3"):
                print ("After a few minutes the door swings open; a hugely rotund figure fills the frame. A pair of moist, beady eyes framed by a froglike face stare at you. The creature barks out: 'What're you doing out here?!' He waits for your answer with a look of blank expectation. You're paying just about enough attention to read his name badge: 'Colin, Manager.'")
                a=1
                choice_3()
            else:
                print ("Please choose 1, 2, or 3")
        
    splashscreen() 
    def start():
        global on_board
        global Time
        a = 0
        while a == 0:
            intro = (input ("Are you ready? Type 'READY' or 'NO'! ").lower().strip())
            if intro == ("ready"): 
                print ("Here we go!")
                a=1
                area1()     
            elif intro ==("no"):
                input ("Coward.")
                a=1
            elif intro == "papa":
                on_board.append("PAM")
                Time = 40
                asteroid_alley()
            elif intro == "aaa":
                Time = 40
                asteroid_alley()
            elif intro == "arr":
                inventory.remove("PIZZA")
                inventory.remove("PIZZA")
                Time = 30
                pirates()
            elif intro == "dump":
                inventory.remove("PIZZA")
                inventory.remove("PIZZA")
                Time = 30
                on_board.append("DILMA FUCHS")
                pirates()
            elif intro == "pop":
                inventory.remove("PIZZA")
                inventory.remove("PIZZA")
                Time = 30
                on_board.append("PAM")
                pirates()
            elif intro == "pump":
                inventory.remove("PIZZA")
                inventory.remove("PIZZA")
                Time = 30
                on_board.append("PAM")
                on_board.append("DILMA FUCHS")
                pirates()
            elif intro == "rim":
                inventory = []
                ship_health = 70
                final_delivery()
            else:
                print ("Ready up! Type ready or no!")
    
    start()

if Time <= 0:
    input("You ran out of time to make your deliveries. Your Schrödingian Eraser flashes red and pulls you from your miserable existence.")
    input("GAME OVER.")
elif ship_health <= 0:
    input("GAME OVER.")
else:
    win()

