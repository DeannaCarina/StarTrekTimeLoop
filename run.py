# Developer: Deanna Sale
# Date of release: TBC
# Subject: Code Institute Portfolio Project 3 - Python
# Program Name: "Star Trek: Time Loop"

from functions import P_S, FourRoomChoice, FourRoomSecondChance, \
     ThreeRoomChoice, ThreeRoomSecondChance, TwoRoomChoice, \
     TwoRoomSecondChance, NoHealth, Credits, Error
import time

PreviousRoom = "None"

UserStats = {
    "health": 10,
    "fists": True,
    "knife": False,
    "phaser": False,
    "comms": True,
    "locator": True,
    "key": True,
    "batteries": True
}

FirstVisits = {
    "EngineBay": True,
    "1_1N": True,
    "1_1E": True,
    "1_1S": True,
    "1_1W": True,
    "1_1NE": True,
    "1_1SE": True,
    "1_1SW": True,
    "1_1NW": True,
    "1_2N": True,
    "1_2E": True,
    "1_2S": True,
    "1_2W": True,
    "1_2NE": True,
    "1_2SE": True,
    "1_2SW": True,
    "1_2NW": True,
    "NNE": True,
    "ENE": True,
    "TransporterRoom": True,
    "SSE": True,
    "SSW": True,
    "WSW": True,
    "WNW": True,
    "NNW": True
}


def Stats(healthNumber):
    UserStats["health"] = UserStats["health"] + (healthNumber)
    P_S('Your new health is: ' + str(UserStats['health']), 2)


def CheckStats():
    if UserStats["health"] <= 0:
        NoHealth()


def PlayGame():
    print('''
   _____ _______       _____    _______ _____  ______ _  __
  / ____|__   __|/\   |  __ \  |__   __|  __ \|  ____| |/ /
 | (___    | |  /  \  | |__) |    | |  | |__) | |__  | ' /
  \___ \   | | / /\ \ |  _  /     | |  |  _  /|  __| |  <
  ____) |  | |/ ____ \| | \ \     | |  | | \ \| |____| . \ 
 |_______ _____/__  __|______\  _ |_|  ____ \_____________\.
 |__   __|_   _|  \/  |  ____| | |    / __ \ / __ \|  __ \ 
    | |    | | | \  / | |__    | |   | |  | | |  | | |__) |
    | |    | | | |\/| |  __|   | |   | |  | | |  | |  ___/
    | |   _| |_| |  | | |____  | |___| |__| | |__| | |
    |_|  |_____|_|  |_|______| |______\____/ \____/|_|
    \n''')
    WantToPlay = input("Would you like to play? (Y/N): \n")
    if WantToPlay.lower() == "y" or WantToPlay.lower() == "yes":
        P_S("Commencing time loop in...", 1.5)
        P_S("3...", 1)
        P_S("2...", 1)
        P_S("1...", 1)
        global name
        name = input("What is your name? \n")
        P_S(f"Hello {name}... welcome aboard the USS Enterprise:", 2)
        P_S("NCC-1703. It is Star Date 3167. You are the second", 3)
        P_S("engineer on board and work the night shift. You joined", 2.5)
        P_S("the ship on her maiden voyage of her 5 year mission:", 3.5)
        P_S('''
        TO BOLDLY GO WHERE NO MAN HAS GONE BEFORE...

o               .         ___---___                    .
        .              .--\        --.     .     .         .
                     ./.;_.\     __/~ \.
                    /;  / `-'  __\    . \ 
    .      .       / ,--'     / .   .;   \        |
                  | .|       /       __   |      -O-       .
                 |__/    __ |  . ;   \     | .    |
                 |      /  \\_    . ;| \___|
    .    o       |      \  .~\\___,--'     |           .
                  |     | . ; ~~~~\_    __|
     |             \    \   .  .  ; \  /_/   .
    -O-        .    \   /         . |  ~/                  .
     |    .          ~\ \   .      /  /~          o
   .                   ~--___ ; ___--~
                  .          ---         .
                ''', 3.5)
        SeeIntro = False
        while not SeeIntro:
            YesOrNo = input('Do you want to see the intro? (Y/N):\n')
            if YesOrNo.lower() == 'yes' or YesOrNo.lower() == "y":
                time.sleep(2)
                P_S("\nYou have been on the ship for 3 years now, and have", 2)
                P_S("steadily worked your way up the ranks to where you", 2)
                P_S("are currently.\n ", 2)
                P_S("Due to an asteroid colliding with the ship's port", 2)
                P_S("side, The Enterprise lost control of crucial guide", 2)
                P_S("and flight instruments, this made it impossible to", 2)
                P_S("steer away from the nearing Black Hole, and", 2)
                P_S("unfortunately the ship passed through the Black Hole", 2)
                P_S("causing massive loss of life and ship damage. You", 2)
                P_S("wake up in the Engine Bay after suffering from", 2)
                P_S("concussion. It seems that due to being close to the", 2)
                P_S("Warp Core of the ship, you were protected from the", 2)
                P_S("initial space-time anomalies.\n", 2)
                P_S("In the aftermath of the asteroid and passage through", 2)
                P_S("the Black Hole, you have broken your comms device and", 2)
                P_S("lost your locator device.\n", 2)
                P_S("Things don't seem as they should with the ship -", 2)
                P_S("walls are rippling with life, and even as you watch,", 2)
                P_S("things around you are dissapearing into nothingness", 2)
                P_S("and imploding in on themselves.\n", 2)
                P_S("There is a nearby planet which should be within beam", 2)
                P_S("distance, but without your comms and locator devices", 2)
                P_S("the chances of getting there safely are slim.\n", 2)
                P_S("You must search the ship for all the necessary", 2)
                P_S("equipment before you can safely leave via the", 2)
                P_S("transporter room. \n", 2)
                P_S("You will need the following items to safely beam ", 2)
                P_S("down to Nova VII:", 2)
                print("     1. Locator Device")
                print("     2. Communication (Comms) Device")
                print("     3. Batteries for Items 1 & 2")
                P_S("     4. Power key for the transporter device\n", 4)
                P_S("On your exploration of the ship, you might also find", 2)
                P_S("weapons and items that will help you with healing,", 2)
                P_S("energy levels and defending yourself. As well as", 2)
                P_S("encounter situations that will reduce your health.\n", 2)
                P_S(f"Good luck {name}, live long... and prosper.", 2)
                RoomEngineBay()
            elif YesOrNo.lower() == 'no' or YesOrNo.lower() == "n":
                RoomEngineBay()
            else:
                print("That response does not compute.")
        else:
            Error()
    elif WantToPlay.lower() == "n" or WantToPlay.lower() == "no":
        P_S("*Beaming you out*", 1)
        P_S("Initialising shut down...", 1)
        P_S('''
                 ___ _ _ ___   ___ _ _ ___
                |_ _| | | __> | __| \ | . |
                 | ||   | _>  | _>|   | | |
                 |_||_|_|___> |___|_\_|___/
                ''', 2)
        Credits()
    else:
        print("That option does not compute, please try again.")
        PlayGame()


