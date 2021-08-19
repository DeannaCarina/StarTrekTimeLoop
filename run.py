# Developer: Deanna Sale
# Date of release: TBC
# Subject: Code Institute Portfolio Project 3 - Python
# Program Name: "Star Trek: Time Loop"

import time

health = 5
weapons = ["fists"]
comms = True
locator = True
transporter = True
key = True
batteries = True


def PlayGame():
    print('''
       ____ _______       _____    _______ _____  ______ _  __
     / ____|__   __|/\   |  __ \  |__   __|  __ \|  ____| |/ /
    | (___    | |  /  \  | |__) |    | |  | |__) | |__  | ' /
     \___ \   | | / /\ \ |  _  /     | |  |  _  /|  __| |  <
     ____) |  | |/ ____ \| | \ \     | |  | | \ \| |____| . |
    |_____/_ _|_/_/__  \_\_|__\_\  _ |_|  |_|_ \_\______|_|\_|
    |__   __|_   _|  \/  |  ____| | |    / __ \ / __ \|  __ |
       | |    | | | \  / | |__    | |   | |  | | |  | | |__) |
       | |    | | | |\/| |  __|   | |   | |  | | |  | |  ___/
       | |   _| |_| |  | | |____  | |___| |__| | |__| | |
       |_|  |_____|_|  |_|______| |______\____/ \____/|_|
       ''')
    print("")
    WantToPlay = input("Would you like to play? (Y/N): \n")
    if WantToPlay.lower() == "y" or WantToPlay.lower() == "yes":
        print("Commencing time loop in...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        global name
        name = input("What is your name? \n")
        print(f"Hello {name}... welcome aboard the USS Enterprise III")
        time.sleep(2)
        print("in Star Date 3167. You are the second engineer on")
        time.sleep(2)
        print("board and work the night shift. You joined")
        time.sleep(2)
        print("the ship on her maiden voyage of her 15 year mission to...")
        time.sleep(3)
        print('''
                  BOLDLY GO WHERE NONE HAVE GONE BEFORE...

          o               .        ___---___                    .
                 .              .--\        --.     .     .         .
                              ./.;_.\     __/~ \.
                             /;  / `-'  __\    . \                   
           .        .       / ,--'     / .   .;   \        |
                           | .|       /       __   |      -O-       .
                          |__/    __ |  . ;   \ | . |      |
                          |      /  \\_    . ;| \___|
             .    o       |      \  .~\\___,--'     |           .
                           |     | . ; ~~~~\_    __|
              |             \    \   .  .  ; \  /_/   .
             -O-        .    \   /         . |  ~/                  .
              |    .          ~\ \   .      /  /~          o
             .                   ~--___ ; ___--~
                 .          ---         .
                 ''')
        time.sleep(3.5)
        SkipIntro = input("Do you want to skip the intro? (Y/N): \n")
        if SkipIntro.lower() == "n" or SkipIntro.lower() == "no":
            time.sleep(2)
            print("")
            print("You have been on the ship for 6 years now,")
            time.sleep(2)
            print("and have steadily worked your")
            time.sleep(2)
            print("way up the ranks to where you are.")
            time.sleep(2.5)
            print("")
            time.sleep(2)
            print("Due to an asteroid colliding with the ship's port side,")
            time.sleep(2)
            print("The Enterprise lost control of crucial guide and")
            time.sleep(2)
            print("flight instruments, this made it impossible to steer")
            time.sleep(2)
            print("away from the nearing Black Hole, and unfortunately the")
            time.sleep(2)
            print("ship passed through the Black Hole causing massive loss of")
            time.sleep(2)
            print("life and ship damage. You wake up in the Engine Bay after")
            time.sleep(2)
            print("suffering from concussion. It seems that due to being")
            time.sleep(2)
            print("close to the Warp Core of the ship, you were")
            time.sleep(2)
            print("protected from the initial space-time anomalies.")
            time.sleep(2.5)
            print("")
            print("In the aftermath of the asteroid and passage through the")
            time.sleep(2)
            print("Black Hole, you have broken your comms device and lost")
            time.sleep(2)
            print("your locator device. Things don't seem as they should with")
            time.sleep(2)
            print("the ship - walls are rippling with life, and even as you")
            time.sleep(2)
            print("watch, things around you are dissapearing into nothingness")
            time.sleep(2)
            print("and imploding in on themselves. There is a nearby planet")
            time.sleep(2)
            print("which should be within beam distance, but without your")
            time.sleep(2)
            print("comms and locator devices the chances ofgetting there")
            time.sleep(2)
            print("safely are slim.")
            print("")
            time.sleep(3)
            print("You must search the ship for all the necessary equipment")
            time.sleep(2)
            print("before you can safely leave via the transporter room.")
            time.sleep(3)
            print("")
            print("You will need the following items to safely beam down to")
            time.sleep(2)
            print("Nova VII:")
            time.sleep(2)
            print('''1. Locator Device
                     2. Communication (Comms) Device
                     3. Batteries for Items 1 & 2
                     4. Power-on key for the transporter device''')
            print("")
            time.sleep(5)
            print("On your exploration of the ship, you might also find")
            time.sleep(3)
            print("weapons and items that will help you with healing, energy")
            time.sleep(2)
            print("levels and defending yourself.")
            time.sleep(3)
            print("")
            print(f"Good luck {name}, live long... and prosper.")
            time.sleep(3)
            print("")
            print("----------------------------------------------------------")
            print("")
            time.sleep(3)
            RoomEngineBay()
        elif SkipIntro.lower() == "y" or SkipIntro.lower() == "yes":
            print("")
            print("----------------------------------------------------------")
            print("")
            time.sleep(3)
            RoomEngineBay()
        else:
            print("That option does not compute, please try again.")
            PlayGame()
    elif WantToPlay.lower() == "n" or WantToPlay.lower() == "no":
        print("*Beaming you out*")
        time.sleep(1)
        print("Initialising shut down...")
        time.sleep(1)
        print('''
                ___ _ _ ___   ___ _ _ ___
               |_ _| | | __> | __| \ | . |
                | ||   | _>  | _>|   | | |
                |_||_|_|___> |___|_\_|___/
                ''')
        exit()
    else:
        print("That option does not compute, please try again.")
        PlayGame()


def RoomEngineBay():
    # Starting room - From here we can go to... 1_1N(1),
    # # 1_1E(2), 1_1S(3) and 1_1W(4)
    EngineBayOptions = ["1", "2", "3", "4"]
    UserChoice = ""
    while UserChoice not in EngineBayOptions:
        print("You are in the Engine Bay!")
        print('''
        ___________________          _-_             _      _-_      _
        \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                    \_ \    \----._________.----/  \----._________.----/
                      \ \   /  /    `-_-'              `.  `]-['  ,'
                  __,--`█`-'..'-_                        `.' █ `.
                 /____          ||                        | (_) |
                      `--.____,-'                          `___'
                      \n
                      █ = You are here.
        ''')
        print('''Room text here, with potential options.
        1. Option 1 (1_1N)
        2. Option 2 (1_1E)
        3. Option 3 (1_1S)
        4. Option 4 (1_1W)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == EngineBayOptions[0]:
        Room1_1N()
    elif UserChoice == EngineBayOptions[1]:
        Room1_1E()
    elif UserChoice == EngineBayOptions[2]:
        Room1_1S()
    elif UserChoice == EngineBayOptions[3]:
        Room1_1W()
    else:
        print("That it not a valid option, please chose 1, 2, 3 or 4")


def Room1_1N():
    # Rooms around the outside of the engine bay
    # Health -3 cannot be changed by weapons
    # From here we can go to... 1_1NW, NNW, 1_2N and NNE
    Room1_1N_Options = ["1", "2", "3", "4"]
    UserChoice = ""
    while UserChoice not in Room1_1N_Options:
        print("")
        print("You are in 1_1N!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1NW - Observation Deck)
        2. Option 2 (NNW - The Bridge)
        3. Option 3 (1_2N - Shuttle Bay [Kill Room])
        4. Option 4 (NNE)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1N_Options[0]:
        Room1_1NW()
    elif UserChoice == Room1_1N_Options[1]:
        RoomNNW()
    elif UserChoice == Room1_1N_Options[2]:
        Room1_2N()
    elif UserChoice == Room1_1N_Options[3]:
        RoomNNE()
    else:
        print("That it not a valid option, please chose 1, 2, 3 or 4")


def Room1_1E():
    # Health -2 unless knife (-1) or phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_1NE and 1_2E"
    Room1_1E_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1E_Options:
        print("")
        print("You are in 1_1E!")
        print('''Room text here, with potential options.
        1. Option 1 (Engine Bay)
        2. Option 2 (1_1NE - Holodeck)
        3. Option 3 (1_2E)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1E_Options[0]:
        RoomEngineBay()
    elif UserChoice == Room1_1E_Options[1]:
        Room1_1NE()
    elif UserChoice == Room1_1E_Options[2]:
        Room1_2E()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_1S():
    # Health -1 cannot be changed by weapons
    # From here we can go to... 1_1W, 1_1E, 1_1SE and 1_2S"
    Room1_1S_Options = ["1", "2", "3", "4"]
    UserChoice = ""
    while UserChoice not in Room1_1S_Options:
        print("")
        print("You are in 1_1S!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1W)
        2. Option 2 (1_1E)
        3. Option 3 (1_1SE - Sickbay)
        4. Option 4 (1_2S)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1S_Options[0]:
        Room1_1W()
    elif UserChoice == Room1_1S_Options[1]:
        Room1_1E()
    elif UserChoice == Room1_1S_Options[2]:
        Room1_1SE()
    elif UserChoice == Room1_1S_Options[3]:
        Room1_2S()
    else:
        print("That it not a valid option, please chose 1, 2, 3 or 4")


def Room1_1W():
    # Health -2 unless knife (-1) or phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_1SW and 1_2W"
    Room1_1W_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1W_Options:
        print("")
        print("You are in 1_1W!")
        print('''Room text here, with potential options.
        1. Option 1 (Engine Bay)
        2. Option 2 (1_1SW - Crew Quarters)
        3. Option 3 (1_2W)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1W_Options[0]:
        RoomEngineBay()
    elif UserChoice == Room1_1W_Options[1]:
        Room1_1SW()
    elif UserChoice == Room1_1W_Options[2]:
        Room1_2W()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_1NE():
    # Health +1
    # From here we can go to... 1_1N, NNE and ENE"
    Room1_1NE_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1NE_Options:
        print("")
        print("You are in 1_1NE! (Holodeck")
        print('''Room text here, with potential options.
        1. Option 1 (1_1N)
        2. Option 2 (NNE)
        3. Option 3 (ENE)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1NE_Options[0]:
        Room1_1N()
    elif UserChoice == Room1_1NE_Options[1]:
        RoomNNE()
    elif UserChoice == Room1_1NE_Options[2]:
        RoomENE()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_1SE():
    # Health +1
    # From here we can go to... 1_1E, ESETransporterRoom and SSE"
    Room1_1SE_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1SE_Options:
        print("")
        print("You are in 1_1SE! (Sickbay)")
        print('''Room text here, with potential options.
        1. Option 1 (1_1E)
        2. Option 2 (ESE Transporter Room)
        3. Option 3 (SSE)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1SE_Options[0]:
        Room1_1E()
    elif UserChoice == Room1_1SE_Options[1]:
        RoomESETransporterRoom()
    elif UserChoice == Room1_1SE_Options[2]:
        RoomSSE()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_1SW():
    # Health +1
    # From here we can go to... 1_1S, SSW and WSW"
    Room1_1SW_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1SW_Options:
        print("")
        print("You are in 1_1SW! (Crew Quarters)")
        print('''Room text here, with potential options.
        1. Option 1 (1_1S)
        2. Option 2 (SSW)
        3. Option 3 (WSW [Kill Room])
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1SW_Options[0]:
        Room1_1S()
    elif UserChoice == Room1_1SW_Options[1]:
        RoomSSW()
    elif UserChoice == Room1_1SW_Options[2]:
        RoomWSW()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_1NW():
    # Health +1
    # From here we can go to... 1_1W, WNW and NNW"
    Room1_1NW_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1NW_Options:
        print("")
        print("You are in 1_1NW! (Observation Deck")
        print('''Room text here, with potential options.
        1. Option 1 (1_1W)
        2. Option 2 (WNW - Conference Lounge)
        3. Option 3 (NNW - The Bridge)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1NW_Options[0]:
        Room1_1W()
    elif UserChoice == Room1_1NW_Options[1]:
        RoomWNW()
    elif UserChoice == Room1_1NW_Options[2]:
        RoomNNW()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


# Rooms around the outside of the map (not including transporter room)


def Room1_2N():
    # kill room
    # From here we can't go anywhere - we die!"
    print("")
    print("You are in 1_2N! The Shuttle Bay.")
    print("You died!")
    time.sleep(1)
    print('''
         ___  ___ __ __ ___   ___ _ _ ___ ___
        /  _>| . |  \  | __> | . | | | __| . |
        | <_/|   |     | _>  | | | ' | _>|   /
        `____|_|_|_|_|_|___> `___|__/|___|_\_|
        ''')
    print("")
    time.sleep(1)
    print("Resetting time loop in...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Press PLAY GAME to initialise time loop.")
    time.sleep(1)
    exit()


def Room1_2E():
    # Health -1 unless phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_2NE and ESETransporterRoom"
    Room1_2E_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_2E_Options:
        print("")
        print("You are in 1_2E!")
        print('''Room text here, with potential options.
        1. Option 1 (Engine Bay)
        2. Option 2 (1_2NE - Store Room [Kill Room])
        3. Option 3 (ESE Transporter Room)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2E_Options[0]:
        RoomEngineBay()
    elif UserChoice == Room1_2E_Options[1]:
        Room1_2NE()
    elif UserChoice == Room1_2E_Options[2]:
        RoomESETransporterRoom()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_2S():
    # Health -3 unless phaser (-2) in weapons
    # From here we can go to... 1_2SE and SSW"
    Room1_2S_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2S_Options:
        print("")
        print("You are in 1_2S!")
        print('''Room text here, with potential options.
        1. Option 1 (1_2SE - Captain's Quarters)
        2. Option 2 (SSW)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2S_Options[0]:
        Room1_2SE()
    elif UserChoice == Room1_2S_Options[1]:
        RoomSSW()
    else:
        print("That it not a valid option, please chose 1 or 2")


def Room1_2W():
    # Health -1 unless phaser or knife (-0) in weapons
    # From here we can go to... 1_2SW, WNW and RoomEngineBay"
    Room1_2W_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_2W_Options:
        print("")
        print("You are in 1_2W!")
        print('''Room text here, with potential options.
        1. Option 1 (1_2SW - Mess Hall)
        2. Option 2 (WNW - Conference Lounge)
        3. Option 3 (Engine Bay)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2W_Options[0]:
        Room1_2SW()
    elif UserChoice == Room1_2W_Options[1]:
        RoomWNW()
    elif UserChoice == Room1_2W_Options[2]:
        RoomEngineBay()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def Room1_2NE():
    # Kill Room
    # From here we can't go anywhere - we die!"
    print("")
    print("You are in 1_2NE! (Store Room [Kill Room]")
    print("You died!")
    time.sleep(1)
    print('''
         ___  ___ __ __ ___   ___ _ _ ___ ___
        /  _>| . |  \  | __> | . | | | __| . |
        | <_/|   |     | _>  | | | ' | _>|   /
        `____|_|_|_|_|_|___> `___|__/|___|_\_|
        ''')
    print("")
    time.sleep(1)
    print("Resetting time loop in...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Press PLAY GAME to initialise time loop.")
    time.sleep(1)
    exit()


def Room1_2SE():
    # Health +3
    # From here we can go to... 1_2E and SSE"
    Room1_2SE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2SE_Options:
        print("")
        print("You are in 1_2SE! (Captain's Quarters)")
        print('''Room text here, with potential options.
        1. Option 1 (1_2E)
        2. Option 2 (SSE)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2SE_Options[0]:
        Room1_2E()
    elif UserChoice == Room1_2SE_Options[1]:
        RoomSSE()
    else:
        print("That it not a valid option, please chose 1 or 2")


def Room1_2SW():
    # Health +2
    # From here we can go to... 1_2S and WSW"
    Room1_2SW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2SW_Options:
        print("")
        print("You are in 1_2SW! (Mess Hall)")
        print('''Room text here, with potential options.
        1. Option 1 (1_2S)
        2. Option 2 (WSW [Kill Room])
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2SW_Options[0]:
        Room1_2S()
    elif UserChoice == Room1_2SW_Options[1]:
        RoomWSW()
    else:
        print("That it not a valid option, please chose 1 or 2")


def Room1_2NW():
    # Health +3
    # From here we can go to... NNW and 1_2W"
    Room1_2NW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2NW_Options:
        print("")
        print("You are in 1_2NW")
        print('''Room text here, with potential options.
        1. Option 1 (NNW - The Bridge)
        2. Option 2 (1_2W)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2NW_Options[0]:
        RoomNNW()
    elif UserChoice == Room1_2NW_Options[1]:
        Room1_2W()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomNNE():
    # Knife weapon location
    # From here we can go to... 1_2NE and 1_1NE"
    RoomNNE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomNNE_Options:
        print("")
        print("You are in NNE!")
        print('''Room text here, with potential options.
        1. Option 1 (1_2NE - Store room [Kill Room])
        2. Option 2 (1_1NE - Holodeck)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomNNE_Options[0]:
        Room1_2NE()
    elif UserChoice == RoomNNE_Options[1]:
        Room1_1NE()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomENE():
    # Locator device location
    # From here we can go to... NNE and 1_2E"
    RoomENE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomENE_Options:
        print("")
        print("You are in ENE!")
        print('''Room text here, with potential options.
        1. Option 1 (NNE)
        2. Option 2 (1_2E)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomENE_Options[0]:
        RoomNNE()
    elif UserChoice == RoomENE_Options[1]:
        Room1_2E()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomSSE():
    # Batteries location
    # From here we can go to... 1_1SE and 1_2S"
    RoomSSE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomSSE_Options:
        print("")
        print("You are in SSE!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1SE - Sickbay)
        2. Option 2 (1_2S)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomSSE_Options[0]:
        Room1_1SE()
    elif UserChoice == RoomSSE_Options[1]:
        Room1_2S()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomSSW():
    # Transporter key location
    # From here we can go to... 1_1SW and 1_2SW"
    RoomSSW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomSSW_Options:
        print("")
        print("You are in SSW!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1SW - Crew Quarters)
        2. Option 2 (1_2SW - Mess Hall)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomSSW_Options[0]:
        Room1_1SW()
    elif UserChoice == RoomSSW_Options[1]:
        Room1_2SW()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomWSW():
    # kill room
    # From here we can't go anywhere - we die!"
    print("")
    print("You are in WSW!")
    print("You died!")
    time.sleep(1)
    print('''
         ___  ___ __ __ ___   ___ _ _ ___ ___
        /  _>| . |  \  | __> | . | | | __| . |
        | <_/|   |     | _>  | | | ' | _>|   /
        `____|_|_|_|_|_|___> `___|__/|___|_\_|
        ''')
    print("")
    time.sleep(1)
    print("Resetting time loop in...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Press PLAY GAME to initialise time loop.")
    time.sleep(1)
    exit()


def RoomWNW():
    # Phaser Weapon location
    # From here we can go to... 1_2NW and NNW"
    RoomWNW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomWNW_Options:
        print("")
        print("You are in WNW! (Conference Lounge)")
        print('''Room text here, with potential options.
        1. Option 1 (1_2NW)
        2. Option 2 (NNW - The Bridge)
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomWNW_Options[0]:
        Room1_2NW()
    elif UserChoice == RoomWNW_Options[1]:
        RoomNNW()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomNNW():
    # Comms device location
    # From here we can go to... 1_1NW and 1_2N"
    RoomNNW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomNNW_Options:
        print("")
        print("You are in NNW! (The Bridge)")
        print('''Room text here, with potential options.
        1. Option 1 (1_1NW - Observation Deck)
        2. Option 2 (1_2N - Shuttle Bay [Kill Room])
        \n
        Where would you like to go?''')
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomNNW_Options[0]:
        Room1_1NW()
    elif UserChoice == RoomNNW_Options[1]:
        Room1_2N()
    else:
        print("That it not a valid option, please chose 1 or 2")


def RoomESETransporterRoom():
    # Ending room
    # From here we can go to... 1_1E and 1_2SE"
    # We can also die here if we don't have the correct equipment"
    print("")
    print("You are in ESE Transporter Room!")
    BeamOut = input("Would you like to try and beam out of the ship? (Y/N) \n")
    if BeamOut.lower() == "y" or BeamOut.lower() == "yes":
        print("")
        print("Initialising beam...")
        time.sleep(1)
        print("Beaming down to planet surface in...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        if (comms is True and locator is True and transporter is True and
                key is True and batteries is True):
            print("")
            print("Congratulations! You beamed safely down to Nova VII")
            time.sleep(2)
            print("and escaped the time loop, you look up to the sky just")
            time.sleep(2)
            print(" in time to see The Enterprise lose the last of its")
            time.sleep(2)
            print("structural integrity and scatter accross the heavens,")
            time.sleep(2)
            print("some small pieces break through the atmosphere of")
            time.sleep(2)
            print("Nova VII giving the planet a final farewell in a symbolic")
            time.sleep(2)
            print("meteor shower.")
            time.sleep(3)
            PlayAgain = input("Would you like to play again? (Y/N) \n")
            if PlayAgain.lower() == "y" or PlayAgain.lower() == "yes":
                print("Press PLAY GAME to initialise time loop.")
            elif PlayAgain.lower() == "n" or PlayAgain.lower() == "no":
                print(f"Live long and prosper {name}")
                time.sleep(1)
                print("Initialising shut down...")
                time.sleep(1)
                print('''
                    ___ _ _ ___   ___ _ _ ___
                   |_ _| | | __> | __| \ | . |
                    | ||   | _>  | _>|   | | |
                    |_||_|_|___> |___|_\_|___/
                    ''')
                print("")
                time.sleep(2)
                print("")
                print("")
                print("")
                print('''
            _____ _____  ______ _____ _____ _______ _____
           / ____|  __ \|  ____|  __ \_   _|__   __/ ____|
          | |    | |__) | |__  | |  | || |    | | | (___
          | |    |  _  /|  __| | |  | || |    | |  \___ |
          | |____| | \ \| |____| |__| || |_   | |  ____) |
           \_____|_|  \_\______|_____/_____|  |_| |_____/
           ''')
                print("")
                time.sleep(2)
                print('''
                            Developer
                           DEANNA SALE
                ''')
                time.sleep(1)
                print('''
                              Theme
                 GENE RODDENBERRY (Star Trek Creator)
                ''')
                time.sleep(1)
                print('''
                            ASCII Text
                  https://patorjk.com/software/taag/
                ''')
                time.sleep(1)
                print('''
                           ASCII Images
              http://www.asciiartfarts.com/star_trek.html
                ''')
                time.sleep(1)
                print('''
                            Story Line
                           DEANNA SALE
                ''')
                time.sleep(3)
                exit()
        else:
            print("")
            print("You did not have all the required equipment and items to")
            time.sleep(2)
            print("successfully beam down to Nova VII. You beamed half way")
            time.sleep(2)
            print("down to the planet's surface but appeared in space before")
            time.sleep(2)
            print("you could reach your desination.")
            time.sleep(2)
            print('''
                     ____ ___ __ __ ___   ___ _ _ ___ ___
                    /  _>| . |  \  | __> | . | | | __| . |
                    | <_/|   |     | _>  | | | ' | _>|   /
                    `____|_|_|_|_|_|___> `___|__/|___|_\_|
                    \n
                    ''')
            time.sleep(1)
            print("Resetting time loop in...")
            time.sleep(1)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("Press PLAY GAME to initialise time loop.")
            time.sleep(1)
            exit()
    elif BeamOut.lower() == "n" or BeamOut.lower() == "no":
        print("")
        print("You continue on your journey...")
        RoomESE_Options = ["1", "2"]
        UserChoice = ""
        while UserChoice not in RoomESE_Options:
            print("")
            print('''Room text here, with potential options.
                1. Option 1 (1_1E)
                2. Option 2 (1_2SE - Captain's Quarters)
                \n
                Where would you like to go?''')
            UserChoice = str(input("Enter option number: \n"))
            if UserChoice == RoomESE_Options[0]:
                Room1_1E()
            elif UserChoice == RoomESE_Options[1]:
                Room1_2SE()
            else:
                print("That it not a valid option, please chose 1 or 2")
    else:
        print("That option does not compute, please try again.")
        RoomESETransporterRoom()


PlayGame()
