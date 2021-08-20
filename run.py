# Developer: Deanna Sale
# Date of release: TBC
# Subject: Code Institute Portfolio Project 3 - Python
# Program Name: "Star Trek: Time Loop"

from functions import P_S, FourRoomChoice, FourRoomSecondChance, \
    ThreeRoomChoice, ThreeRoomSecondChance, TwoRoomChoice, \
    TwoRoomSecondChance, NoHealth
import time

UserStats = {
    "health": 5,
    "weapons": ["fists"],
    "comms": True,
    "locator": False,
    "key": True,
    "batteries": True
}


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
    \n''')
    WantToPlay = input("Would you like to play? (Y/N): \n")
    if WantToPlay.lower() == "y" or WantToPlay.lower() == "yes":
        P_S("Commencing time loop in...", 1.5)
        P_S("3...", 1)
        P_S("2...", 1)
        P_S("1...", 1)
        global name
        name = input("What is your name? \n")
        P_S(f"Hello {name}... welcome aboard the USS Enterprise:", 1.5)
        P_S("NCC-1703. It is Star Date 3167. You are the second", 2)
        P_S("engineer on board and work the night shift. You joined", 2)
        P_S("the ship on her maiden voyage of her 15 year mission to:", 2)
        P_S('''
        BOLDLY GO WHERE NO ONE HAS GONE BEFORE...