def RoomEngineBay():
    # ENGINE BAY---------------------------------------------------------------

    if FirstVisits["EngineBay"] is True:
        # Text for user's first visit to the Engine Bay
        P_S("\n-------------------------------------------\n", 3)
        print("You are in the Engine Bay.")  
        P_S("You tentatively feel your head, checking for any bumps or", 2)
        P_S("cuts and look at your hand for any traces of blood. You", 2)
        P_S('must have really hit your head hard as the room seems to be', 2)
        P_S("spinning. You slowly get to your feet pushing yourself up", 2)
        P_S("on the nearby Warp Core control systems - this is what you", 2)
        P_S("must have hit your head on as you notice a small clump of", 2)
        P_S("your hair caught on the corner.", 2)
        P_S("   You head over to the nearby window and see a few pieces of", 2)
        P_S("the Enterprise's hull floating away into space. The nearby", 2)
        P_S("planet comes into view as the Enterprise rotates around. You", 2)
        P_S("have no idea where you are, but the planet does look", 2)
        P_S("familiar.", 2)
        P_S("   A nearby control panel for the Core Cooling Systems starts", 2)
        P_S("to distort and ripple. After a few seconds it starts to", 2)
        P_S("shrink into itself until there is nothing there. You stare", 2)
        P_S("at the place the control panel once stood - transfixed.", 2)
        P_S("What on Earth is going on? Does this have something to do", 2)
        P_S("with the Black Hole?", 2)
        # Log that user has now visited this room
        FirstVisits["EngineBay"] = False
    else:
        global PreviousRoom
        if PreviousRoom == "1_1W":
            # Travel text from 1_1W (Science Bay) to EngineBay
            P_S("You head back into the center of the ship along a very", 2)
            P_S("official looking corridor with warnings and alarms all", 2)
            P_S("over the walls and ceilings.", 2)
        elif PreviousRoom == "1_2W":
            # Travel text from 1_2W (Science Store) to EngineBay
            P_S("You make your way back to the center of the ship past the", 2)
            P_S("outside of the Science Bay and along a very official", 2)
            P_S("looking corridor with warnings and alarms all over the", 2)
            P_S("walls and ceilings.", 2)
        elif PreviousRoom == "1_1E":
            # Travel text from 1_1E (Eng.Sub.Con) to EngineBay
            P_S("You head back into the center of the ship along a very", 2)
            P_S("official looking corridor with warnings and alarms all", 2)
            P_S("over the walls and ceilings.", 2)
        elif PreviousRoom == "1_2E":
            # Travel text from 1_2E (Weapons Control) to EngineBay
            P_S("You make your way back to the center of the ship past the", 2)
            P_S("outside of Engineering Sub-Control and along a very", 2)
            P_S("official looking corridor with warnings and alarms all", 2)
            P_S("over the walls and ceilings.", 2)
        P_S("\n-------------------------------------------\n", 3)
        print("You are in the Engine Bay.")
        # If user has the locator device and batteries, show the ship diagram
        while UserStats["locator"] and UserStats["batteries"]:
            P_S('''
        ___________________          _-_             _      _-_      _
        \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                    \_ \    \----._________.----/  \----._________.----/
                    \ \   /  /    `-_-'              `.  `]-['  ,'
                __,--` `-'..'-_                        `.'   `.
                /____     █    ||                        | (█) |
                    `--.____,-'                          `___'
                \n
                █ = You are here.
            ''', 2)
            break
        P_S("You enter the room... you've been here before! It's the", 2)
        P_S("Engine Bay! You subconciously look over to where the control", 2)
        P_S("panel once stood for the cooling systems and are startled", 2)
        P_S("to see that it is standing there as if nothing had happened!", 2)
        P_S("You walk slowly towards it and as you do, it once again", 2)
        P_S("shrinks and implodes, trapped in a perpetual time-loop.", 2)
    P_S("   There are four potential exits from this room, each one on", 2)
    P_S("one of the four walls. The one straight ahead of you will head", 2)
    P_S("to the bow of the ship, the one behind - to the stern, the left", 2)
    P_S("- to port, and right - to starboard. Where would you like to go?", 2)
    PreviousRoom = "EngineBay"
    FourRoomChoice("Towards the bow",
                   "Towards the starboard",
                   "Towards the stern",
                   "Towards the port",
                   Room1_1N, Room1_1E, Room1_1S, Room1_1W)
    FourRoomSecondChance(Room1_1N, Room1_1E, Room1_1S, Room1_1W)


