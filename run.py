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
    "comms": False,
    "locator": False,
    "key": False,
    "batteries": False
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
    # 1_2NE Will never be false as this is a kill room
    "1_2SE": True,
    "1_2SW": True,
    "1_2NW": True,
    # NNE uses knife variable to determine previous visits
    # ENE uses locator variable to determine previous visits
    # ESE (Transporter Room) true/false value not needed
    # SSE uses batteries variable to determine previous visits
    # SSW uses key variable to determine previous visits
    # WSW Will never be false as this is a kill room
    # WNW uses phaser variable to determine previous visits
    # NNW uses comms variable to determine previous visits
}


def Stats(healthNumber):
    """
    Increases or decreases the users health by a specified amount
    then displays the users new health score.
    """
    UserStats["health"] = UserStats["health"] + (healthNumber)
    P_S('Your new health is: ' + str(UserStats['health']), 2)


def CheckStats():
    """
    At any point the users health is decreased using Stats(), the
    Checkstats() function is called after it to ensure the user hasn't
    got a health score of 0 or less. If they do then the NoHealth() function
    is called (from the functions.py file) and it is game over for the user.
    """
    if UserStats["health"] <= 0:
        NoHealth()


def PlayGame():
    """
    Function called at the end of the run.py file. Only function
    called on a global scale, subsequent room functions all called
    from within another function. This function allows the user to
    play or exit the game as well as see or not see the introduction.
    """
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
                P_S("things around you are disappearing into nothingness", 2)
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
                P_S("     4. Override key for the transporter device\n", 4)
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
            P_S("You head back into the centre of the ship along a very", 2)
            P_S("official looking corridor with warnings and alarms all", 2)
            P_S("over the walls and ceilings.", 2)
        elif PreviousRoom == "1_2W":
            # Travel text from 1_2W (Science Store) to EngineBay
            P_S("You run for the exit into the Science Bay and slam your", 2)
            P_S("shoulder against the door, it swings open and crashes", 2)
            P_S("into the wall behind it. You keep running as fast as", 2)
            P_S("you can through the Science Bay, taking no notice of", 2)
            P_S("the slightly wriggling mounds beneath the pristine white", 2)
            P_S("sheets on the gurneys. Again, you run for the exit of the", 2)
            P_S("Science Bay and the door opens for you automatically.", 2)
            P_S("You head back into the centre of the ship along a very", 2)
            P_S("official looking corridor with warnings and alarms all", 2)
            P_S("over the walls and ceilings.", 2)
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
        # Text for if user has been here before
        P_S("You subconciously look over to where the control", 2)
        P_S("panel once stood for the cooling systems and are startled", 2)
        P_S("to see that it is standing there as if nothing had happened!", 2)
        P_S("You walk slowly towards it and as you do, it once again", 2)
        P_S("shrinks and implodes, trapped in a perpetual time-loop.", 2)
    # Path information
    P_S("   There are four potential exits from this room, each one on", 2)
    P_S("one of the four walls. The one straight ahead of you will head", 2)
    P_S("to the bow of the ship, the one behind - to the stern, the left", 2)
    P_S("- to port, and right - to starboard. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "EngineBay"
    # Choice of where to go to
    FourRoomChoice("Towards the bow",
                   "Towards the starboard",
                   "Towards the stern",
                   "Towards the port",
                   Room1_1N, Room1_1E, Room1_1S, Room1_1W)
    # If user inputs invalid value - re-ask question
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
        # Travel text from The Holodeck to Meeting Room
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
        P_S("that might help with your current endeavours.", 2)
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
    # Path information
    P_S("From where you stand on the corridor with the meeting room behind", 2)
    P_S("you, there is the observation deck directly to your right", 2)
    P_S("(heading to port) past the entrance to another corridor, and", 2)
    P_S("there are corridors on either side of the meeting room, one", 2)
    P_S("heading to the Port Bow, and the other to the Starboard Bow. You", 2)
    P_S("also noticed a door on the opposite side of the meeting room", 2)
    P_S("which you know you could get to safely if you cover your face.", 2)
    P_S("Where would you like to go?", 2)
    # Log user's presence in the Meeting Room
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
        P_S("You head away from the centre of the ship along a very", 2)
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
        # Text for user's subsequent visits to this room
        P_S("You enter the room cautiously... You've been in here before!", 2)
        P_S("This is where you were attacked by the Crew Member. He's", 2)
        P_S("back! Almost as if he never left or never encountered you", 2)
        P_S("before, he turns to you with the same look of terror as", 2)
        P_S("before and stumbles towards you with his knife raised...", 2)
    if UserStats["phaser"] is True:
        # If user has phaser this happens:
        P_S("\nThankfully as you have acquired the phaser, you managed to", 2)
        P_S("stun the crew member and knock him out without causing him", 2)
        P_S("harm. You received no damage. (You would have lost 2 if you", 2)
        P_S("were undefended).", 2)
    elif UserStats["knife"] is True:
        # If user has knife this happens:
        P_S("\nAs you have acquired the knife, you managed to defend", 2)
        P_S("from the oncoming attack, but not without the RedJac first", 2)
        P_S("catching you with his knife. The possessed crew member runs", 2)
        P_S("out of the door clutching his arm where you caught him", 2)
        P_S("with the KaBar Combat Knife. You lost 1 health (you would", 2)
        P_S("have lost 2 if you were undefended).", 2)
        Stats(-1)
        CheckStats()
    else:
        # If user doesn't have phaser or knife, this happens:
        P_S("\nYou try your best to defend yourself from the possessed", 2)
        P_S("crew member. You punch and kick with all your might whenever", 2)
        P_S("he comes close. Eventually he runs away not wanting to face", 2)
        P_S("you any longer. You lost 2 health.", 2)
        Stats(-2)
        CheckStats()
    # Path information from this room
    P_S("There are three potential exits from this room: the door to", 2)
    P_S("the engine bay where you have been before, a door straight", 2)
    P_S("ahead to go starboard, and a door to your left to go", 2)
    P_S("towards the bow. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_1E"
    # Choice of where to go to
    ThreeRoomChoice("To the Engine Bay",
                    "Towards the bow",
                    "Towards the starboard",
                    RoomEngineBay, Room1_1NE, Room1_2E)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(RoomEngineBay, Room1_1NE, Room1_2E)


def Room1_1S():
    # THRUSTERS CONTROL--------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "EngineBay":
        # Travel text from EngineBay to 1_1S (Thrusters control)
        P_S("You head through the door behind you and towards the rear", 2)
        P_S("of the ship, along a very official-looking corridor covered", 2)
        P_S("in posters and warnings about the ships engines.", 2)
    elif PreviousRoom == "1_1SW":
        # Text from 1_1SW (Crew Quarters) to 1_1S (Thrusters control)
        P_S("You head along a short internal corridor from the crew", 2)
        P_S("member's room towards what you think is the rear of the", 2)
        P_S("ship... This makes no sense - the crew quarters shouldn't be", 2)
        P_S("accessible from here!", 2)

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
        P_S("On entering the room the first thing you notice is how warm", 2)
        P_S("and clammy the room is. You head over to the thrusters", 2)
        P_S("control panel and see that every possible error and warning", 2)
        P_S("light is visible and active. Sweat starts to bead on your", 2)
        P_S("forehead, which you wipe off with the back of your sleeve.", 2)
        P_S("   You look over to the warp core power diversion column and", 2)
        P_S("notice that the radiation protection cover has been blown", 2)
        P_S("open in the commotion! You must shut it otherwise the ship", 2)
        P_S("will be flooded with lethal amounts of radiation... it could", 2)
        P_S("already be too late.", 2)
        P_S("   You pick up one of the lead thyroid shields and strap it", 2)
        P_S("around your throat and put on some radiation safety goggles", 2)
        P_S("then make your way to the open hatch. As you get closer the", 2)
        P_S("heat you felt on entrance to the room intensifies and sweat", 2)
        P_S("once again starts to bead and run down your face.", 2)
        P_S("   With a quick movement you take hold of the hatch handle", 2)
        P_S("and swing the door shut. You pull your hand away and look at", 2)
        P_S("your palm which now is mostly covered in hot, angry, red", 2)
        P_S("blisters. Unsure whether they are radiation or heat burns,", 2)
        P_S("you rush over to the nearby sink and run your hand under", 2)
        P_S("cold water for a few minutes.", 2)
        P_S("You got hurt from burns! You lost 1 health.", 2)
        Stats(-1)
        CheckStats()
        # Log that user has now visited this room
        FirstVisits["1_1S"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You enter the room and are met with a wave of heat as you", 2)
        P_S("were the first time. Instinctively, you look at your palm and", 2)
        P_S("are shocked to see that the blisters you sustained on your", 2)
        P_S("last visit are no longer there.", 2)
        P_S("   You look over to the radiation hatch - it's open again!", 2)
        P_S("Once again you don the radiation protection and rush over to", 2)
        P_S("the hatch to close it - not learning from your previous", 2)
        P_S("mistakes, you once again pull your hand away after closing", 2)
        P_S("the door to find your palm covered in burns.", 2)
        P_S("You got hurt from burns! You lost 1 health.", 2)
        Stats(-1)
        CheckStats()
    # Path information
    P_S("With nothing else of interest in this room you look around to see", 2)
    P_S("your exit options. In this hexagonal room, there are two doors", 2)
    P_S("that seem to be heading in port-bow and starboard-bow directions,", 2)
    P_S("as well as a door on your right reading to starboard, and one", 2)
    P_S("behind you heading to stern. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_1S"
    # Choice of where to go to
    FourRoomChoice("Towards the port-bow", "Towards the starboard-bow",
                   "Through the door on your right",
                   "Through the door behind you",
                   Room1_1W, Room1_1E, Room1_1SE, Room1_2S)
    # If user inputs invalid value - re-ask question
    FourRoomSecondChance(Room1_1W, Room1_1E, Room1_1SE, Room1_2S)


def Room1_1W():
    # SCIENCE BAY--------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1NW":
        # Text from 1_1NW (Observation Deck) to 1_1W (Science Bay)
        P_S("You make your way out of the Observation Deck and towards the", 2)
        P_S("main ship elevator. You head down in the elevator and along a", 2)
        P_S("short internal corridor. You head through the next door you", 2)
        P_S("come to which is large and metal.", 2)
    elif PreviousRoom == "EngineBay":
        # Travel text from EngineBay to 1_1W (Science Bay)
        P_S("You head away from the centre of the ship along a very", 2)
        P_S("official looking corridor with warnings and alarms all", 2)
        P_S("over the walls and ceilings.", 2)
    elif PreviousRoom == "1_1S":
        # Text from 1_1S (Thrusters Control) to 1_1W (Science Bay)
        P_S("You head through the door in the port-bow direction, walk", 2)
        P_S("along a short internal corridor to the door at the end and", 2)
        P_S("go through.", 2)
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
        P_S("You head into the room and look around at all the strange", 2)
        P_S("things on the shelves. You peer at some of the bottles'", 2)
        P_S("labels and can't help but scrunch your nose at some of the", 2)
        P_S("disgusting substances inside them. This is why you never", 2)
        P_S("wanted to work in the Science Bay. Engineering is much", 2)
        P_S("less... gooey.", 2)
        P_S("   Around you there are gurneys with pristine white sheets", 2)
        P_S("covering small mounds of things you dread to think of. You", 2)
        P_S("keep searching the shelves for anything that might be of use", 2)
        P_S("to you and bend down to search in the lower cupboards.", 2)
        P_S("   As you bend down you didn't notice one of the white sheets", 2)
        P_S("moving ever so slightly with a Neural Parasite underneath it!", 2)
        # Log that user has now visited this room
        FirstVisits["1_1W"] = False
    else:
        # Text for users subsequent visits to this room
        P_S("You instinctively look over to the sheet-covered gurneys.", 2)
        P_S("The Neural Parasite that you last encountered in here still", 2)
        P_S("lying motionless on the floor. You shiver from the memory", 2)
        P_S("and head into the room. This is the Science Bay... there must", 2)
        P_S("be something in here of use! After a search in the desk", 2)
        P_S("drawers you find a packet of pretzels which you can't help", 2)
        P_S("but scavenge and eat on the spot. Your health increases by 1.", 2)
        Stats(+1)
        P_S("   As you eat, you don't notice that the Neural Parasite you", 2)
        P_S("killed last time has come back to life, and just as", 2)
        P_S("ravenously as you ate the pretzels - the parasite attacks", 2)
        P_S("you once more!", 2)
    P_S("   It launches itself onto your back and attempts to form a", 2)
    P_S("neural link to take over your body. You reach around your back", 2)
    P_S("and grab handfuls of the slimy parasite, it latches onto your", 2)
    P_S("hand not wanting to lose its plentiful bounty and starts to wind", 2)
    P_S("its tendrils around your arm. You hold it out in front of you...", 2)
    if UserStats["phaser"] is True:
        P_S("While you hold the parasite in front of you, you grab your", 2)
        P_S("phaser with your other hand and shoot it multiple times. It", 2)
        P_S("releases you from its grasp and falls to the floor in a", 2)
        P_S("slimy heap - scorch marks forming on its amoeba-like body.", 2)
        P_S("You didn't lose any health due to having the phaser.", 2)
    elif UserStats["knife"] is True and UserStats["phaser"] is False:
        P_S("While you hold the parasite in front of you, you grab your", 2)
        P_S("knife with your other hand and start slashing at the", 2)
        P_S("creature. On your first connection with the parasite, it", 2)
        P_S("tightens its grasp on you causing the supply of blood to", 2)
        P_S("your hand to be cut off. You grimace in pain and continue", 2)
        P_S("your attack! Eventually the parasite releases you from", 2)
        P_S("its grasp and falls to the floor in a gooey mound.", 2)
        P_S("   In the commotion and due to the tight grip the Neural", 2)
        P_S("Parasite had on you - you lost 1 health.", 2)
        Stats(-1)
        CheckStats()
    else:
        P_S("While you hold the parasite in front of you, you try and", 2)
        P_S("punch it with your other hand, but on contact your hand just", 2)
        P_S("seems to go straight through the creature. You try again and", 2)
        P_S("again as the parasite's grip on you tightens, squeezing the", 2)
        P_S("life out of your hand. You bend over and place your parasite-", 2)
        P_S("covered hand on the floor. You stamp on the creature with", 2)
        P_S("your heavy work boots causing it to release you. You stamp on", 2)
        P_S("it a few more times, not enjoying the fact you're killing", 2)
        P_S("something but at the same time, glad you weren't taken over", 2)
        P_S("by the parasite. You look down at the hand the parasite was", 2)
        P_S("attached to and see thin trails of blood dripping down your", 2)
        P_S("arm. You lost 2 health.", 2)
        Stats(-2)
        CheckStats()
    # Log users presence in this room
    PreviousRoom = "1_1W"
    # Path information
    P_S("You look around the room and see three exits. One heading back", 2)
    P_S("to the centre of the ship, one on the other side of the room with", 2)
    P_S("a sign above it saying 'Science Store' and one on the back wall", 2)
    P_S("that you imagine leads to the stern of the ship. Where would you", 2)
    P_S("like to go?", 2)
    # Choice of where to go to
    ThreeRoomChoice("Back to the centre of the ship",
                    "Science Store", "Towards the stern",
                    RoomEngineBay, Room1_1SW, Room1_2W)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(RoomEngineBay, Room1_1SW, Room1_2W)


def Room1_1NE():
    # HOLODECK-----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1E":
        # Travel text from 1_1E (Eng.Sub.Con) to 1_1NE (Holodeck)
        P_S("You head along a short internal corridor and up the main ship", 2)
        P_S("elevator. You head along a wide corridor with windows", 2)
        P_S("looking out into space. You notice a couple more pieces of", 2)
        P_S("The Enterprise floating around outside. You think back to the", 2)
        P_S("crew member that just attacked you wishing there was", 2)
        P_S("something you could do to save him. You walk a little further", 2)
        P_S("and notice the door to the next room is ajar... you go in.", 2)
    elif PreviousRoom == "NNE":
        # Travel text from NNE (Captain's Quarters) to 1_1NE (Holodeck)
        P_S("You head directly across the corridor into the Holodeck.", 2)
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
        P_S("You have never needed to use the Holodeck, but have heard", 2)
        P_S("that it's an amazing room with infinite possibilities. You", 2)
        P_S("ask the computer for what you'd like, and the room gives it", 2)
        P_S("to you... Would you like to:", 2)
        # Log that user has now visited this room
        FirstVisits["1_NE"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You smile at the memory of your last visit to this room.", 2)
        P_S("You have the same options as last time... what would you like", 2)
        P_S("to do?", 2)
    # Text for all visits to this room
    print("1: Relax on a Caribbean beach for a moment to get your breath")
    P_S("back from your adventure so far?", 4)
    print("2: See your family back on Earth for a few minutes as it")
    P_S("could be the last time you ever see them?", 4)
    P_S("3: Rest for a moment in a replica of the Captain's Quarters?", 3)
    print("4: You don't have the time for this, you want to leave the")
    P_S("Holodeck and keep trying to find a way off the ship.", 4)
    WouldLike = False
    while not WouldLike:
        OTTF = input("What would you like to do? (1/2/3/4):\n")
        if OTTF.lower() == "1" or OTTF.lower() == "one":
            P_S("The Holodeck transports you to a virtual Caribbean", 2)
            P_S("beach where you take a moment to scrunch your toes", 2)
            P_S("in the sand.", 2)
            P_S("   When you have had enough, you tell the computer to", 2)
            P_S("shut down and open the door. You go and stand outside", 2)
            P_S("on the corridor.", 2)
            P_S("   You feel refreshed and ready for your adventure to", 2)
            P_S("continue, you gain 1 health.", 2)
            Stats(+1)
            break
        elif OTTF.lower() == "2" or OTTF.lower() == "two":
            P_S("The Holodeck transports you to your home back on Earth", 2)
            P_S("where all of your family are stood around you smiling.", 2)
            P_S("You take a moment to smile at each one in turn.", 2)
            P_S("   When you have had enough, you tell the computer to", 2)
            P_S("shut down and open the door. You go and stand outside", 2)
            P_S("on the corridor.", 2)
            P_S("   You feel refreshed and ready for your adventure to", 2)
            P_S("continue, you gain 1 health.", 2)
            Stats(+1)
            break
        elif OTTF.lower() == "3" or OTTF.lower() == "three":
            P_S("The Holodeck transports you to an exact replica of the", 2)
            P_S("captain's cabin on board. You launch yourself on to the", 2)
            P_S("extra-large bed and rest for a moment with your head on", 2)
            P_S("the feather pillows.", 2)
            P_S("   When you have had enough, you tell the computer to", 2)
            P_S("shut down and open the door. You go and stand outside", 2)
            P_S("on the corridor.", 2)
            P_S("   You feel refreshed and ready for your adventure to", 2)
            P_S("continue, you gain 1 health.", 2)
            Stats(+1)
            break
        elif OTTF.lower() == "4" or OTTF.lower() == "four":
            P_S("You tell the computer to shut down and open the door.", 2)
            P_S("You go and stand outside on the corridor.", 2)
            break
        else:
            print("That response does not compute. Please try again.")
    # Log users presence in this room
    PreviousRoom = "1_1NE"
    # Path information
    P_S("From where you are outside the Holodeck, you can go down the", 2)
    P_S("corridor to the left towards port or the right towards starboard.", 2)
    P_S("There is also a room directly in front of you which has the sign", 2)
    P_S("'Captain's Quarters' above it. Where would you like to go?", 2)
    # Choice of where to go to
    ThreeRoomChoice("To port", "Into the Captain's Quarters", "To starboard",
                    Room1_1N, RoomNNE, RoomENE)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(Room1_1N, RoomNNE, RoomENE)


def Room1_1SE():
    # SICKBAY------------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1S":
        # Travel text from 1_1S (Thrusters Control) to 1_1SE (Sickbay)
        P_S("You head along an internal corridor towards the starboard", 2)
        P_S("quarter of the ship and notice there are lots of health", 2)
        P_S("related posters down here. You stop and look at one... 'The", 2)
        P_S("dangers of Cobalt Diselenide (if you're human)' You come to", 2)
        P_S("a large pair of glass double sliding doors and go through.", 2)
    elif PreviousRoom == "SSE":
        # Travel text from SSE (Maintenance) to 1_1SE (Sickbay)
        P_S("You go through the door towards starboard and expect to find", 2)
        P_S("the corridor that leads to your personal quarters... You are", 2)
        P_S("stunned to realise that...", 2)
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
    if PreviousRoom == "SSE":
        P_S("You look behind you and you find that you have just stepped", 2)
        P_S("out of the Sickbay medical storeroom! This makes no sense -", 2)
        P_S("you were just in maintenance! You head into sickbay and close", 2)
        P_S("the door behind you.", 2)
    if FirstVisits["1_1SE"] is True:
        # Text for user's first visit to this room
        P_S("You look around Sickbay... You accidentally knock over a tray", 2)
        P_S("of operating tools in your haste to look around. You quickly", 2)
        P_S("look through some of the cupboards. You find an energy bar", 2)
        P_S("high in electrolytes and quickly eat it before continuing on", 2)
        P_S("your way. You gained 1 health.", 2)
    # Log that user has now visited this room
        FirstVisits["1_1SE"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You head into sickbay and notice that the operating tools you", 2)
        P_S("knocked over on your last visit are sat neatly in their", 2)
        P_S("original positions on the sterile tray. You quickly head over", 2)
        P_S("to the same cupboard you found the energy bar in before, but", 2)
        P_S("in your haste knock the operating tools over again! You open", 2)
        P_S("up the cupboard and find the energy bar sat there as if you", 2)
        P_S("had never taken it in the first place. You eat it again,", 2)
        P_S("grateful for any extra energy. You gained 1 health.", 2)
    Stats(+1)
    # Path Information
    P_S("From sickbay you have three options of where you can go: There is", 2)
    P_S("a door directly across the corridor labelled 'Maintenance', there", 2)
    P_S("is a door on the starboard wall labelled 'Medical Store' or you", 2)
    P_S("can head towards the bow of the ship via the other exit from", 2)
    P_S("Sickbay. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_1SE"
    # Choice of where to go to
    ThreeRoomChoice("Towards the Bow of the ship",
                    "Through the door labelled 'Medical Store'",
                    "Through the door labelled 'Maintenance'",
                    Room1_1E, RoomESETransporterRoom, RoomSSE)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(Room1_1E, RoomESETransporterRoom, RoomSSE)


def Room1_1SW():
    # CREW QUARTERS------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1W":
        # Travel text from 1_1W (Science Bay) to 1_1SW (Crew Quarters)
        P_S("From the Science Bay you head towards the stern of the ship,", 2)
        P_S("clutching your arm where the Neural Parasite attacked you.", 2)
        P_S("You head around a long curved corridor and come to another", 2)
        P_S("corridor labelled 'Crew Quarters' - you go down it, there", 2)
        P_S("could be something useful in one of the crews rooms.", 2)
    elif PreviousRoom == "SSW":
        # Travel text from SSW (Security) to 1_SW (Crew Quarters)
        P_S("You leave security through the door on the right and expect", 2)
        P_S("to go into the Brig, but to add to the list of strange things", 2)
        P_S("happening on this ship, you find yourself somewhere", 2)
        P_S("completely wrong for the layout of the ship...", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in a Crew Member's Quarters area.")
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
        P_S("You have never been to the crew quarters before - as you are", 2)
        P_S("classed as an officer, you have your own private quarters", 2)
        P_S("close to engineering in case of emergency call-outs.", 2)
        P_S("   You head along the crew quarters corridor, testing doors", 2)
        P_S("as you go and find that the majority of them are locked. You", 2)
        P_S("eventually come to one that isn't locked and go inside.", 2)
        P_S("Quickly, you search around looking for anything that might be", 2)
        P_S("useful for you.", 2)
        P_S("   You find a half-drunk cup of tea... as much as you are", 2)
        P_S("tempted, you can't bring yourself to drink it, so you place", 2)
        P_S("it back onto the windowsill. As you do you notice a piece", 2)
        P_S("of Moba Fruit wrapped in cellophane on the shelf next to you.", 2)
        P_S("The crew member who stayed in here must have been Bajoran.", 2)
        P_S("You wolf down the Moba Fruit grateful for the ample fluid it", 2)
        P_S("contains. You gained 1 health", 2)
        Stats(+1)
        P_S("Careful not to waste any more time, you head back", 2)
        P_S("outside the room.", 2)
        # Log that user has now visited this room
        FirstVisits["1_1SW"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You start to try the doors to the different crew members", 2)
        P_S("rooms and find (like last time) that the majority of them", 2)
        P_S("are locked. You jog forward and head into the one room you", 2)
        P_S("are sure is open. You head straight for the Moba Fruit and", 2)
        P_S("eat it as quickly as you can before heading back outside.", 2)
        P_S("You gain 1 health.", 2)
        Stats(+1)
    # Path information
    P_S("From here, you know that if you go further into the crew quarters", 2)
    P_S("area and further towards the port side of the ship there is the", 2)
    P_S("Recreation Room (note this is where the asteroid hit!). Or you", 2)
    P_S("can go back to the entrance of the crew area corridor and take", 2)
    P_S("the corridor opposite to go towards the stern of the ship or turn", 2)
    P_S("left to go starboard. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_1SW"
    # Choice of where to go to
    ThreeRoomChoice("Towards the Starboard",
                    "Down the opposite corridor towards the Stern",
                    "Into the Recreation Room",
                    Room1_1S, RoomSSW, RoomWSW)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(Room1_1S, RoomSSW, RoomWSW)


def Room1_1NW():
    # OBSERVATION DECK---------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1N":
        # Text from 1_1N (Meeting Room) to 1_1NW (Observation Deck)
        P_S("You head past the open end of the corridor on your right and", 2)
        P_S("into the observation deck.", 2)
    elif PreviousRoom == "NNW":
        # Travel text from NNW (The Bridge) to 1_1NW (Observation Deck)
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
        P_S("You head into the vast room. Straight ahead of you there is", 2)
        P_S("the Observation window which spans across the whole width of", 2)
        P_S("the room, at a guess you'd probably say about 20 meters.", 2)
        P_S("   It is a very peaceful room and always so quiet no matter", 2)
        P_S("how many people have been in here. You head over to the", 2)
        P_S("window and sit on the plush seating behind you.", 2)
        P_S("   You take a moment just to catch your breath and gather", 2)
        P_S("your thoughts before continuing on your journey.", 2)
        # Log that user has now visited this room
        FirstVisits["1_1NW"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You head onto the Observation Deck and take a moment to just", 2)
        P_S("watch through the window at the great expanse of space, you", 2)
        P_S("take a few deep breaths and gather your thoughts before", 2)
        P_S("carrying on.", 2)
    P_S("Feeling refreshed, you gain 1 health.", 2)
    Stats(+1)
    # Path information
    P_S("From the Observation deck, you can go down the corridor just", 2)
    P_S("outside and to the left which will head towards the port-bow.", 2)
    P_S("You also have the option of going further to port or to stern.", 2)
    P_S("Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_1NW"
    # Choice of where to go to
    ThreeRoomChoice("Towards the stern", "Towards the port",
                    "Towards the port-bow",
                    Room1_1W, RoomWNW, RoomNNW)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(Room1_1W, RoomWNW, RoomNNW)


# Rooms around the outside of the map (not including transporter room)---------
def Room1_2N():
    # SHUTTLE BAY--------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1N":
        # Travel text from 1_1N (Meeting Room) to 1_2N (Shuttle Bay)
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
    # Text for every visit to this room
    P_S("You look around for a little while and find a snack bar, you", 2)
    P_S("are very hungry, so quickly un-wrap the snack and wolf it", 2)
    P_S("down. You gain 1 health.", 2)
    Stats(+1)
    KeepLooking = False
    while not KeepLooking:
        YesOrNo = input('Do you want to keep searching this room? (Y/N):\n')
        if YesOrNo.lower() == 'yes' or YesOrNo.lower() == "y":
            # If user chooses to keep looking around - game over!
            P_S("You head deeper into the Shuttle Bay and rummage through", 2)
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
            P_S("your eyes and lose consciousness.", 2)
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
                # Log users presence in the meeting room NOT the shuttle bay
                PreviousRoom = "1_1N"
                # Choice of where to go to
                ThreeRoomChoice("The Observation deck",
                                "To the Port Bow",
                                "To the Starboard Bow",
                                Room1_1NW, RoomNNW, RoomNNE)
                # If user inputs invalid value - re-ask question
                ThreeRoomSecondChance(Room1_1NW, RoomNNW, RoomNNE)
            elif PreviousRoom == "NNW":
                P_S("You head back into the Bridge", 2)
                P_S("Where would you like to go from here?", 2)
                # Log users presence on the bridge NOT the shuttle bay
                PreviousRoom = "NNW"
                # Choice of where to go to
                TwoRoomChoice("The Observation Deck",
                              "Back into the Shuttle Bay",
                              Room1_1NW, Room1_2N)
                # If user inputs invalid value - re-ask question
                TwoRoomSecondChance(Room1_1NW, Room1_2N)
            else:
                Error()
        else:
            print("That response does not compute.")


def Room1_2E():
    # WEAPONS CONTROL----------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "ENE":
        # Travel text from ENE (Navigation) to 1_2E (Weapons Control)
        P_S("You go through the newly appeared door and go down an ", 2)
        P_S("external corridor. You go into the next room you come to.", 2)
    elif PreviousRoom == "1_1E":
        # Travel text from 1_1E (Eng.Sub.Con) to 1_2E (Weapons Control)
        P_S("You go through the door straight ahead of you towards the", 2)
        P_S("starboard side of the ship, you go down a corridor with", 2)
        P_S("many warning signs and posters about the correct use of", 2)
        P_S("photon torpedoes. You head into the next room you come to", 2)
        P_S("straight ahead of you.", 2)
    elif PreviousRoom == "1_2SE":
        # Text from 1_2SE (Personal Quarters) to 1_2E (Weapons Control)
        P_S("You head through your closet door which opens up onto an", 2)
        P_S("outer corridor of the ship. With your personal quarters", 2)
        P_S("behind you, you walk a little further and head into the next", 2)
        P_S("room on your left. Given everything crazy going on in the", 2)
        P_S("ship, you don't know which room you're going in to...", 2)
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
        P_S("You poke your head round the door, making sure the coast is", 2)
        P_S("clear of anything untoward before you go in... Everything", 2)
        P_S("seems fine to you, so you head into the room.", 2)
        P_S("   Surely in weapons control there must be something to help", 2)
        P_S("defend yourself? As you look around you find nothing but", 2)
        P_S("safety booklets and instructions on correct sequence of", 2)
        P_S("events needed to fire the photon torpedoes.", 2)
        P_S("   You shake your head in frustration and keep on looking.", 2)
        P_S("After a little while you start to feel a bit funny, your", 2)
        P_S("hands start to shake and take on a life of their own grabbing", 2)
        P_S("things of the shelves and throwing them across the room.", 2)
        P_S("   Just as soon as this strange behaviour started, it stops", 2)
        P_S("again. You rack your brain trying to figure out what could", 2)
        P_S("have been the cause and can only think that with the black", 2)
        P_S("hole interference and the space-time anomalies that are", 2)
        P_S("occurring, it could have attracted a Dark Matter Lifeform.", 2)
        P_S("Thankfully it didn't do too much damage to you and left", 2)
        P_S("fairly soon. You lose 1 Health.", 2)
        Stats(-1)
        CheckStats()
        # Log that user has now visited this room
        FirstVisits["1_2E"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You head inside the room and find you are in the Weapons", 2)
        P_S("Control room again, before you can make a hasty retreat so", 2)
        P_S("as to not have a repeat performance of the Dark Matter", 2)
        P_S("Lifeform taking control of your body...", 2)
        P_S("   You once again find yourself incapable of free will.", 2)
        P_S("The creature directs you toward the photon torpedo controls.", 2)
        P_S("You have no idea what buttons you are pressing, but the", 2)
        P_S("creature certainly does. You see Nova VII appear on the", 2)
        P_S("screen. You can't believe it! This thing that's possessing", 2)
        P_S("you wants to target and destroy the only chance you have of", 2)
        P_S("escaping this ship before it implodes!", 2)
        P_S("   You gather all of you mental strength to not press the", 2)
        P_S("'fire' button just as your hand hovers above it.", 2)
        P_S("You nose starts to bleed with the intensity of your will", 2)
        P_S("to not move your hand. Just as quick as it possessed you,", 2)
        P_S("it leaves your body again. But not without taking its toll", 2)
        P_S("on your mind. You lose 2 health.", 2)
        Stats(-2)
        CheckStats()
    P_S("You take a moment to catch your breath before heading outside of", 2)
    P_S("the room to think about your next path.", 2)
    # Path information
    P_S("From where you are outside of weapons control on the large", 2)
    P_S("external corridor, there is a sign for the main ship storeroom", 2)
    P_S("at the starboard-bow of the ship, there is also an internal", 2)
    P_S("corridor next to weapons control that will head back to the", 2)
    P_S("centre of the ship, or the next room heading to the stern of", 2)
    P_S("the ship is the transporter room. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_2E"
    # Choice of where to go to
    ThreeRoomChoice("Back to the centre of the ship",
                    "The ship storeroom",
                    "The Transporter Room",
                    RoomEngineBay, Room1_2NE, RoomESETransporterRoom)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(RoomEngineBay, Room1_2NE, RoomESETransporterRoom)


def Room1_2S():
    # THE BRIG-----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "SSE":
        # Travel text from SSE (Maintenance) to 1_2S (The Brig)
        P_S("You head along a short internal corridor and into the", 2)
        P_S("next room on your right.", 2)
    elif PreviousRoom == "1_1S":
        # Travel text from 1_1S (Thrusters Control) to 1_2S (The Brig)
        P_S("You head through the door behind you on the rear wall of", 2)
        P_S("Thrusters control. As you push the door open you know", 2)
        P_S("instantly that this door has been affected by the black-", 2)
        P_S("hole. As you open it, the door starts to ripple. You look", 2)
        P_S("through the doorframe and almost as if there is a thin sheet", 2)
        P_S("of water there, the room on the other side looks distorted.", 2)
        P_S("You take a deep breath and step through the transparent", 2)
        P_S("barrier and into the next room.", 2)
    elif PreviousRoom == "1_2SW":
        # Travel text from 1_2SW (Mess Hall) to 1_2S (The Brig)
        P_S("You head through the door in front of you and into a", 2)
        P_S("corridor which seems to be pulsing with life. Objects", 2)
        P_S("around you are disappearing and reappearing, there is only", 2)
        P_S("one door at the end of this corridor, so you push your way", 2)
        P_S("through it and into the next room.", 2)
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
        P_S("All around you in this huge almost circular room there", 2)
        P_S("are cells made to detain prisoners. For the majority of", 2)
        P_S("the cells, the forcefields made to close the cell off are", 2)
        P_S("disappearing and reappearing much the same as you have seen", 2)
        P_S("in other areas of the ship.", 2)
        P_S("   You head over to the cell control station and have a look", 2)
        P_S("in the drawers and cupboards surrounding it. As you search,", 2)
        P_S("you begin to feel very tired, your body becomes deprived of", 2)
        P_S("all energy and you slump to the floor with your back against", 2)
        P_S("the desk.", 2)
        P_S("   With what little energy you have left you open your eyes", 2)
        P_S("to see the tail-end mist of a Dikironium Cloud floating", 2)
        P_S("through the back wall of one of the cells.", 2)
        P_S("   You close your eyes and pass out, not knowing if or when", 2)
        P_S("you might wake up again... You lost 3 health.", 2)
        Stats(-3)
        CheckStats()
        P_S("...", 2)
        P_S("...", 2)
        P_S("Not knowing how long you were out for, your eyes flutter", 2)
        P_S("open. There is no sign of the Dikironium cloud. You slowly", 2)
        P_S("push yourself into a kneeling position, and then use the desk", 2)
        P_S("for support as you make your way to your feet. Feeling dizzy", 2)
        P_S("but okay, you look around for your next path.", 2)
        # Log that user has now visited this room
        FirstVisits["1_2S"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You head into the room, remembering with fear the encounter", 2)
        P_S("you had with the Dikironium Cloud last time. Do you want to", 2)
        StayHere = False
        while not StayHere:
            YesOrNo = input('stay in here and look around again? (Y/N):\n')
            if YesOrNo.lower() == 'yes' or YesOrNo.lower() == "y":
                P_S("You decide this time to stay away from the desk and", 2)
                P_S("look around the cells instead. You head over to the", 2)
                P_S("cells and peer into each one when the forcefield is", 2)
                P_S("non-existent.", 2)
                P_S("   On peering into the 4th cell along, you notice a", 2)
                P_S("small package under the bed in the corner. Your", 2)
                P_S("curiosity gets the better of you and you head inside", 2)
                P_S("the cell to see what it is.", 2)
                P_S("   You unwrap the package and find two rolls of bread", 2)
                P_S("they seem fresh, so you sit on the bed and rip them", 2)
                P_S("apart, eating them bit-by-bit.", 2)
                P_S("   Feeling full, you gain 1 health.", 2)
                Stats(+1)
                P_S("You step out of the cell and look for you next path.", 2)
                break
            if YesOrNo.lower() == 'no' or YesOrNo.lower() == "n":
                P_S("You start to back out of the room onto the main", 2)
                P_S("corridor, looking around you for any signs of attack.", 2)
                P_S("   Just as you near the exit, you spot it! It's", 2)
                P_S("heading straight for you! You turn quickly and run", 2)
                P_S("for the exit while watching the cloud glide towards", 2)
                P_S("you... not fully aware of your surroundings. You run", 2)
                P_S("headfirst into the exit doorframe and knock yourself", 2)
                P_S("out cold. You lost 2 health.", 2)
                Stats(-2)
                CheckStats()
                P_S("   As you come round, thankfully the Dikironium cloud", 2)
                P_S("is no longer here, so you pull yourself up using the", 2)
                P_S("door handle and look around for your next path.", 2)
                break
    # Path Information
    P_S("You look around the brig and plan your next move. There are four", 2)
    P_S("doorways in this room, but two of them are distorting and ", 2)
    P_S("shrinking so you rule them out as potential exits. The other two", 2)
    P_S("doors are on opposite sides of the room - one heading to port,", 2)
    P_S("and the other to starboard. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_2S"
    # Choice of where to go to
    TwoRoomChoice("To starboard", "To port",
                  Room1_2SE, RoomSSW)
    # If user inputs invalid value - re-ask question
    TwoRoomSecondChance(Room1_2SE, RoomSSW)


def Room1_2W():
    # SCIENCE STORE------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1W":
        # Travel text from 1_1W (Science Bay) to 1_2W (Science Store)
        P_S("You head towards the door labelled 'Science Store' and", 2)
        P_S("turn the handle. You push the door open slowly just in case", 2)
        P_S("theres something else in here that wants to attack you.", 2)
    elif PreviousRoom == "1_2NW":
        # Text from 1_2NW (Meditation Room) to 1_2W (Science Store)
        P_S("You leave the meditation room feeling refreshed and ready", 2)
        P_S("for whatever this ship might throw at you. You head", 2)
        P_S("along an external corridor and come to the next door", 2)
        P_S("on your left, labelled 'Science Store', you pull down the", 2)
        P_S("handle and push the door open to go inside.", 2)
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Science Storeroom.")
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
        P_S("You head into the room which is a room about as big as the", 2)
        P_S("Engine Bay! The shelves are filled will all manners of jars,", 2)
        P_S("boxes, files and corpses of hundreds of Genesis Worms.", 2)
        P_S("   You walk along the rows of shelves searching for anything", 2)
        P_S("that could be of use. You move things around on the shelves,", 2)
        P_S("pushing things to the sides to have a better look at other", 2)
        P_S("things that are behind.", 2)
        P_S("   Out of the corner of your eye you notice something moving.", 2)
        P_S("You start to turn to head back towards the exit but find", 2)
        P_S("you're surrounded by the things you thought were corpses of", 2)
        P_S("creatures actually aren't dead. They're very much alive, and", 2)
        P_S("seem very interested in you!", 2)
        P_S("   The genesis worms slither towards you all wanting a taste", 2)
        P_S("of your human flesh.", 2)
        # Log that user has now visited this room
        FirstVisits["1_2W"] = False
    else:
        # Text for user's subsequent visit to this room
        print("Subsequent visit text here")
    if UserStats["phaser"] is True:
        P_S("You pull out your phaser and start shooting the Genesis", 2)
        P_S("Worms. As you back away from the horde of creatures, you", 2)
        P_S("look around you for any potential exits. There are three...", 2)
        P_S("one to your left heading towards the bow of the ship, one", 2)
        P_S("behind you which is in the direction you're already going.", 2)
        P_S("Or you can run back through the Science Bay and into the", 2)
        P_S("Engine Bay. You keep shooting at the worms, holding them", 2)
        P_S("back as you make your decision.", 2)
    elif UserStats["knife"] is True and UserStats["phaser"] is False:
        P_S("You pull your knife from your belt and start slashing at the", 2)
        P_S("Genesis Worms. As you back away from the horde of creatures,", 2)
        P_S("you look around you for any potential exits. There are", 2)
        P_S("three... one to your left heading towards the bow of the", 2)
        P_S("ship, one behind you which is in the direction you're", 2)
        P_S("already going. Or you can run back through the Science Bay", 2)
        P_S("and into the Engine Bay. You keep slashing at the worms,", 2)
        P_S("attempting to hold them back. As you make your decision", 2)
        P_S("the Genesis Worms lunge at you, catching your hands and", 2)
        P_S("arms with their fangs, but recoil away when your knife", 2)
        P_S("finds their fleshy bodies.", 2)
        Stats(-1)
        CheckStats()
    else:
        P_S("You raise your fists, you wish you had a weapon to help", 2)
        P_S("defend yourself! You back away from the creatures with", 2)
        P_S("your hands raised, but the Genesis Worms lunge at you,", 2)
        P_S("attaching themselves to your flesh with their suckers and", 2)
        P_S("fangs and begin to feed from you.", 2)
        P_S("   You look around you for any potential exits. There are", 2)
        P_S("three... one to your left heading towards the bow of the", 2)
        P_S("ship, one behind you which is in the direction you're", 2)
        P_S("already going. Or you can run back through the Science Bay", 2)
        P_S("and into the Engine Bay. You pull at the creatures that,", 2)
        P_S("are latched onto you, pulling them from your skin leaving", 2)
        P_S("welts and bruises where they fed from you. You throw them", 2)
        P_S("to the floor, punching and kicking with everything you have", 2)
        P_S("attempting to hold them back. As you make your decision", 2)
        P_S("the Genesis Worms lunge at you, catching your hands and", 2)
        P_S("arms with their fangs, but recoil away when you flail your", 2)
        P_S("limbs and catch their bodies with the force of your terror.", 2)
        Stats(-2)
        CheckStats()
    # Path information
    print("Where would you like to go?")
    # Log users presence in this room
    PreviousRoom = "1_2W"
    # Choice of where to go to
    ThreeRoomChoice("The direction you're already going",
                    "Towards the bow of the ship",
                    "Through the Science Bay and into the Engine Bay",
                    Room1_2SW, RoomWNW, RoomEngineBay)
    # If user inputs invalid value - re-ask question
    ThreeRoomSecondChance(Room1_2SW, RoomWNW, RoomEngineBay)


def Room1_2NE():
    # STOREROOM----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2E":
        # Travel text from 1_2E (Weapons Control) to 1_2NE (Storeroom)
        P_S("You follow the signs for the Storeroom and head towards the", 2)
        P_S("starboard bow. The storeroom is in front of you. You push", 2)
        P_S("the door open and go inside.", 2)
    elif PreviousRoom == "NNE":
        # Travel text from NNE (Captains Quarters) to 1_2NE (Storeroom)
        P_S("Leaving the Captain's Quarters behind you, you turn to your", 2)
        P_S("left and along a short internal corridor. The storeroom is on", 2)
        P_S("your left. You push the door open and go inside.", 2)
    P_S("\n-------------------------------------------\n", 3)
    P_S("You are in the Ship Storeroom.", 2)
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
    # Text for user's ONLY visit to the Storeroom
    P_S("As you enter the storeroom, you feel uneasy. You quickly look", 2)
    P_S("around to see if there's anything that might be of use to you.", 2)
    P_S("...", 2)
    P_S("You hear a faint rumbling. You look up as the rumbling seems to", 2)
    P_S("be coming from the ceiling.", 2)
    P_S("   You start to make your way back to the exit when your path is", 2)
    P_S("blocked by an avalanche of fluffy round balls falling from the", 2)
    P_S("now cracked open ceiling.", 2)
    P_S("   There's nothing you can do as you are quickly and surely", 2)
    P_S("surrounded by Tribbles. In a matter of seconds you are barely a", 2)
    P_S("head above them as they continue to pour out of the now gaping", 2)
    P_S("holes in the ceiling.", 2)
    P_S("   Just before your eyes are covered by the masses of fur, you", 2)
    P_S("can't help but think that of all the ways to die... suffocated", 2)
    P_S("by Tribbles wasn't the way you thought you'd go.", 2)
    P_S("   You close your eyes and sucomb to the fluffy onslaught.", 2)
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
        # Text from ESE (Transporter Room) to 1_2SE (Personal Quarters)
        P_S("You leave the transporter room and turn right. You head along", 2)
        P_S("the wide external corridor for a short while and come to the", 2)
        P_S("officers quarters corridor. You head down it and the third", 2)
        P_S("door on the left is your personal quarters. You head inside.", 2)
    elif PreviousRoom == "1_2S":
        # Travel text from 1_2S(The Brig) to 1_2SE (Personal Quarters)
        P_S("You take the door to starboard and find youself in the", 2)
        P_S("engineers quarters. You look around for a second to get your", 2)
        P_S("bearings and head into your personal quarters which are just", 2)
        P_S("to your left.", 2)
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
        P_S("You step inside the familiar room and take a moment to", 2)
        P_S("catch your breath by just sitting on your bed for a moment.", 2)
        P_S("   The family photos that you have sat on your bedside table", 2)
        P_S("catch your eye. You pick one up to look at the happy faces", 2)
        P_S("of your family surrounding you on your graduation day from", 2)
        P_S("Starfleet Academy. It feels like a lifetime ago.", 2)
        P_S("   You set the picture back down on the surface and pick up", 2)
        P_S("the letter than was next to it. Your mother placed this in", 2)
        P_S("your bag as you left for the Star Base on your first day.", 2)
        print("")
        P_S(f"\x1B[3mDear {name},", 2)
        P_S("   That's what they'll be calling you in Starfleet now isn't", 2)
        P_S("it? I'm going to miss you with all my heart while you are", 2)
        P_S("away. Remember how much we all love you, and as much as we", 2)
        P_S("are proud of who you are and what you have acheived, the", 2)
        P_S("most we could ever ask for is your safe return home.", 2)
        print("")
        P_S("   Love always and forever,", 2)
        P_S("       Your loving mother x.\x1B[0m", 2)
        print("")
        P_S("You fold up the letter and place it in your pocket as a", 2)
        P_S("solitary tear slides down your cheek.", 2)
        P_S("   Reaching under your bed, you pull out a small package", 2)
        P_S("wrapped in a linen sheet and carefully unfold it in your", 2)
        P_S("lap. You look down at your knees and can't help but smile", 2)
        P_S("at the small pile of cherry bakewells that your mother", 2)
        P_S("somehow managed to send to you a couple of days ago when", 2)
        P_S("the ship restocked at its last outpost.", 2)
        P_S("   You pick one up and take the foil off before putting", 2)
        P_S("the small tart into your mouth in one whole piece.", 2)
        P_S("   Reminded of home and filled with new determination", 2)
        P_S("to escape the crippled ship, you gain 3 health.", 2)
        Stats(+3)
        P_S("You neatly fold the package back up and place it back under", 2)
        P_S("your bed.", 2)
        # Log that user has now visited this room
        FirstVisits["1_2SE"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You head into your personal quarters and kneel on the floor", 2)
        P_S("next to your bed. You pull out the folded package of cherry", 2)
        P_S("bakewells and eat another one whole. You gain 2 health.", 2)
        Stats(+2)
        P_S("You neatly fold the package back up and place it back under", 2)
        P_S("your bed.", 2)
    # Path information
    P_S("From where you are in the engineer's quarters, you can head back", 2)
    P_S("onto the external corridor and past the Transporter room towards", 2)
    P_S("the bow of the ship. Or you can head along the stern of the ship", 2)
    P_S("and into maintenance.", 2)
    # Log users presence in this room
    PreviousRoom = "1_2SE"
    # Choice of where to go to
    TwoRoomChoice("Past the Transporter Room towards the Bow",
                  "To maintenance",
                  Room1_2E, RoomSSE)
    # If user inputs invalid value - re-ask question
    TwoRoomSecondChance(Room1_2E, RoomSSE)


def Room1_2SW():
    # MESS HALL----------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "SSW":
        # Travel text from SSW (Security Quarters) to 1_2SW (Mess Hall)
        P_S("With Security behind you, you head down the wide external", 2)
        P_S("corridor towards the Mess Hall.You go through the sliding", 2)
        P_S("double doors and are greeted with the recent smells of", 2)
        P_S("freshly cooked dinner.", 2)
    elif PreviousRoom == "1_2W":
        # Travel text from 1_2W (Science Store) to 1_2SW (Mess Hall)
        P_S("You keep heading towards the door behind you while fending", 2)
        P_S("off the Genesis Worms. You fumble for the door handle and", 2)
        P_S("squeeze through the smallest gap you can in the door to stop", 2)
        P_S("any of the creatures following you.", 2)
        P_S("   You slam the door after you and fall to the ground not yet", 2)
        P_S("knowing which room you have fallen into. You make your way to", 2)
        P_S("your feet and are greeted with the beautiful smells of", 2)
        P_S("cooked dinner.", 2)
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
        P_S("The large room is completely empty of people but is full", 2)
        P_S("of multiple sized tables, chairs and sofas, with an extra", 2)
        P_S("long sofa running the full length of the room beneath the", 2)
        P_S("window. You head over to the serving counter and grab a plate", 2)
        P_S("of your favourite foods.", 2)
        P_S("   You take a moment to sit down and have a few mouthfulls", 2)
        P_S("before you continue on your journey. You gain 2 health.", 2)
        Stats(+2)
        # Log that user has now visited this room
        FirstVisits["1_2SW"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("The Mess Hall is just as empty as it was the first time you", 2)
        P_S("visited. You head over to the table you were sat at during", 2)
        P_S("your first visit and grab a few more peices of food from the", 2)
        P_S("plate you put together. You gain 1 health.", 2)
        Stats(+1)
    # Path information
    P_S("From the Mess Hall you have two potential exits: The door in the", 2)
    P_S("corner that leads to the recreation room or the door in front of", 2)
    P_S("you that you think will lead to the centre of the ship. As you", 2)
    P_S("look at the door to the recreation room, it seems to pulsate and", 2)
    P_S("ripple, but looks fairly permanent. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_2SW"
    # Choice of where to go to
    TwoRoomChoice("Towards the centre of the ship",
                  "To the recreation room",
                  Room1_2S, RoomWSW)
    # If user inputs invalid value - re-ask question
    TwoRoomSecondChance(Room1_2S, RoomWSW)


def Room1_2NW():
    # MEDITATION ROOM----------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "WNW":
        # Text from WNW (Conference Lounge) to 1_2NW (Meditation)
        P_S("You make you way down the short internal corridor and into", 2)
        P_S("the next room on your left.", 2)
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
        P_S("You are in a small comfortable room with a plush chaise", 2)
        P_S("lounge in the middle and a Chesterfield winged chair to its", 2)
        P_S("side. A large wooden bookcase sits along the back wall with", 2)
        P_S("a slection of bean bags in front of it.", 2)
        P_S("   The room is set in dim lighting and has an aura of", 2)
        P_S("calmness about it. You nod your head to the portrait of", 2)
        P_S("Lieutenant Commander Deanna Troi that sits above the", 2)
        P_S("fireplace and make your way to the chaise.", 2)
        P_S("   You sit down and close your eyes, taking a moment to", 2)
        P_S("catch your breath and gather your thoughts before you", 2)
        P_S("continue on your journey, you gain 2 health.", 2)
        Stats(+2)
        # Log that user has now visited this room
        FirstVisits["1_2NW"] = False
    else:
        # Text for user's subsequent visit to this room
        P_S("You head over to the chaise nodding at the portrait above", 2)
        P_S("the fireplace as you go and take a moment to have a", 2)
        P_S("few deep breaths and gather your thoughts before you", 2)
        P_S("continue on your journey. You gain 1 health.", 2)
        Stats(+1)
    # Path information
    P_S("You stand up from the chaise and head out of the room. When", 2)
    P_S("on the corridor you find yourself on a different corridor to", 2)
    P_S("the one you used to enter. You could go left towards the bow of", 2)
    P_S("the ship or go in the opposite direction towards the port side.", 2)
    P_S("Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "1_2NW"
    # Choice of where to go to
    TwoRoomChoice("Towards the bow", "Towards the port side",
                  RoomNNW, Room1_2W)
    # If user inputs invalid value - re-ask question
    TwoRoomSecondChance(RoomNNW, Room1_2W)


def RoomNNE():
    # CAPTAINS QUARTERS--------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1N":
        # Text from 1_1N (Meeting Room) to NNE (Captain's Quarters)
        P_S("Leaving the outside of the meeting room behind you, you", 2)
        P_S("head in a starboard bow direction along an internal corridor.", 2)
        P_S("You go past the elevator and come to the captain’s quarters", 2)
        P_S("on your left. You push the door open and go inside.", 2)
    elif PreviousRoom == "1_1NE":
        # Travel text from 1_1NE (Holodeck) to NNE (Captain's Quarters)
        P_S("You head across the corridor and through the door opposite.", 2)
    elif PreviousRoom == "ENE":
        # Travel text from ENE (Navigation) to NNE (Captain's Quarters)
        P_S("You go through the newly formed door on the bow wall of the", 2)
        P_S("room and head along a short corridor in a starboard bow", 2)
        P_S("direction. You come to the captain's quarters on your right,", 2)
        P_S("you push through the door and close it behind you.", 2)
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
        P_S("You have never needed to come into the captain's quarters", 2)
        P_S("before so have no idea what you might find. As much as it", 2)
        P_S("intruiges you to be in here, you want to make your visit", 2)
        P_S("quick out of respect for the captain, whom you assume to be", 2)
        P_S("dead. The room is large and comfortable with a large table", 2)
        P_S("in the middle covered in files and charts.", 2)
        P_S("   You head over to the captain's desk and open a few drawers", 2)
        P_S("down the left hand side. In the third drawer you find a KaBar", 2)
        P_S("Combat Knife! You hook it on to your belt and make your way", 2)
        P_S("out of the room.", 2)
        # Log that the user has been here before
        UserStats["knife"] = True
    elif UserStats["knife"] is True:
        # Text for subsequent visits to this room
        P_S("You look around the room even quicker than you did last", 2)
        P_S("time. This is where you found the knife. There's nothing else", 2)
        P_S("of interest in here so you head back out onto the corridor.", 2)
    else:
        Error()
    # Path information
    P_S("From where you are on the corridor you have two options, go on to", 2)
    P_S("the Holodeck or towards the starboard side of the ship - you look", 2)
    P_S("in that direction down the corridor and hear banging above you,", 2)
    P_S("perhaps that way might not be a great idea.", 2)
    # Log users presence in this room
    PreviousRoom = "NNE"
    # Choice of where to go to
    TwoRoomChoice("Towards the starboard side of the ship", 
                  "On to the Holodeck",
                  Room1_2NE, Room1_1NE)
    # If user inputs invalid value - re-ask question
    TwoRoomSecondChance(Room1_2NE, Room1_1NE)


def RoomENE():
    # NAVIGATION---------------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_1NE":
        P_S("Travel text from 1_1NE (Holodeck) to ENE (Navigation)", 2)
        P_S("You take the path to starboard - a short internal corridor,", 2)
        P_S("the walls covered in star charts and paintings of planets you", 2)
        P_S("have long since forgotten the name of since your navigation", 2)
        P_S("training at Starfeel Academy. You head through the door at", 2)
        P_S("the end of the corridor. The door opens automatically.", 2)
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
        P_S("You head over to the desk in the middle of the room.", 2)
        P_S("As the computers and screens beep around you, you", 2)
        P_S("frantically search for anything that might be of use.", 2)
        P_S("There's nothing in the desk.", 2)
        P_S("   You head over to the computers along the edges of the", 2)
        P_S("room - people left in a hurry, there's still cups of", 2)
        P_S("tea and snacks next to their workstations.", 2)
        P_S("   You bump into one of the computer chairs as you look", 2)
        P_S("around which causes it to swivel towards you. You peer", 2)
        P_S("down at the seat and can't believe your luck! You've", 2)
        P_S("found a locator device!", 2)
        # Log that the user now has possession of the locator device
        UserStats["locator"] = True
        # Text for if the user has the batteries
        if UserStats["batteries"] is True:
            P_S("\nThe locator device is completely out of battery", 2)
            P_S("but springs into life once you put the batteries", 2)
            P_S("inside and shows you a small graphic of where you", 2)
            P_S("are in the ship...", 2)
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
        P_S("This is where you found the Locator device. There is nothing", 2)
        P_S("else of interest in this room.", 2)
    else:
        Error()
    # Log users presence in this room
    PreviousRoom = "ENE"
    # Path information
    P_S("From where you are in the Navigation room you seem to have two", 2)
    P_S("exit choices. The door you came through has since disappeared,", 2)
    P_S("but there are doors on two of the walls that have appeared in", 2)
    P_S("its place. From a quick look out of the window you can tell", 2)
    P_S("that one is heading in a bow direction and the other to stern.", 2)
    P_S("Where would you like to go?", 2)
    # Choice of where to go to
    TwoRoomChoice("Through the door on the bow wall", 
                  "Through the door on the stern wall",
                  RoomNNE, Room1_2E)
    # If user inputs invalid value - re-ask question
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
            P_S("about in the commotion as I woke up on the floor and", 2)
            P_S('things were all over the place!', 2)
            P_S("\nYou wait anxiously for Clancy to respond.\n", 2)
            P_S('"Yes, I heard all about it! I managed to get some of your', 2)
            P_S("crew to safety down here on Nova VII before your ship", 2)
            P_S("wide comms and transporter went offline. I can help you", 2)
            P_S("get out, but you'll need to find a locator device on", 2)
            P_S("board so I can pinpoint your location. You'll also need", 2)
            P_S("the Transporter override key so I can access it remotely.", 2)
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
            P_S("about in the commotion as I woke up on the floor and", 2)
            P_S('things were all over the place!', 2)
            P_S("\nYou wait anxiously for Clancy to respond.\n", 2)
            P_S('"Yes, I heard all about it! I managed to get some of your', 2)
            P_S("crew to safety down here on Nova VII before your ship", 2)
            P_S("wide comms and transporter went offline. I can help you", 2)
            P_S("get out, but you'll need to find a locator device on", 2)
            P_S("board so I can pinpoint your location. You'll also need", 2)
            P_S("the Transporter override key so I can access it remotely.", 2)
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
    # Log users presence in this room
    PreviousRoom = "SSE"
    # Path information
    print("PATH INFO HERE")
    # Choice of where to go to
    TwoRoomChoice("Room1_1SE", "Room1_2S",
                  Room1_1SE, Room1_2S)
    # If user inputs invalid value - re-ask question
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
        P_S("The Enterprise, you have only seen this key a handful of", 2)
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
    # Log users presence in this room
    PreviousRoom = "SSW"
    # Path information
    print("PATH INFO HERE")
    # Choice of where to go to
    TwoRoomChoice("Room1_1SW", "Room1_2SW",
                  Room1_1SW, Room1_2SW)
    # If user inputs invalid value - re-ask question
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
    # Path information
    print("PATH INFO HERE")
    # Log users presence in this room
    PreviousRoom = "WNW"
    # Choice of where to go to
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
    if UserStats["comms"] is False:
        # Text for user's first visit to this room (if they don't have comms)
        P_S("You head onto the bridge. It's the first time you have ever", 2)
        P_S("seen this spectacular room empty. You head over to the", 2)
        P_S("captain's chair and run your hand over the smooth grey", 2)
        P_S("leather... you look around the room again checking for anyone", 2)
        P_S("else's presence. You smile to yourself... no one would know.", 2)
        P_S("   You slowly lower yourself into the most important chair on", 2)
        P_S("the ship and look at the viewscreen in front of you which is", 2)
        P_S("set to show the outside. In all your years in Starfleet, you", 2)
        P_S("never thought you'd find yourself sat here.", 2)
        P_S("   Standing up again, you look around to see if there's", 2)
        P_S("anything that might help you with your current plight.", 2)
        P_S("", 2)
        P_S("You found a comms device!", 2)
        # Log that the user now has possession of the comms device
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
            P_S("about in the commotion as I woke up on the floor and", 2)
            P_S('things were all over the place!', 2)
            P_S("\nYou wait anxiously for Clancy to respond.\n", 2)
            P_S('"Yes, I heard all about it! I managed to get some of your', 2)
            P_S("crew to safety down here on Nova VII before your ship", 2)
            P_S("wide comms and transporter went offline. I can help you", 2)
            P_S("get out, but you'll need the Transporter override key", 2)
            P_S("so I can access it remotely.", 2)
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
                # Text for if the user doesn't have the key or locator device
                P_S('"You will also need to find a locator device so I can', 2)
                P_S('pinpoint your exact location once you are in the', 2)
                P_S('beam transportation room."', 2)
            P_S("I have a feeling you don't have much time, your ship", 2)
            P_S(f'is highly compromised. Hurry {name}, hurry... "', 2)
            print("")
            P_S("You stow the comms device into your pocket and continue", 2)
            P_S("on your way - filled with new hope.", 2)
        elif UserStats["batteries"] is False:
            # Text for if the user doesn't have the batteries
            P_S('The comms device is completely out of batteries, "There', 2)
            P_S('should be some batteries on this ship somewhere!", you', 2)
            P_S("think to yourself.", 2)
    elif UserStats["comms"] is True:
        # Text for if user has been here before (has comms device)
        P_S("You head onto the bridge and smile at the captain's chair,", 2)
        P_S("almost going over to sit on it again.", 2)
        P_S("This is where you found the comms device. There's nothing.", 2)
        P_S("else here of interest.", 2)
    else:
        Error()
    # Path information
    P_S("As you look around The Bridge, there is a door here that has", 2)
    P_S("never been here before, you look at it uneasily, waiting for it", 2)
    P_S("to disappear as the cooling controls did in the Engine Bay, but", 2)
    P_S("it seems permanent enough. You could go through this door, or you", 2)
    P_S("could go down in the elevator, but you don't know where it would", 2)
    P_S("stop. Where would you like to go?", 2)
    # Log users presence in this room
    PreviousRoom = "NNW"
    # Choice of where to go to
    TwoRoomChoice("Down the elevator", "Through the unusual door",
                  Room1_1NW, Room1_2N)
    # If user inputs invalid value - re-ask question
    TwoRoomSecondChance(Room1_1NW, Room1_2N)


def RoomESETransporterRoom():
    # TRANSPORTER ROOM---------------------------------------------------------

    global PreviousRoom
    if PreviousRoom == "1_2E":
        # Text from 1_2E (Weapons Control) to ESE (Transporter Room)
        P_S("Leaving weapons control, you head along the outer starboard", 2)
        P_S("corridor of the ship, looking out at the starry expanse as", 2)
        P_S("you go. You head into the next room you come to.", 2)
    elif PreviousRoom == "1_1SE":
        # Travel text from 1_1SE (Sickbay) to ESE (Transporter Room)
        P_S("Leaving sickbay, you go through the door labelled 'Medical", 2)
        P_S("Store' and once again are confronted with something", 2)
        P_S("unexpected... You head along a short internal corridor.", 2)
        P_S("As you walk along, the multiple doors along this corridor", 2)
        P_S("seem to be disappearing and reappearing much the same as", 2)
        P_S("the cooling controls in the Engine Bay. You keep walking", 2)
        P_S("until you come to the only door that has some semblance of", 2)
        P_S("permanence and head through it.", 2)
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
    # Text for every visit to the transporter room
    P_S("You head over to the transporter chamber and make your way up", 2)
    P_S("the couple of steps onto the transporter platform. You never", 2)
    P_S("did like beaming much. You jog down the steps again and over", 2)
    P_S("to the transporter controls, you notice all the screens are", 2)
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
        P_S('"I have everything you said I need, and I am in the', 2)
        P_S('Transporter Room, ready to beam down!"', 2)
        P_S('"Fantastic!" replies Clancy. "Put the override key in the', 2)
        P_S('controls and hold the locator device to your chest while', 2)
        P_S('you are stood on the transporter platform".', 2)
        P_S('You head up onto the platform again. "Ready!" you shout.', 2)
        P_S('"Calculating your position, distance, mass... setting', 2)
        P_S(f'controls to manual. Okay {name}, here we go..."', 2)
    # Does the user want to attempt beaming out of the ship?
    BeamOut = False
    while not BeamOut:
        YesOrNo = input('Would you like to beam out of the ship? (Y/N):\n')
        if YesOrNo.lower() == 'yes' or YesOrNo.lower() == "y":
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
                P_S("its structural integrity and scatter across the", 2)
                P_S("heavens, some small pieces break through the", 2)
                P_S("atmosphere of Nova VII giving the planet a final ", 2)
                P_S("farewell in a symbolic meteor shower.", 2)
                P_S("You feel a hand settle on your shoulder...", 2)
                P_S('"Glad you made it out." Clancy smiles at you.', 3)
                PlayAgain = False
                while not PlayAgain:
                    YesOrNo = input('Do you want play again? (Y/N):\n')
                    if YesOrNo.lower() == 'yes' or YesOrNo.lower() == "y":
                        print("Press PLAY GAME to initialise time loop.")
                    elif YesOrNo.lower() == 'no' or YesOrNo.lower() == "n":
                        P_S(f"Live long and prosper {name}", 2)
                        P_S("Initialising shut down...", 2)
                        P_S('''
                ___ _ _ ___   ___ _ _ ___
               |_ _| | | __> | __| \ | . |
                | ||   | _>  | _>|   | | |
                |_||_|_|___> |___|_\_|___/
                    \n\n\n\n''', 2)
                        Credits()
                    else:
                        print("That response does not compute.")
            else:
                # Text for if user attempted to beam out without required items
                P_S("\nYou didn't have all the required equipment and", 2)
                P_S("items to successfully beam down to Nova VII. You", 2)
                P_S("beamed halfway down to the planet's surface but", 2)
                P_S("appeared in space before you could reach your", 2)
                P_S("destination.", 2)
                P_S('''
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
                    \n
                    ''', 1)
                Credits()
        # If user doesn't want to beam out of the ship:
        elif YesOrNo.lower() == 'no' or YesOrNo.lower() == "n":
            P_S("\nYou continue on your journey...", 2)
            # Path information
            P_S("From the Transporter room you have two options of where", 2)
            P_S("to go: Along an internal corridor towards the centre of", 2)
            P_S("the ship or an external corridor towards your personal", 2)
            P_S("quarters. Where would you like to go?", 2)
            # Log users presence in this room
            PreviousRoom = "ESE"
            # Choice of where to go to
            TwoRoomChoice("Towards the centre of the ship",
                          "Personal Quarters",
                          Room1_1E, Room1_2SE)
            # If user inputs invalid value - re-ask question
            TwoRoomSecondChance(Room1_1E, Room1_2SE)
        else:
            print("That option does not compute, please try again.")


PlayGame()