o               .         ___---___                    .
        .              .--\        --.     .     .         .
                     ./.;_.\     __/~ \.
                    /;  / `-'  __\    . \                   
    .      .       / ,--'     / .   .;   \        |
                  | .|       /       __   |      -O-       .
                 |__/    __ |  . ;   \ | . |      
                 |      /  \\_    . ;| \___|
    .    o       |      \  .~\\___,--'     |           .
                  |     | . ; ~~~~\_    __|
     |             \    \   .  .  ; \  /_/   .
    -O-        .    \   /         . |  ~/                  .
     |    .          ~\ \   .      /  /~          o
   .                   ~--___ ; ___--~
                  .          ---         .
                ''', 3.5)
        SkipIntro = input("Do you want to skip the intro? (Y/N): \n")
        if SkipIntro.lower() == "n" or SkipIntro.lower() == "no":
            time.sleep(2)
            P_S("\nYou have been on the ship for 6 years now, and have", 2)
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
        elif SkipIntro.lower() == "y" or SkipIntro.lower() == "yes":
            RoomEngineBay()
        else:
            print("That option does not compute, please try again.")
            PlayGame()
    elif WantToPlay.lower() == "n" or WantToPlay.lower() == "no":
        P_S("*Beaming you out*", 1)
        P_S("Initialising shut down...", 1)
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
    P_S("\n-------------------------------------------\n", 3)
    print("You are in the Engine Bay!")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    FourRoomChoice("Room1_1N", "Room1_1E", "Room1_1S", "Room1_1W",
                   Room1_1N, Room1_1E, Room1_1S, Room1_1W)
    FourRoomSecondChance(Room1_1N, Room1_1E, Room1_1S, Room1_1W)


def Room1_1N():
    # Rooms around the outside of the engine bay
    # Health -3 cannot be changed by weapons
    # From here we can go to... 1_1NW, NNW, 1_2N and NNE
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1N\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-3
    P_S("You got hurt! You lost 3 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        FourRoomChoice("1_1NW - Observation Deck", "RoomNNW", "Room1_2N",
                       "RoomNNE", Room1_1NW, RoomNNW, Room1_2N, RoomNNE)
        FourRoomSecondChance(Room1_1NW, RoomNNW, Room1_2N, RoomNNE)


def Room1_1E():
    # Health -2 unless knife (-1) or phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_1NE and 1_2E"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1E\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-2
    P_S("You got hurt! You lost 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        ThreeRoomChoice("Engine Bay", "1_1NE - Holodeck", "1_2E",
                        RoomEngineBay, Room1_1NE, Room1_2E)
        ThreeRoomSecondChance(RoomEngineBay, Room1_1NE, Room1_2E)


def Room1_1S():
    # Health -1 cannot be changed by weapons
    # From here we can go to... 1_1W, 1_1E, 1_1SE and 1_2S"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1S\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-1
    P_S("You got hurt! You lost 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        FourRoomChoice("Room1_1W", "Room1_1E", "Room1_1SE", "Room1_2S",
                       Room1_1W, Room1_1E, Room1_1SE, Room1_2S)
        FourRoomSecondChance(Room1_1W, Room1_1E, Room1_1SE, Room1_2S)


def Room1_1W():
    # Health -2 unless knife (-1) or phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_1SW and 1_2W"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1W\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-2
    P_S("You got hurt! You lost 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        ThreeRoomChoice("Engine Bay", "1_1SW - Holodeck", "1_2W",
                        RoomEngineBay, Room1_1SW, Room1_2W)
        ThreeRoomSecondChance(RoomEngineBay, Room1_1SW, Room1_2W)


def Room1_1NE():
    # Health +1
    # From here we can go to... 1_1N, NNE and ENE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1NE\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    ThreeRoomChoice("Room1_1N", "RoomNNE", "RoomENE",
                    Room1_1N, RoomNNE, RoomENE)
    ThreeRoomSecondChance(Room1_1N, RoomNNE, RoomENE)


def Room1_1SE():
    # Health +1
    # From here we can go to... 1_1E, ESETransporterRoom and SSE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1SE\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    ThreeRoomChoice("Room1_1E", "RoomESETransporterRoom", "RoomSSE",
                    Room1_1E, RoomESETransporterRoom, RoomSSE)
    ThreeRoomSecondChance(Room1_1E, RoomESETransporterRoom, RoomSSE)


def Room1_1SW():
    # Health +1
    # From here we can go to... 1_1S, SSW and WSW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1SW\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    ThreeRoomChoice("Room1_1S", "RoomSSW", "RoomWSW",
                    Room1_1S, RoomSSW, RoomWSW)
    ThreeRoomSecondChance(Room1_1S, RoomSSW, RoomWSW)


def Room1_1NW():
    # Health +1
    # From here we can go to... 1_1W, WNW and NNW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1NW\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    ThreeRoomChoice("Room1_1W", "RoomWNW", "RoomNNW",
                    Room1_1W, RoomWNW, RoomNNW)
    ThreeRoomSecondChance(Room1_1W, RoomWNW, RoomNNW)


# Rooms around the outside of the map (not including transporter room)
def Room1_2N():
    # kill room
    # From here we can't go anywhere - we die!"
    P_S("You are in 1_2N! The Shuttle Bay.\n", 2)
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    P_S("You died!\n", 1.5)
    P_S('''
         ___  ___ __ __ ___   ___ _ _ ___ ___
        /  _>| . |  \  | __> | . | | | __| . |
        | <_/|   |     | _>  | | | ' | _>|   /
        `____|_|_|_|_|_|___> `___|__/|___|_\_|
        \n''', 2)
    P_S("Resetting time loop in...", 1)
    P_S("3...", 1)
    P_S("2...", 1)
    P_S("1...", 1)
    print("Press PLAY GAME to re-initialise time loop.")
    exit()


def Room1_2E():
    # Health -1 unless phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_2NE and
    # ESETransporterRoom"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2E\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-1
    P_S("You got hurt! You lost 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        ThreeRoomChoice("RoomEngineBay", "Room1_2NE", "RoomESETransporterRoom",
                        RoomEngineBay, Room1_2NE, RoomESETransporterRoom)
        ThreeRoomSecondChance(RoomEngineBay, Room1_2NE, RoomESETransporterRoom)


def Room1_2S():
    # Health -3 unless phaser (-2) in weapons
    # From here we can go to... 1_2SE and SSW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2S\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-3
    P_S("You got hurt! You lost 3 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        TwoRoomChoice("Room1_2SE", "RoomSSW",
                      Room1_2SE, RoomSSW)
        TwoRoomSecondChance(Room1_2SE, RoomSSW)


def Room1_2W():
    # Health -1 unless phaser or knife (-0) in weapons
    # From here we can go to... 1_2SW, WNW and RoomEngineBay"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2W\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]-1
    P_S("You got hurt! You lost 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        ThreeRoomChoice("Room1_2SW", "RoomWNW", "RoomEngineBay",
                        Room1_2SW, RoomWNW, RoomEngineBay)
        ThreeRoomSecondChance(Room1_2SW, RoomWNW, RoomEngineBay)


def Room1_2NE():
    # Kill Room
    # From here we can't go anywhere - we die!"
    P_S("You are in 1_2NE!\n", 2)
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    P_S("You died!\n", 1.5)
    P_S('''
         ___  ___ __ __ ___   ___ _ _ ___ ___
        /  _>| . |  \  | __> | . | | | __| . |
        | <_/|   |     | _>  | | | ' | _>|   /
        `____|_|_|_|_|_|___> `___|__/|___|_\_|
        \n''', 2)
    P_S("Resetting time loop in...", 1)
    P_S("3...", 1)
    P_S("2...", 1)
    P_S("1...", 1)
    print("Press PLAY GAME to re-initialise time loop.")
    exit()


def Room1_2SE():
    # Health +3
    # From here we can go to... 1_2E and SSE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2SE\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+3
    P_S("You found food! You gained 3 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    TwoRoomChoice("Room1_2E", "RoomSSE",
                  Room1_2E, RoomSSE)
    TwoRoomSecondChance(Room1_2E, RoomSSE)


def Room1_2SW():
    # Health +2
    # From here we can go to... 1_2S and WSW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2SW\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+2
    P_S("You found food! You gained 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    TwoRoomChoice("Room1_2S", "RoomWSW",
                  Room1_2S, RoomWSW)
    TwoRoomSecondChance(Room1_2S, RoomWSW)


def Room1_2NW():
    # Health +3
    # From here we can go to... NNW and 1_2W"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2NW\n")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    UserStats["health"] = UserStats["health"]+2
    P_S("You found food! You gained 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    TwoRoomChoice("RoomNNW", "Room1_2W",
                  RoomNNW, Room1_2W)
    TwoRoomSecondChance(RoomNNW, Room1_2W)


def RoomNNE():
    # Knife weapon location
    # From here we can go to... 1_2NE and 1_1NE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomNNE")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    TwoRoomChoice("Room1_2NE", "Room1_1NE",
                  Room1_2NE, Room1_1NE)
    TwoRoomSecondChance(Room1_2NE, Room1_1NE)


def RoomENE():
    # Locator device location
    # From here we can go to... NNE and 1_2E"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomENE")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    TwoRoomChoice("RoomNNE", "Room1_2E",
                  RoomNNE, Room1_2E)
    TwoRoomSecondChance(RoomNNE, Room1_2E)


def RoomSSE():
    # Batteries location
    # From here we can go to... 1_1SE and 1_2S"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomSSE")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    TwoRoomChoice("Room1_1SE", "Room1_2S",
                  Room1_1SE, Room1_2S)
    TwoRoomSecondChance(Room1_1SE, Room1_2S)


def RoomSSW():
    # Transporter key location
    # From here we can go to... 1_1SW and 1_2SW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomSSW")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    TwoRoomChoice("Room1_1SW", "Room1_2SW",
                  Room1_1SW, Room1_2SW)
    TwoRoomSecondChance(Room1_1SW, Room1_2SW)


def RoomWSW():
    # kill room
    # From here we can't go anywhere - we die!"
    P_S("You are in WSW!\n", 2)
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    P_S("You died!\n", 1.5)
    P_S('''
         ___  ___ __ __ ___   ___ _ _ ___ ___
        /  _>| . |  \  | __> | . | | | __| . |
        | <_/|   |     | _>  | | | ' | _>|   /
        `____|_|_|_|_|_|___> `___|__/|___|_\_|
        \n''', 2)
    P_S("Resetting time loop in...", 1)
    P_S("3...", 1)
    P_S("2...", 1)
    P_S("1...", 1)
    print("Press PLAY GAME to re-initialise time loop.")
    exit()


def RoomWNW():
    # Phaser Weapon location
    # From here we can go to... 1_2NW and NNW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomWNW")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    TwoRoomChoice("Room1_2NW", "RoomNNW",
                  Room1_2NW, RoomNNW)
    TwoRoomSecondChance(Room1_2NW, RoomNNW)


def RoomNNW():
    # Comms device location
    # From here we can go to... 1_1NW and 1_2N"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomNNW")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    TwoRoomChoice("Room1_1NW", "Room1_2N",
                  Room1_1NW, Room1_2N)
    TwoRoomSecondChance(Room1_1NW, Room1_2N)


def RoomESETransporterRoom():
    # Ending room
    # From here we can go to... 1_1E and 1_2SE"
    # We can also die here if we don't have the correct equipment"
    P_S("\n-------------------------------------------\n", 3)
    print("\nYou are in ESE Transporter Room!")
    while UserStats["locator"]:
        P_S('''
    ___________________          _-_             _      _-_      _
    \__(==========/_=_/ ____.---'---`---.____  _|_|.---'---`---.|_|_
                \_ \    \----._________.----/  \----._________.----/
                  \ \   /  /    `-_-'              `.  `]-['  ,'
              __,--`█`-'..'-_                        `.' █ `.
             /____          ||                        | (_) |
                  `--.____,-'                          `___'
            \n
            █ = You are here.
        ''', 2)
        break
    BeamOut = input("Would you like to beam out of the ship? (Y/N) \n")
    if BeamOut.lower() == "y" or BeamOut.lower() == "yes":
        P_S("\nInitialising beam...", 1)
        P_S("Beaming down to planet surface in...", 1)
        P_S("3...", 1)
        P_S("2...", 1)
        P_S("1...", 1)
        if ((UserStats["health"]) is True and (UserStats["health"]) is
                True and (UserStats["health"]) is True and
                (UserStats["health"]) is True):
            P_S("Congratulations! You beamed safely down to Nova VII", 2)
            P_S("and escaped the time loop, you look up to the sky", 2)
            P_S("just in time to see The Enterprise lose the last of", 2)
            P_S("its structural integrity and scatter accross the", 2)
            P_S("heavens, some small pieces break through the", 2)
            P_S("atmosphere of Nova VII giving the planet a final ", 2)
            P_S("farewell in a symbolic meteor shower.", 3)
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
                P_S('''
          _____ _____  ______ _____ _____ _______ _____
         / ____|  __ \|  ____|  __ \_   _|__   __/ ____|
        | |    | |__) | |__  | |  | || |    | | | (___
        | |    |  _  /|  __| | |  | || |    | |  \___ |
        | |____| | \ \| |____| |__| || |_   | |  ____) |
         \_____|_|  \_\______|_____/_____|  |_| |_____/
        \n''', 2)
                P_S('''
                            Developer
                        DEANNA SALE
                ''', 1)
                P_S('''
                            Theme
                GENE RODDENBERRY (Star Trek Creator)
                ''', 1)
                P_S('''
                            ASCII Text
                https://patorjk.com/software/taag/
                ''', 1)
                P_S('''
                        ASCII Images
            http://www.asciiartfarts.com/star_trek.html
                ''', 1)
                P_S('''
                            Story Line
                        DEANNA SALE
                ''', 3)
                exit()
        else:
            P_S("\nYou didn't have all the required equipment and", 2)
            P_S("items to successfully beam down to Nova VII. You", 2)
            P_S("beamed half way down to the planet's surface but", 2)
            P_S("appeared in space before you could reach your", 2)
            P_S("desination.", 2)
            P_S('''
                     ____ ___ __ __ ___   ___ _ _ ___ ___
                    /  _>| . |  \  | __> | . | | | __| . |
                    | <_/|   |     | _>  | | | ' | _>|   /
                    `____|_|_|_|_|_|___> `___|__/|___|_\_|
                    \n
                    ''', 1)
            P_S("Resetting time loop in...", 1)
            P_S("3...", 1)
            P_S("2...", 1)
            P_S("1...", 1)
            print("Press PLAY GAME to re-initialise time loop.")
            exit()
    elif BeamOut.lower() == "n" or BeamOut.lower() == "no":
        print("\nYou continue on your journey...")
        TwoRoomChoice("Room1_1E", "Room1_2SE",
                      Room1_1E, Room1_2SE)
        TwoRoomSecondChance(Room1_1E, Room1_2SE)
    else:
        print("That option does not compute, please try again.")
        RoomESETransporterRoom()


PlayGame()