def Room1_1N():
    # MEETING ROOM-------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "EngineBay":
        # Travel text from Engine Bay to Meeting Room
        P_S("You head along a very long corridor and into the upper-mid", 2)
        P_S('section of the ship. You go into the room directly in front', 2)
        P_S("of you.", 2)
    elif PreviousRoom == "1_1NE":
        # Travel text from Engine Bay to Meeting Room
        P_S("You head out of the automatic sliding doors of the Holodeck", 2)
        P_S("and turn to your right, you walk for about 20 yards and head", 2)
        P_S("into the next room on your right.", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Meeting Room.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----.____█____.----/  \----.____█____.----/
                  \ \   /  /    `-_-'              `.  `] ['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1N"] is True:
        # Text for user's first visit to the meeting room
        P_S("You head into a small meeting room containing an oval", 2)
        P_S("table and eight chairs surrounding it.", 2)
        P_S("You look around to see if there's anything useful for you", 2)
        P_S("that might help with your current endevours.", 2)
        P_S("...", 2)
        P_S("After about 20 seconds you feel yourself going lightheaded,", 2)
        P_S("you can smell something strange, it's Neurazine Gas! You", 2)
        P_S("quickly cover your nose and mouth with your sleeve and make a", 2)
        P_S("hasty retreat from the room. You cough and splutter trying to", 2)
        P_S("rid your lungs of the putrid gases. You lose 2 health.", 2)
        # Log that user has now visited this room
        FirstVisits["1_1N"] = False
        # Reduce user's health and show user's new health score
        Stats(-2)
        CheckStats()
    else:
        # Text for user's subsequent visit to the meeting room
        P_S("You've been in here before! It's the small meeting", 2)
        P_S("room with the Neurazine Gas! You quickly bid a hasty", 2)
        P_S("retreat... even with a visit as fleeting as that, you can", 2)
        P_S("still feel the effects the gas has had on your lungs. You", 2)
        P_S("lose 1 health.", 2)
        # Reduce user's health and show user's new health score
        Stats(-1)
        CheckStats()
    # Text for visits to meeting room which end with leaving the shuttle bay
    P_S("From where you stand on the corridor with the meeting room behind", 2)
    P_S("you, there is the observation deck directly to your right", 2)
    P_S("(heading to port) past the entrance to another corridor, and", 2)
    P_S("there are corridors on either side of the meeting room, one", 2)
    P_S("heading to the Port Bow, and the other to the Starboard Bow. You", 2)
    P_S("also noticed a door on the opposite side of the meeting room", 2)
    P_S("which you know you could get to safely if you cover your face.", 2)
    P_S("Where would you like to go?", 2)
    # Log user's precence in the Meeting Room
    PreviousRoom = "1_1N"
    # Choice of where to go to
    FourRoomChoice("The Observation deck",
                   "To the Port Bow",
                   "Through the meeting room",
                   "To the Starboard Bow",
                   Room1_1NW, RoomNNW, Room1_2N, RoomNNE)
    # If user inputs invalid value - re-ask question
    FourRoomSecondChance(Room1_1NW, RoomNNW, Room1_2N, RoomNNE)


def Room1_1E():
    # ENGINEERING SUB CONTROL--------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "EngineBay":
        # Travel text from EngineBay to 1_1E (Eng.Sub.Con)
        P_S("You head away from the center of the ship along a very", 2)
        P_S("official looking corridor with warnings and alarms all", 2)
        P_S("over the walls and ceilings.", 2)
    elif PreviousRoom == "1_1S":
        # Travel text from 1_1S (Thrusters Control) to 1_1E (Eng.Sub.Con)
        P_S("You leave the Thrusters Control room and head in a starboard-", 2)
        P_S("bow direction along a corridor filled with safety and warning", 2)
        P_S("signs. Every empty space containing a computer screen or ship", 2)
        P_S("information poster. You head into the next room on your left.", 2)
    elif PreviousRoom == "1_1SE":
        # Travel text from 1_1SE (SickBay) to 1_1E (Eng.Sub.Con)
        P_S("You leave sickbay and head towards the bow of the ship,", 2)
        P_S("along a corridor filled with safety and warning signs.", 2)
        P_S("Every empty space containing a computer screen or ship", 2)
        P_S("information poster. You head into the room straight ahead.", 2)
    elif PreviousRoom == "ESE":
        # Travel text from ESE (Transporter Room) to 1_1E (Eng.Sub.Con)
        P_S("You leave the Transporter room and head in a port-bow,", 2)
        P_S("direction, along a corridor filled with safety and warning", 2)
        P_S("signs. Every empty space containing a computer screen or ship", 2)
        P_S("information poster. You head into the next room on the right.", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Engineering sub-control.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____     █    ||                        | (_)█|
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1E"] is True:
        # Text for user's first visit to Engineering Sub-Control
        P_S("You enter the room cautiously, there is a crew member in", 2)
        P_S("here! He is facing the wall and not moving. You move slowly", 2)
        P_S('towards him. "Hello?" you say. He turns... his face looks', 2)
        P_S("full of terror as he stumbles towards you while raising his", 2)
        P_S("combat knife in offence. He is going to attack you!", 2)
        # Log that user has now visited this room
        FirstVisits["1_1E"] = False
    else:
        P_S("You enter the room cautiously... You've been in here before!", 2)
        P_S("This is where you were attacked by the Crew Member. He's", 2)
        P_S("back! Almost as if he never left or never encountered you", 2)
        P_S("before, he turns to you with the same look of terror as", 2)
        P_S("before and stumbles towards you with his knife raised...", 2)
    if UserStats["phaser"] is True:
        P_S("\nThankfully as you have acquired the phaser, you managed to", 2)
        P_S("stun the crew member and knock him out without causing him", 2)
        P_S("harm. You recieved no damage. (You would have lost 2 if you", 2)
        P_S("were undefended).", 2)
    elif UserStats["knife"] is True:
        P_S("\nAs you have acquired the knife, you managed to defend", 2)
        P_S("from the oncoming attack, but not without the RedJac first", 2)
        P_S("catching you with his knife. The possessed crew member runs", 2)
        P_S("out of the door clutching his arm where you caught him", 2)
        P_S("with the KaBar Combat Knife. You lost 1 health (you would", 2)
        P_S("have lost 2 if you were undefended).", 2)
        Stats(-1)
        CheckStats()
    else:
        P_S("\nYou try your best to defend yourself from the possessed", 2)
        P_S("crew member. You punch and kick with all your might whenever", 2)
        P_S("he comes close. Eventually he runs away not wanting to face", 2)
        P_S("you any longer. You lost 2 health.", 2)
        Stats(-2)
        CheckStats()
    P_S("There are three potential exits from this room: the door to", 2)
    P_S("the engine bay where you have been before, a door straight", 2)
    P_S("ahead to go starboard, and a door to your left to go", 2)
    P_S("towards the bow. Where would you like to go?", 2)
    PreviousRoom = "1_1E"
    ThreeRoomChoice("To the Engine Bay",
                    "Towards the bow",
                    "Towards the starboard",
                    RoomEngineBay, Room1_1NE, Room1_2E)
    ThreeRoomSecondChance(RoomEngineBay, Room1_1NE, Room1_2E)


def Room1_1S():
    # THRUSTERS CONTROL--------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "EngineBay":
        P_S("Travel text from EngineBay to 1_1S (Thrusters control)", 2)
    elif PreviousRoom == "1_1SW":
        P_S("Text from 1_1SW (Crew Quarters) to 1_1S (Thrusters control)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Thrusters Control Room.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /___█          ||                        | (█) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1S"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_1S"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You got hurt (Cobalt Diselenide)! You lost 1 health.", 2)
    Stats(-1)
    CheckStats()
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_1S"
    FourRoomChoice("Room1_1W", "Room1_1E", "Room1_1SE", "Room1_2S",
                   Room1_1W, Room1_1E, Room1_1SE, Room1_2S)
    FourRoomSecondChance(Room1_1W, Room1_1E, Room1_1SE, Room1_2S)


def Room1_1W():
    # SCIENCE BAY--------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1NW":
        P_S("Text from 1_1NW (Observation Deck) to 1_1W (Science Bay)", 2)
    elif PreviousRoom == "EngineBay":
        P_S("Travel text from EngineBay to 1_1W (Science Bay)", 2)
    elif PreviousRoom == "1_1S":
        P_S("Text from 1_1S (Thrusters Control) to 1_1W (Science Bay)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Science Bay.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____     █    ||                        |█(_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's first visit to the Science Bay
    if FirstVisits["1_1W"] is True:
        print("Text for first visit")
        # Log that user has now visited this room
        FirstVisits["1_1W"] = False
    else:
        # Text for users subsequent visits to this room
        print("Text for second visit")
    if UserStats["phaser"] is True:
        print("Neural Parasites + Phaser")
        print("No health deducted")
    elif UserStats["knife"] is True and UserStats["phaser"] is False:
        print("Neural Parasites + Knife")
        Stats(-1)
        CheckStats()
    else:
        print("Neural Parasites + Fists")
        Stats(-2)
        CheckStats()
    PreviousRoom = "1_1W"
    print("ROOM AND PATH INFO HERE")
    ThreeRoomChoice("Engine Bay", "1_1SW", "1_2W",
                    RoomEngineBay, Room1_1SW, Room1_2W)
    ThreeRoomSecondChance(RoomEngineBay, Room1_1SW, Room1_2W)


def Room1_1NE():
    # HOLODECK-----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1E":
        P_S("Travel text from 1_1E (Eng.Sub.Con) to 1_1NE (Holodeck)", 2)
    elif PreviousRoom == "NNE":
        P_S("Travel text from NNE (Captain's Quarters) to 1_1NE (Holodeck)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Holodeck.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----.____█____.----/  \----._________.--█-/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /___█          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1NE"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_NE"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 1 health.", 2)
    Stats(+1)
    PreviousRoom = "1_1NE"
    print("ROOM AND PATH INFO HERE")
    ThreeRoomChoice("Room1_1N", "RoomNNE", "RoomENE",
                    Room1_1N, RoomNNE, RoomENE)
    ThreeRoomSecondChance(Room1_1N, RoomNNE, RoomENE)


def Room1_1SE():
    # SICKBAY------------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1S":
        P_S("Travel text from 1_1S (Thrusters Control) to 1_1SE (Sickbay)", 2)
    elif PreviousRoom == "SSE":
        P_S("Travel text from SSE (Maintenance) to 1_1SE (Sickbay)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Sickbay.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /___█          ||                        | (_)█|
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1SE"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_1SE"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 1 health.", 2)
    Stats(+1)
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_1SE"
    ThreeRoomChoice("Room1_1E", "RoomESETransporterRoom", "RoomSSE",
                    Room1_1E, RoomESETransporterRoom, RoomSSE)
    ThreeRoomSecondChance(Room1_1E, RoomESETransporterRoom, RoomSSE)


def Room1_1SW():
    # CREW QUARTERS------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1W":
        P_S("Travel text from 1_1W (Science Bay) to 1_1SW (Crew Quarters)", 2)
    elif PreviousRoom == "SSW":
        P_S("Travel text from SSW (Security) to 1_SW (Crew Quarters)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in someone's Crew Quarters.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /___█          ||                        |█(_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1SW"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_1SW"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 1 health.", 2)
    Stats(+1)
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_1SW"
    ThreeRoomChoice("Room1_1S", "RoomSSW", "RoomWSW",
                    Room1_1S, RoomSSW, RoomWSW)
    ThreeRoomSecondChance(Room1_1S, RoomSSW, RoomWSW)


def Room1_1NW():
    # OBSERVATION DECK---------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1N":
        P_S("Text from 1_1N (Meeting Room) to 1_1NW (Observation Deck)", 2)
    elif PreviousRoom == "NNW":
        P_S("Travel text from NNW (The Bridge) to 1_1NW (Observation Deck)", 2)
        P_S("You go down in the elevator which stops a few floors down.", 2)
        P_S("The doors open, and you head along an internal corridor, you", 2)
        P_S("head into the next room.", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are on the Observation Deck.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----.____█____.----/  \-█--._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_1NW"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_1NW"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    Stats(+1)
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_1NW"
    ThreeRoomChoice("Room1_1W", "RoomWNW", "RoomNNW",
                    Room1_1W, RoomWNW, RoomNNW)
    ThreeRoomSecondChance(Room1_1W, RoomWNW, RoomNNW)


# Rooms around the outside of the map (not including transporter room)---------
def Room1_2N():
    # SHUTTLE BAY--------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1N":
        P_S("You cover your mouth and nose with your sleeve and make", 2)
        P_S("your way through the meeting room.", 2)
    elif PreviousRoom == "NNW":
        # Travel text from NNW (The Bridge) to 1_2N (Shuttle Bay)
        P_S("You head through the door in The Bridge and are astonished", 2)
        P_S("to find that...", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the shuttle bay.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.--█-/  \----.____█____.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's first visit to the Shuttle Bay
    if FirstVisits["1_2N"] is True:
        P_S("This makes no sense... the Shuttle bay shouldn't be in", 2)
        P_S("this area of the ship. You figure that the passage of the", 2)
        P_S("ship through the Black Hole must have not only affected the", 2)
        P_S("things within the ship, but the ship itself! There is no way", 2)
        P_S("of knowing if where you think you're going is actually going", 2)
        P_S("to be where you end up!", 2)
        # Log that user has now visited this room
        FirstVisits["1_2N"] = False
    else:
        # Text for subsequent visits to this room
        P_S("You've been here before! You're in the shuttle bay!", 2)
    P_S("You look around for a little while and find a snack bar, you", 2)
    P_S("are very hungry, so quickly un-wrap the snack and wolf it", 2)
    P_S("down. You gain 1 health.", 2)
    Stats(+1)
    KeepLooking = False
    while not KeepLooking:
        YesOrNo = input('Do you want to keep searching this room? (Y/N):\n')
        if YesOrNo.lower() == 'yes' or YesOrNo.lower() == "y":
            P_S("You head deeper into the Shuttle Bay and rumage through", 2)
            P_S("some nearby sacks. You don't notice that on the opposite", 2)
            P_S("side of sack there is a Hazardous Waste warning! You peer", 2)
            P_S("into the bag and can't believe your eyes! It's Trilithium", 2)
            P_S("Resin! You quickly turn and run from the bag and head ", 2)
            P_S("towards the door you came through...", 2)
            P_S("The door starts to open, but just as it does you hear a", 2)
            P_S("massive commotion behind you, the Trilithium Resin must", 2)
            P_S("have exploded on the pressure change of the room when the", 2)
            P_S("door opened. You feel your body break under the force of", 2)
            P_S("the blast and you get slammed into the wall. You close", 2)
            P_S("your eyes and lose conciousness.", 2)
            P_S('''
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
            \n''', 2)
            Credits()
        elif YesOrNo.lower() == 'no' or YesOrNo.lower() == "n":
            if PreviousRoom == "1_1N":
                P_S("You head back to the other side of the meeting room", 2)
                P_S("to the corridor you were in before. Where would you", 2)
                P_S("like to go?", 2)
                PreviousRoom = "1_1N"
                ThreeRoomChoice("The Observation deck",
                                "To the Port Bow",
                                "To the Starboard Bow",
                                Room1_1NW, RoomNNW, RoomNNE)
                ThreeRoomSecondChance(Room1_1NW, RoomNNW, RoomNNE)
            elif PreviousRoom == "NNW":
                P_S("You head back into the Bridge", 2)
                P_S("Where would you like to go from here?", 2)
                PreviousRoom = "NNW"
                TwoRoomChoice("The Observation Deck",
                              "Back into the Shuttle Bay",
                              Room1_1NW, Room1_2N)
                TwoRoomSecondChance(Room1_1NW, Room1_2N)
            else:
                Error()
        else:
            print("That response does not compute.")


def Room1_2E():
    # WEAPONS CONTROL----------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "ENE":
        P_S("Travel text from ENE (Navigation) to 1_2E (Weapons Control)", 2)
    elif PreviousRoom == "1_1E":
        P_S("Travel text from 1_1E (Eng.Sub.Con) to 1_2E (Weapons Control)", 2)
    elif PreviousRoom == "1_2SE":
        P_S("Text from 1_2SE (Personal Quarters) to 1_2E (Weapons Control)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Weapons Control.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--._█__,-'                          `___█
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2E"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_2E"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You got hurt (Dark Matter LifeForm)! You lost 1 health.", 2)
    Stats(-1)
    CheckStats()
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_2E"
    ThreeRoomChoice("RoomEngineBay", "Room1_2NE", "RoomESETransporterRoom",
                    RoomEngineBay, Room1_2NE, RoomESETransporterRoom)
    ThreeRoomSecondChance(RoomEngineBay, Room1_2NE, RoomESETransporterRoom)


def Room1_2S():
    # THE BRIG-----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "SSE":
        P_S("Travel text from SSE (Maintenance) to 1_2S (The Brig)", 2)
    elif PreviousRoom == "1_1S":
        P_S("Travel text from 1_1S (Thrusters Control) to 1_2S (The Brig)", 2)
    elif PreviousRoom == "1_2SW":
        P_S("Travel text from 1_2SW (Mess Hall) to 1_2S (The Brig)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in The Brig.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /█___          ||                        | (_) |
                  `--.____,-'                          `_█_'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2S"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_2S"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You got hurt (Dikironium Cloud)! You lost 3 health.", 2)
    Stats(-3)
    CheckStats()
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_2S"
    TwoRoomChoice("Room1_2SE", "RoomSSW",
                  Room1_2SE, RoomSSW)
    TwoRoomSecondChance(Room1_2SE, RoomSSW)


def Room1_2W():
    # SCIENCE STORE------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1W":
        P_S("Travel text from 1_1W (Science Bay) to 1_2W (Science Store)", 2)
    elif PreviousRoom == "1_2NW":
        P_S("Text from 1_2NW (Meditation Room) to 1_2W (Science Store)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Science Store Room.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--._█__,-'                          █___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2W"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_2W"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You got hurt (Genesis Worms)! You lost 1 health.", 2)
    Stats(-1)
    CheckStats()
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_2W"
    ThreeRoomChoice("Room1_2SW", "RoomWNW", "RoomEngineBay",
                    Room1_2SW, RoomWNW, RoomEngineBay)
    ThreeRoomSecondChance(Room1_2SW, RoomWNW, RoomEngineBay)


def Room1_2NE():
    # STOREROOM----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2E":
        P_S("Travel text from 1_2E (Weapons Control) to 1_2NE (Storeroom)", 2)
    elif PreviousRoom == "NNE":
        P_S("Travel text from NNE (Captains Quarters) to 1_2NE (Storeroom)", 2)
    P_S("\n-------------------------------------------\n", 3)
    P_S("You are in the Ship Store Room.", 2)
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.--█-/  \----._________.--█-/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's ONLY visit to the Store Room
    P_S("You died!\n", 1.5)
    P_S('''
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
        \n''', 2)
    Credits()


def Room1_2SE():
    # PERSONAL QUARTERS--------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "ESE":
        P_S("Text from ESE (Transporter Room) to 1_2SE (Personal Quarters)", 2)
    elif PreviousRoom == "1_2S":
        P_S("Travel text from 1_2S(The Brig) to 1_2SE (Personal Quarters)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in your Personal Quarters.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /█___          ||                        | (_) |
                  `--.____,-'                          `___█
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2SE"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_2SE"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 3 health.", 2)
    Stats(+3)
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_2SE"
    TwoRoomChoice("Room1_2E", "RoomSSE",
                  Room1_2E, RoomSSE)
    TwoRoomSecondChance(Room1_2E, RoomSSE)


def Room1_2SW():
    # MESS HALL----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "SSW":
        P_S("Travel text from SSW (Security QUarters) to 1_2SW (Mess Hall)", 2)
    elif PreviousRoom == "1_2W":
        P_S("Travel text from 1_2W (Science Store) to 1_2SW (Mess Hall)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Mess Hall.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /█___          ||                        | (_) |
                  `--.____,-'                          █___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2SW"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_2SW"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 2 health.", 2)
    Stats(+2)
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_2SW"
    TwoRoomChoice("Room1_2S", "RoomWSW",
                  Room1_2S, RoomWSW)
    TwoRoomSecondChance(Room1_2S, RoomWSW)


def Room1_2NW():
    # MEDITATION ROOM----------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "WNW":
        P_S("Text from WNW (Conference Lounge) to 1_2NW (Meditation)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Meditation Room.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.--█-/  \-█--._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2NW"] is True:
        # Text for user's first visit to this room
        print("First Visit text here")
    # Log that user has now visited this room
        FirstVisits["1_2NW"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    P_S("You found food! You gained 2 health.", 2)
    Stats(+2)
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "1_2NW"
    TwoRoomChoice("RoomNNW", "Room1_2W",
                  RoomNNW, Room1_2W)
    TwoRoomSecondChance(RoomNNW, Room1_2W)


def RoomNNE():
    # CAPTAINS QUARTERS--------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1N":
        P_S("Text from 1_1N (Meeting Room) to NNE (Captain's Quarters)", 2)
    elif PreviousRoom == "1_1NE":
        P_S("Travel text from 1_1NE (Holodeck) to NNE (Captain's Quarters)", 2)
    elif PreviousRoom == "ENE":
        P_S("Travel text from ENE (Navigation) to NNE (Captain's Quarters)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Captain's Quarters.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.--█-/  \----._________█----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's first visit to the Captains Quarters
    if UserStats["knife"] is False:
        print("You found a knife! You hook it into your belt.")
        # Log that the user has been here before
        UserStats["knife"] = True
    elif UserStats["knife"] is True:
        # Text for subsequent visits to this room
        print("This is where you found the knife.")
    else:
        Error()
    print("ROOM AND PATH INFO HERE")
    PreviousRoom = "NNE"
    TwoRoomChoice("Room1_2NE", "Room1_1NE",
                  Room1_2NE, Room1_1NE)
    TwoRoomSecondChance(Room1_2NE, Room1_1NE)


def RoomENE():
    # NAVIGATION---------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1NE":
        P_S("Travel text from 1_1NE (Holodeck) to ENE (Navigation)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Ship Navigation.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,█'                          `___█
            \n
            █ = You are here.
        ''', 2)
        break
    if UserStats["locator"] is False:
        # Text for user's first visit to Navigation
        P_S("You found a locator device!", 2)
        # Log that the user now has possession of the locator device
        UserStats["locator"] = True
        # Text for if the user has the batteries
        if UserStats["batteries"] is True:
            P_S("\nThe Locator device springs into life once you", 2)
            P_S("put the batteries inside and shows you a", 2)
            P_S("small graphic of where you are in the ship...", 2)
            P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,█'                          `___█
            \n
            █ = You are here.
        ''', 2)
            P_S("You will now get a visual representation of where you", 2)
            P_S("are in the Enterprise each time you enter a room.", 2)
            if UserStats["comms"] is True and UserStats["batteries"] is True:
                # Text for if user has comms device and batteries
                print("")
                P_S("A voice comes out of your comms device:", 2)
                P_S(f'"{name}! We can see you! Just make sure you have the', 2)
                P_S('transporter override key and we should be able to', 2)
                P_S(f'safely beam you down to Nova VII. Good look {name}', 2)
                P_S('"hopefully we will see each other very soon."', 2)
        elif UserStats["batteries"] is False:
            # Text for if the user doesn't have the batteries
            P_S('The locator device is completely out of batteries, "There', 2)
            P_S('should be some batteries on this ship somewhere!", you', 2)
            P_S("think to yourself.", 2)
    elif UserStats["locator"] is True:
        # Text for if the user has been here before
        print("This is where you found the Locator device.")
    else:
        Error()
    PreviousRoom = "ENE"
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("RoomNNE", "Room1_2E",
                  RoomNNE, Room1_2E)
    TwoRoomSecondChance(RoomNNE, Room1_2E)


def RoomSSE():
    # MAINTENANCE--------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1SE":
        P_S("Travel text from 1_1SE (Sickbay) to SSE (Maintenance)", 2)
    elif PreviousRoom == "1_2SE":
        P_S("Text from 1_2SE (Personal Quarters) to SSE (Maintenance)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Ship Maintenance.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `█-.____,-'                          `___█
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's first visit to Ship Maintenance
    if UserStats["batteries"] is False:
        P_S("You found some batteries!", 2)
        # Log that the user now has possession of the batteries
        UserStats["batteries"] = True
        if UserStats["locator"] is False and UserStats["comms"] is False:
            # Text for if comms and locator devices are false
            P_S("\nYou put the batteries into your pocket for safekeeping.", 2)
        elif UserStats["comms"] is True and UserStats["locator"] is False:
            # Text for if comms device is true and locator device is false
            P_S("\nYou put two batteries inside of the comms device,", 2)
            P_S("and store the other two in your pocket for safekeeping.", 2)
            P_S("\nA voice comes out of your comms device:", 2)
            P_S('"He... Hello? Can anyone hear me? Simister Clancy here', 2)
            P_S('of Starfleet outpost 3-1-Victor-2-Foxtrott, on Nova VII', 2)
            P_S('do you read me? Please respond."', 2)
            P_S("You can't believe it... You fumble with the comms device", 2)
            P_S("almost dropping it in your hurry to respond...", 2)
            P_S(f'"Hello Mr Clancy", {name} here, Second Engineer of the', 2)
            P_S("USS Enterprise NCC-1703, it's so good to hear your voice!", 2)
            P_S("things are a bit crazy up here, we were struck by an", 2)
            P_S("asteroid and lost control of the ship, we ended up", 2)
            P_S("passing though a Black Hole. I must have been thrown", 2)
            P_S("about in the comotion as I woke up on the floor and", 2)
            P_S('things were all over the place!', 2)
            P_S("\nYou wait anxiously for Clancy to respond.\n", 2)
            P_S('"Yes, I heard all about it! I managed to get some of your', 2)
            P_S("crew to safety down here on Nova VII before your shipwide", 2)
            P_S("comms and transporter went offline. I can help you get", 2)
            P_S("out, but you'll need to find a locator device on board so", 2)
            P_S("I can pinpoint your location. You'll also need the", 2)
            P_S("Transporter override key so I can access it remotely.", 2)
            if UserStats["key"] is True:
                # Text for if key is in users possession
                P_S('\n"I already have the key!" you shout down the comms', 2)
                P_S("device excitedly.\n", 2)
                P_S('"Fantastic!" replies Clancy.', 2)
            P_S("Let me know as soon as you have the locator device and", 2)
            P_S("are ready in the Transporter room with the override key.", 2)
            P_S("I have a feeling you don't have much time, your ship", 2)
            P_S(f'is highly compromised. Hurry {name}, hurry... "', 2)
            print("")
            P_S("You stow the comms device into your pocket and continue", 2)
            P_S("on your way - filled with new hope.", 2)
        elif UserStats["locator"] is True and UserStats["comms"] is False:
            # Text for if locator device is true and comms device is false
            P_S("\nYou put two batteries inside of the locator device,", 2)
            P_S("and store the other two in your pocket for safekeeping.", 2)
            P_S("\nThe Locator device springs into life once you", 2)
            P_S("put the batteries inside and shows you a", 2)
            P_S("small graphic of where you are in the ship...", 2)
            P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,█'                          `___█
            \n
            █ = You are here.
        ''', 2)
            P_S("You will now get a visual representation of where you", 2)
            P_S("are in the Enterprise each time you enter a room.", 2)
        elif UserStats["locator"] is True and UserStats["comms"] is True:
            # Text for if user has the comms and locator devices
            P_S("\nYou put two batteries inside of the comms device.", 2)
            P_S("\nA voice comes out of your comms device:", 2)
            P_S('"He... Hello? Can anyone hear me? Simister Clancy here', 2)
            P_S('of Starfleet outpost 3-1-Victor-2-Foxtrott, on Nova VII', 2)
            P_S('do you read me? Please respond."', 2)
            P_S("You can't believe it... You fumble with the comms device", 2)
            P_S("almost dropping it in your hurry to respond...", 2)
            P_S(f'"Hello Mr Clancy", {name} here, Second Engineer of the', 2)
            P_S("USS Enterprise NCC-1703, it's so good to hear your voice!", 2)
            P_S("things are a bit crazy up here, we were struck by an", 2)
            P_S("asteroid and lost control of the ship, we ended up", 2)
            P_S("passing though a Black Hole. I must have been thrown", 2)
            P_S("about in the comotion as I woke up on the floor and", 2)
            P_S('things were all over the place!', 2)
            P_S("\nYou wait anxiously for Clancy to respond.\n", 2)
            P_S('"Yes, I heard all about it! I managed to get some of your', 2)
            P_S("crew to safety down here on Nova VII before your shipwide", 2)
            P_S("comms and transporter went offline. I can help you get", 2)
            P_S("out, but you'll need to find a locator device on board so", 2)
            P_S("I can pinpoint your location. You'll also need the", 2)
            P_S("Transporter override key so I can access it remotely.", 2)
            if UserStats["key"] is True:
                P_S('\n"I already have the key!" you shout down the comms', 2)
                P_S("device excitedly.\n", 2)
                P_S('"Fantastic!" replies Clancy.', 2)
            P_S("Let me know as soon as you have the locator device and", 2)
            P_S("are ready in the Transporter room with the override key.", 2)
            P_S("I have a feeling you don't have much time, your ship", 2)
            P_S(f'is highly compromised. Hurry {name}, hurry... "', 2)
            print("")
            P_S("\nYou put the other batteries inside the locator device.", 2)
            P_S("\nThe Locator device springs into life once you", 2)
            P_S("put the batteries inside and shows you a", 2)
            P_S("small graphic of where you are in the ship...", 2)
            P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,█'                          `___█
            \n
            █ = You are here.
        ''', 2)
            P_S("You will now get a visual representation of where you", 2)
            P_S("are in the Enterprise each time you enter a room.", 2)
            P_S("You stow the comms device into your pocket and continue", 2)
            P_S("on your way, holding the locator device out in front of", 2)
            P_S("you - filled with new hope.", 2)
        else:
            Error()
    elif UserStats["batteries"] is True:
        # Text for if user has been here before
        print("This is where you found the batteries.")
    else:
        Error()
    PreviousRoom = "SSE"
    print("PATH INFO HERE")
    TwoRoomChoice("Room1_1SE", "Room1_2S",
                  Room1_1SE, Room1_2S)
    TwoRoomSecondChance(Room1_1SE, Room1_2S)


def RoomSSW():
    # SECURITY-----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2S":
        P_S("Travel text from 1_2S (The Brig) to SSW (Security)", 2)
    elif PreviousRoom == "1_1SW":
        P_S("Travel text from 1_1SW (Crew Quarters) to SSW (Security)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Security.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `█-.____,-'                          █___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's first visit to Security
    if UserStats["key"] is False:
        P_S("You found a key! On close inspection its branded with the", 2)
        P_S("Starfleet logo. During the three years you have worked on", 2)
        P_S("The Enterprise, you have only seen this key a handfull of", 2)
        P_S("times, when the residents of a planet want to be in control", 2)
        P_S("of who beams down to the surface and when - it allows them", 2)
        P_S("full control over the ship's external beam capabilities -", 2)
        P_S("very helpful when they aren't very trusting!\n", 2)
        P_S("You put the key in your pocket for safekeeping.", 2)
        # Log that the user now has possession of the Key
        UserStats["key"] = True
    elif UserStats["key"] is True:
        # Text for if user has been here before
        print("This is where you found the override key for the Transporter.")
    else:
        Error()
    PreviousRoom = "SSW"
    print("PATH INFO HERE")
    TwoRoomChoice("Room1_1SW", "Room1_2SW",
                  Room1_1SW, Room1_2SW)
    TwoRoomSecondChance(Room1_1SW, Room1_2SW)


def RoomWSW():
    # RECREATION ROOM----------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1SW":
        P_S("Travel text from 1_1SW (Crew Quarters) to WSW (Rec Room)", 2)
    elif PreviousRoom == "1_2SW":
        P_S("Travel text from 1_2SW (Mess Hall) to WSW (Rec Room)", 2)
    P_S("\n-------------------------------------------\n", 3)
    P_S("You are in the Recreation Room.", 2)
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.█   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's ONLY visit to the Recreation Room
    P_S("You died!\n", 1.5)
    P_S('''
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
        \n''', 2)
    Credits()


def RoomWNW():
    # CONFERENCE LOUNGE--------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2W":
        P_S("Text from 1_2W (Science Store) to WNW (Conference Lounge)", 2)
    elif PreviousRoom == "1_1NW":
        P_S("Text from 1_1NW (Observation Deck) to WNW (Conference Lounge)", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Conference Lounge.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.--█-/  \----█_________.----/
                  \ \   /  /    `-_-'              `.  `] ['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for user's first visit to the Conference Lounge
    if UserStats["phaser"] is False:
        P_S("You found a phaser! This will help against corporeal threats", 2)
        P_S("and reduce if not eliminate any potential damage these", 2)
        P_S("threats inflict upon you.", 2)
        # Log that the user now has possession of the phaser
        UserStats["phaser"] = True
    elif UserStats["phaser"] is True:
        # Text for if the user has been here before
        print("This is where you found the phaser.")
    else:
        Error()
    print("PATH INFO HERE")
    PreviousRoom = "WNW"
    TwoRoomChoice("Room1_2NW", "RoomNNW",
                  Room1_2NW, RoomNNW)
    TwoRoomSecondChance(Room1_2NW, RoomNNW)


def RoomNNW():
    # THE BRIDGE---------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2NW":
        # Travel text from 1_2NW (Meditation)  to NNW (The Bridge)
        P_S("Leaving the meditation room, feeling refreshed and relaxed,", 2)
        P_S("you head along the front of the ship and up in the elevator", 2)
        P_S("to the top level.", 2)
    elif PreviousRoom == "WNW":
        # Travel text from WNW (Conference Lounge) to NNW (The Bridge)
        P_S("Leaving the Conference Lounge, and heading along an internal,", 2)
        P_S("corridor, you come to the central elevator. You head up in", 2)
        P_S("the elevator to the top level.", 2)
    elif PreviousRoom == "1_1NW":
        # Travel text from 1_1NW (Observation Deck) to NNW (The Bridge)
        P_S("Leaving the Observation deck, and heading along an internal,", 2)
        P_S("corridor, you come to the central elevator. You head up in", 2)
        P_S("the elevator to the top level.", 2)
    elif PreviousRoom == "1_1N":
        # Travel text from 1_1N (Meeting Room) to NNW (The Bridge)
        P_S("Leaving the outside of the meeting room behind you, you head", 2)
        P_S("in a port-bow direction along an internal, corridor. You come", 2)
        P_S("to the elevator and head up in the elevator to the top level.", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are on the Bridge.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _█_             _      _█_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    if FirstVisits["1_2NW"] is True:
        # Text for user's first visit to The Bridge
        P_S("You head onto the bridge. It's the first time you have ever", 2)
        P_S("seen this spectaular room empty. You head over to the", 2)
        P_S("captain's chair and run your hand over the smooth grey", 2)
        P_S("leather... you look around the room again checking for anyone", 2)
        P_S("else's presence. You smile to yourself... no one would know.", 2)
        P_S("   You slowly lower yourself into the most important chair on", 2)
        P_S("the ship and look at the viewscreen in front of you which is", 2)
        P_S("set to show the outside. In all your years in Starfleet, you", 2)
        P_S("never thought you'd find yourself sat here.", 2)
        P_S("   Standing up again, you look around to see if there's", 2)
        P_S("anything that might help you with your current plight.", 2)
        FirstVisits["1_2NW"] = False
    else:
        P_S("You head onto the bridge and smile at the captain's chair,", 2)
        P_S("almost going over to sit on it again.", 2)
    if UserStats["comms"] is False:
        P_S("You found a comms device!", 2)
        # Log that the user now has possession of the comms device
        UserStats["comms"] = True
        if UserStats["batteries"] is True:
            # Text for if the user has possession of the batteries
            P_S("\nYou put two of the batteries you found inside of the,", 2)
            P_S("comms device...", 2)
            P_S("\nA voice comes out of your comms device:", 2)
            P_S('"He... Hello? Can anyone hear me? Simister Clancy here', 2)
            P_S('of Starfleet outpost 3-1-Victor-2-Foxtrott, on Nova VII', 2)
            P_S('do you read me? Please respond."', 2)
            P_S("You can't believe it... You fumble with the comms device", 2)
            P_S("almost dropping it in your hurry to respond...", 2)
            P_S(f'"Hello Mr Clancy, {name} here, Second Engineer of the', 2)
            P_S("USS Enterprise NCC-1703, it's so good to hear your voice!", 2)
            P_S("things are a bit crazy up here, we were struck by an", 2)
            P_S("asteroid and lost control of the ship, we ended up", 2)
            P_S("passing though a Black Hole. I must have been thrown", 2)
            P_S("about in the comotion as I woke up on the floor and", 2)
            P_S('things were all over the place!', 2)
            P_S("\nYou wait anxiously for Clancy to respond.\n", 2)
            P_S('"Yes, I heard all about it! I managed to get some of your', 2)
            P_S("crew to safety down here on Nova VII before your shipwide", 2)
            P_S("comms and transporter went offline. I can help you get", 2)
            P_S("out, but you'll need need the Transporter override key so", 2)
            P_S("I can access it remotely.", 2)
            if UserStats["key"] is True and UserStats["locator"] is True:
                # Text for if user has the key and locator device
                P_S('\n"I already have the key!" you shout down the comms', 2)
                P_S("device excitedly.\n", 2)
                P_S('"Fantastic!" replies Clancy. "I can also see your', 2)
                P_S("location from your comms device, so I'll be able to", 2)
                P_S('pinpoint your position for safe beam transportation."', 2)
            elif UserStats["key"] is True and UserStats["locator"] is False:
                # Text for if user has the key but not the locator device
                P_S('\n"I already have the key!" you shout down the comms', 2)
                P_S("device excitedly.\n", 2)
                P_S('"Fantastic!" replies Clancy. "You will also need to', 2)
                P_S('find a locator device so I can pinpoint your exact', 2)
                P_S('location once you are in the beam transport room."', 2)
            elif UserStats["key"] is False and UserStats["locator"] is False:
                # Text for if the user doesnt have the key or locator device
                P_S('"You will also need to find a locator device so I can', 2)
                P_S('pinpoint your exact location once you are in the', 2)
                P_S('beam transportation room."', 2)
            P_S("I have a feeling you don't have much time, your ship", 2)
            P_S(f'is highly compromised. Hurry {name}, hurry... "', 2)
            print("")
            P_S("You stow the comms device into your pocket and continue", 2)
            P_S("on your way - filled with new hope.", 2)
        elif UserStats["batteries"] is False:
            # Text for if the user doesnt have the batteries
            P_S('The comms device is completely out of batteries, "There', 2)
            P_S('should be some batteries on this ship somewhere!", you', 2)
            P_S("think to yourself.", 2)
    elif UserStats["comms"] is True:
        # Text for if user has been here before
        P_S("This is where you found the comms device. There's nothing.", 2)
        P_S("else here of interest.", 2)
    else:
        Error()
    P_S("As you look around The Bridge, there is a door here that has", 2)
    P_S("never been here before, you look at it uneasily, waiting for it", 2)
    P_S("to dissappear as the cooling controls did in the Engine Bay, but", 2)
    P_S("it seems permenant enough. You could go through this door, or you", 2)
    P_S("could go down in the elevator, but you don't know where it would", 2)
    P_S("stop. Where would you like to go?", 2)
    PreviousRoom = "NNW"
    TwoRoomChoice("Down the elevator", "Through the unusual door",
                  Room1_1NW, Room1_2N)
    TwoRoomSecondChance(Room1_1NW, Room1_2N)


def RoomESETransporterRoom():
    # TRANSPORTER ROOM---------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2E":
        # Text from 1_2E (Weapons Control) to ESE (Transporter Room)
        P_S("Leaving weapons control, you head long the outer starboard", 2)
        P_S("corridor of the ship, looking out at the starry expanse as", 2)
        P_S("you go. You head into the next room you come to.", 2)
    elif PreviousRoom == "1_1SE":
        # Travel text from 1_1SE (Sickbay) to ESE (Transporter Room)
        P_S("Leaving sickbay, you head long a short internal corridor.", 2)
        P_S("As you walk along, the multiple doors along this corridor", 2)
        P_S("seem to be dissappearing and reappearing much the same as", 2)
        P_S("the cooling controls in the Engine Bay. You keep walking", 2)
        P_S("until you come to the only door that has some semblance of", 2)
        P_S("permenance and head through it.", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Transporter Room.")
    # If user has the locator device and batteries, show the ship diagram
    while UserStats["locator"] and UserStats["batteries"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--` `-'..'-_                        `.'   `.
             /____  █       ||                        | (_)█|
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    # Text for every visit to the tranporter room
    P_S("You head over to the tranporter chamber and make your way up", 2)
    P_S("the couple of steps onto the transporter platform. You never", 2)
    P_S("did like beaming much. You jog down the steps again and over", 2)
    P_S("to the tranporter controls, you notice all the screens are", 2)
    P_S("flickering and the planet name 'Nova VII' keeps popping up on the", 2)
    P_S("screen. You imagine that with the controls in this state it", 2)
    P_S("would probably be quite dangerous to try and beam out of the", 2)
    P_S("ship... but still possible.", 2)
    if ((UserStats["comms"]) is True and (UserStats["batteries"]) is
            True and (UserStats["locator"]) is True and
            (UserStats["key"]) is True):
        # Text for if the user has all necessary equipment to leave the ship
        P_S("You pull the comms device out of your pocket...", 2)
        P_S('"Clancy, can you hear me?"', 2)
        P_S(f'"Loud and clear {name}!"', 2)
        P_S('"I have everything you said I need and I am in the', 2)
        P_S('Transporter Room, ready to beam down!"', 2)
        P_S('"Fantastic!" replies Clancy. "Put the override key in the', 2)
        P_S('controls and hold the locator device to your chest while', 2)
        P_S('you are stood on the transporter platform".', 2)
        P_S('You head up onto the platform again. "Ready!" you shout.', 2)
        P_S('"Calculating your position, distance, mass... setting', 2)
        P_S(f'controls to manual. Okay {name}, here we go..."', 2)
    # Does the user want to attempt beaming out of the ship?
    BeamOut = input("Would you like to beam out of the ship? (Y/N) \n")
    if BeamOut.lower() == "y" or BeamOut.lower() == "yes":
        P_S("\nInitialising beam...", 1)
        P_S("Beaming down to planet surface in...", 1)
        P_S("3...", 1)
        P_S("2...", 1)
        P_S("1...", 1)
        if ((UserStats["key"]) is True and (UserStats["comms"]) is
                True and (UserStats["locator"]) is True and
                (UserStats["batteries"]) is True):
            # Text for if user successfully completed the game
            P_S("Congratulations! You beamed safely down to Nova VII", 2)
            P_S("and escaped the time loop, you look up to the sky", 2)
            P_S("just in time to see The Enterprise lose the last of", 2)
            P_S("its structural integrity and scatter accross the", 2)
            P_S("heavens, some small pieces break through the", 2)
            P_S("atmosphere of Nova VII giving the planet a final ", 2)
            P_S("farewell in a symbolic meteor shower.", 2)
            P_S("You feel a hand settle on your shoulder...", 2)
            P_S('"Glad you made it out." Clancy smiles at you.', 3)
            PlayAgain = input("Would you like to play again? (Y/N) \n")
            if PlayAgain.lower() == "y" or PlayAgain.lower() == "yes":
                print("Press PLAY GAME to initialise time loop.")
            elif PlayAgain.lower() == "n" or PlayAgain.lower() == "no":
                P_S(f"Live long and prosper {name}", 2)
                P_S("Initialising shut down...", 1.5)
                P_S('''
                ___ _ _ ___   ___ _ _ ___
               |_ _| | | __> | __| \ | . |
                | ||   | _>  | _>|   | | |
                |_||_|_|___> |___|_\_|___/
                    \n\n\n\n''', 2)
                Credits()
        else:
            # Text for if user attempted to beam out without required items
            P_S("\nYou didn't have all the required equipment and", 2)
            P_S("items to successfully beam down to Nova VII. You", 2)
            P_S("beamed half way down to the planet's surface but", 2)
            P_S("appeared in space before you could reach your", 2)
            P_S("desination.", 2)
            P_S('''
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
                    \n
                    ''', 1)
            Credits()
    # If user doesn't want to beam out of the ship:
    elif BeamOut.lower() == "n" or BeamOut.lower() == "no":
        P_S("\nYou continue on your journey...", 2)
        P_S("From the Transporter room you have two options of where to", 2)
        P_S("go: Along an internal corridor towards the center of the ship", 2)
        P_S("or an external corridor towards your personal quarters. Where", 2)
        P_S("would you like to go?", 2)
        PreviousRoom = "ESE"
        TwoRoomChoice("Towards the center of the ship", "Personal Quarters",
                      Room1_1E, Room1_2SE)
        TwoRoomSecondChance(Room1_1E, Room1_2SE)
    else:
        print("That option does not compute, please try again.")
        RoomESETransporterRoom()


PlayGame()
