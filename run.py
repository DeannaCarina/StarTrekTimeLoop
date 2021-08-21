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
    "fists": True,
    "knife": False,
    "phaser": False,
    "comms": False,
    "locator": False,
    "key": False,
    "batteries": False
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
        P_S(f"Hello {name}... welcome aboard the USS Enterprise:", 2)
        P_S("NCC-1703. It is Star Date 3167. You are the second", 3)
        P_S("engineer on board and work the night shift. You joined", 2.5)
        P_S("the ship on her maiden voyage of her 15 year mission to:", 3.5)
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
        print("Do you want to see the introduction?")        
        SkipIntro = input("(recommended for beginners) (Y/N): \n")
        if SkipIntro.lower() == "y" or SkipIntro.lower() == "yes":
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
        elif SkipIntro.lower() == "n" or SkipIntro.lower() == "no":
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
    print("ROOM AND PATH INFO HERE")
    FourRoomChoice("Room1_1N", "Room1_1E", "Room1_1S", "Room1_1W",
                   Room1_1N, Room1_1E, Room1_1S, Room1_1W)
    FourRoomSecondChance(Room1_1N, Room1_1E, Room1_1S, Room1_1W)


def Room1_1N():
    # Rooms around the outside of the engine bay
    # Health -3 cannot be changed by weapons
    # From here we can go to... 1_1NW, NNW, 1_2N and NNE
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1N\n")
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
    UserStats["health"] = UserStats["health"]-3
    P_S("You got hurt (Trilithium resin)! You lost 3 health. Your new", 2)
    P_S("health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        FourRoomChoice("1_1NW - Observation Deck", "RoomNNW", "Room1_2N",
                       "RoomNNE", Room1_1NW, RoomNNW, Room1_2N, RoomNNE)
        FourRoomSecondChance(Room1_1NW, RoomNNW, Room1_2N, RoomNNE)


def Room1_1E():
    # Health -2 unless knife (-1) or phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_1NE and 1_2E"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1E\n")
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
    UserStats["health"] = UserStats["health"]-2
    P_S("You got hurt (RedJac)! You lost 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        ThreeRoomChoice("Engine Bay", "1_1NE - Holodeck", "1_2E",
                        RoomEngineBay, Room1_1NE, Room1_2E)
        ThreeRoomSecondChance(RoomEngineBay, Room1_1NE, Room1_2E)


def Room1_1S():
    # Health -1 cannot be changed by weapons
    # From here we can go to... 1_1W, 1_1E, 1_1SE and 1_2S"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1S\n")
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
    UserStats["health"] = UserStats["health"]-1
    P_S("You got hurt (Cobalt Diselenide)! You lost 1 health. Your new", 2)
    P_S("health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        FourRoomChoice("Room1_1W", "Room1_1E", "Room1_1SE", "Room1_2S",
                       Room1_1W, Room1_1E, Room1_1SE, Room1_2S)
        FourRoomSecondChance(Room1_1W, Room1_1E, Room1_1SE, Room1_2S)


def Room1_1W():
    # Health -2 unless knife (-1) or phaser (-0) in weapons
    # From here we can go to... RoomEngineBay, 1_1SW and 1_2W"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_1W\n")
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
    UserStats["health"] = UserStats["health"]-2
    P_S("You got hurt (Neural Parasites)! You lost 2 health. Your new", 2)
    P_S("health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        ThreeRoomChoice("Engine Bay", "1_1SW", "1_2W",
                        RoomEngineBay, Room1_1SW, Room1_2W)
        ThreeRoomSecondChance(RoomEngineBay, Room1_1SW, Room1_2W)


def Room1_1NE():
    # Health +1
    # From here we can go to... 1_1N, NNE and ENE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in room code: 1.1NE (Holodeck).\n")
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
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    ThreeRoomChoice("Room1_1N", "RoomNNE", "RoomENE",
                    Room1_1N, RoomNNE, RoomENE)
    ThreeRoomSecondChance(Room1_1N, RoomNNE, RoomENE)


def Room1_1SE():
    # Health +1
    # From here we can go to... 1_1E, ESETransporterRoom and SSE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in room code: 1.1SE (Sickbay).\n")
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
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    ThreeRoomChoice("Room1_1E", "RoomESETransporterRoom", "RoomSSE",
                    Room1_1E, RoomESETransporterRoom, RoomSSE)
    ThreeRoomSecondChance(Room1_1E, RoomESETransporterRoom, RoomSSE)


def Room1_1SW():
    # Health +1
    # From here we can go to... 1_1S, SSW and WSW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in room code: 1.1SW (Crew Quarters + Tribble).\n")
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
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    ThreeRoomChoice("Room1_1S", "RoomSSW", "RoomWSW",
                    Room1_1S, RoomSSW, RoomWSW)
    ThreeRoomSecondChance(Room1_1S, RoomSSW, RoomWSW)


def Room1_1NW():
    # Health +1
    # From here we can go to... 1_1W, WNW and NNW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in room code: 1.1NW (Observation Deck).\n")
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
    UserStats["health"] = UserStats["health"]+1
    P_S("You found food! You gained 1 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    ThreeRoomChoice("Room1_1W", "RoomWNW", "RoomNNW",
                    Room1_1W, RoomWNW, RoomNNW)
    ThreeRoomSecondChance(Room1_1W, RoomWNW, RoomNNW)


# Rooms around the outside of the map (not including transporter room)
def Room1_2N():
    # kill room
    # From here we can't go anywhere - we die!"
    P_S("\n-------------------------------------------\n", 3)
    P_S("You are in room code: 1.2N (The Shuttle Bay).\n", 2)
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
    UserStats["health"] = UserStats["health"]-1
    P_S("You got hurt (Dark Matter LifeForm)! You lost 1 health. Your new", 2)
    P_S("health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        ThreeRoomChoice("RoomEngineBay", "Room1_2NE", "RoomESETransporterRoom",
                        RoomEngineBay, Room1_2NE, RoomESETransporterRoom)
        ThreeRoomSecondChance(RoomEngineBay, Room1_2NE, RoomESETransporterRoom)


def Room1_2S():
    # Health -2 unless phaser (-1) in weapons
    # From here we can go to... 1_2SE and SSW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2S\n")
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
    UserStats["health"] = UserStats["health"]-2
    P_S("You got hurt (Dikironium Cloud)! You lost 3 health. Your new", 2)
    P_S("health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        TwoRoomChoice("Room1_2SE", "RoomSSW",
                      Room1_2SE, RoomSSW)
        TwoRoomSecondChance(Room1_2SE, RoomSSW)


def Room1_2W():
    # Health -1 unless phaser or knife (-0) in weapons
    # From here we can go to... 1_2SW, WNW and RoomEngineBay"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2W\n")
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
    UserStats["health"] = UserStats["health"]-1
    P_S("You got hurt (Genesis Worms)! You lost 1 health. Your new", 2)
    P_S("health is:", 2)
    P_S(UserStats["health"], 2)
    if UserStats["health"] <= 0:
        NoHealth()
    else:
        print("ROOM AND PATH INFO HERE")
        ThreeRoomChoice("Room1_2SW", "RoomWNW", "RoomEngineBay",
                        Room1_2SW, RoomWNW, RoomEngineBay)
        ThreeRoomSecondChance(Room1_2SW, RoomWNW, RoomEngineBay)


def Room1_2NE():
    # Kill Room
    # From here we can't go anywhere - we die!"
    P_S("\n-------------------------------------------\n", 3)
    P_S("You are in room code: 1.2NE (Storeroom). \n", 2)
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
    print("You are in room code: 1.2SE (Your personal quarters).\n")
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
    UserStats["health"] = UserStats["health"]+3
    P_S("You found food! You gained 3 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("Room1_2E", "RoomSSE",
                  Room1_2E, RoomSSE)
    TwoRoomSecondChance(Room1_2E, RoomSSE)


def Room1_2SW():
    # Health +2
    # From here we can go to... 1_2S and WSW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in room code: 1.2SW (Mess Hall).\n")
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
    UserStats["health"] = UserStats["health"]+2
    P_S("You found food! You gained 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("Room1_2S", "RoomWSW",
                  Room1_2S, RoomWSW)
    TwoRoomSecondChance(Room1_2S, RoomWSW)


def Room1_2NW():
    # Health +3
    # From here we can go to... NNW and 1_2W"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room1_2NW\n")
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
    UserStats["health"] = UserStats["health"]+2
    P_S("You found food! You gained 2 health. Your new health is:", 2)
    P_S(UserStats["health"], 2)
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("RoomNNW", "Room1_2W",
                  RoomNNW, Room1_2W)
    TwoRoomSecondChance(RoomNNW, Room1_2W)


def RoomNNE():
    # Knife weapon location
    # From here we can go to... 1_2NE and 1_1NE"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in Room code: NNE (Captain's Quarters + Knife)")
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
    if UserStats["knife"] is False:
        print("You found a knife! You hook it into your belt.")
        UserStats["knife"] = True
    elif UserStats["knife"] is True:
        print("This is where you found the knife.")
    else:
        print("An error occured, please restart your game!")
        exit()
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("Room1_2NE", "Room1_1NE",
                  Room1_2NE, Room1_1NE)
    TwoRoomSecondChance(Room1_2NE, Room1_1NE)


def RoomENE():
    # Locator device location
    # From here we can go to... NNE and 1_2E"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomENE + Locator")
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
        P_S("You found a locator device!", 2)
        UserStats["locator"] = True
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
                print("")
                P_S("A voice comes out of your comms device:", 2)
                P_S(f'"{name}! We can see you! Just make sure you have the', 2)
                P_S('transporter override key and we should be able to', 2)
                P_S(f'safely beam you down to Nova VII. Good look {name}', 2)
                P_S('"hopefully we will see each other very soon."', 2)
        elif UserStats["batteries"] is False:
            P_S('The locator device is completely out of batteries, "There', 2)
            P_S('should be some batteries on this ship somewhere!", you', 2)
            P_S("think to yourself.", 2)
    elif UserStats["locator"] is True:
        print("This is where you found the Locator device.")
    else:
        print("An error occured, please restart your game!")
        exit()
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("RoomNNE", "Room1_2E",
                  RoomNNE, Room1_2E)
    TwoRoomSecondChance(RoomNNE, Room1_2E)


def RoomSSE():
    # Batteries location
    # From here we can go to... 1_1SE and 1_2S"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomSSE + Batteries")
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
    if UserStats["batteries"] is False:
        P_S("You found some batteries!", 2)
        UserStats["batteries"] = True
        if UserStats["locator"] is False and UserStats["comms"] is False:
            P_S("\nYou put the batteries into your pocket for safekeeping.", 2)
        elif UserStats["comms"] is True and UserStats["locator"] is False:
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
            P_S("Let me know as soon as you have the locator device and", 2)
            P_S("are ready in the Transporter room with the override key.", 2)
            P_S("I have a feeling you don't have much time, your ship", 2)
            P_S(f'is highly compromised. Hurry {name}, hurry... "', 2)
            print("")
            P_S("You stow the comms device into your pocket and continue", 2)
            P_S("on your way - filled with new hope.", 2)
        elif UserStats["locator"] is True and UserStats["comms"] is False:
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
            print("An error occured, please restart your game!")   
            exit() 
    elif UserStats["batteries"] is True:
        print("This is where you found the batteries.")
    else:
        print("An error occured, please restart your game!")
        exit()
    print("ROOM AND PATH INFO HERE")
    TwoRoomChoice("Room1_1SE", "Room1_2S",
                  Room1_1SE, Room1_2S)
    TwoRoomSecondChance(Room1_1SE, Room1_2S)


def RoomSSW():
    # Transporter key location
    # From here we can go to... 1_1SW and 1_2SW"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in RoomSSW + Key")
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
    if UserStats["key"] is False:
        P_S("You found a key! On close inspection its branded with the", 2)
        P_S("Starfleet logo. During the six years you have worked on", 2)
        P_S("The Enterprise, you have only seen this key a handfull of", 2)
        P_S("times, when the residents of a planet want to be in control", 2)
        P_S("of who beams down to the surface and when - it allows them", 2)
        P_S("full control over the ship's external beam capabilities -", 2)
        P_S("very helpful when they aren't very trusting!\n", 2)
        P_S("You put the key in your pocket for safekeeping.", 2)
        UserStats["key"] = True
    elif UserStats["key"] is True:
        print("This is where you found the override key for the Transporter.")
    else:
        print("An error occured, please restart your game!")
        exit()
    print("ROOM AND PATH INFO HERE")    
    TwoRoomChoice("Room1_1SW", "Room1_2SW",
                  Room1_1SW, Room1_2SW)
    TwoRoomSecondChance(Room1_1SW, Room1_2SW)


def RoomWSW():
    # kill room
    # From here we can't go anywhere - we die!"
    P_S("\n-------------------------------------------\n", 3)
    P_S("You are in WSW! + Window blow out\n", 2)
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
    print("You are in room code: WNW (Conference Lounge) + Phaser.")
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
    if UserStats["phaser"] is False:
        P_S("You found a phaser! This will help against corporeal threats", 2)
        P_S("and reduce if not eliminate any potential damage these", 2)
        P_S("threats inflict upon you.", 2)
        UserStats["phaser"] = True
    elif UserStats["phaser"] is True:
        print("This is where you found the phaser.")
    else:
        print("An error occured, please restart your game!")
        exit()
    print("ROOM AND PATH INFO HERE")    
    TwoRoomChoice("Room1_2NW", "RoomNNW",
                  Room1_2NW, RoomNNW)
    TwoRoomSecondChance(Room1_2NW, RoomNNW)


def RoomNNW():
    # Comms device location
    # From here we can go to... 1_1NW and 1_2N"
    P_S("\n-------------------------------------------\n", 3)
    print("You are in room code: NNW (The Bridge) + Comms.")
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
        P_S("You found a comms device!", 2)
        UserStats["comms"] = True
        if UserStats["batteries"] is True:
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
                P_S('\n"I already have the key!" you shout down the comms', 2)
                P_S("device excitedly.\n", 2)
                P_S('"Fantastic!" replies Clancy. "I can also see your', 2)
                P_S("location from your comms device, so I'll be able to", 2)
                P_S('pinpoint your position for safe beam transportation."', 2)
            elif UserStats["key"] is False and UserStats["locator"] is False:
                P_S('"You will also need to find a locator device so I can', 2)
                P_S('pinpoint your exact location once you are in the', 2)
                P_S('beam transportation room."', 2)
            P_S("I have a feeling you don't have much time, your ship", 2)
            P_S(f'is highly compromised. Hurry {name}, hurry... "', 2)
            print("")
            P_S("You stow the comms device into your pocket and continue", 2)
            P_S("on your way - filled with new hope.", 2)
        elif UserStats["batteries"] is False:
            P_S('The comms device is completely out of batteries, "There', 2)
            P_S('should be some batteries on this ship somewhere!", you', 2)
            P_S("think to yourself.", 2)
    elif UserStats["comms"] is True:
        print("This is where you found the comms device.")
    else:
        print("An error occured, please restart your game!")
    TwoRoomChoice("Room1_1NW", "Room1_2N",
                  Room1_1NW, Room1_2N)
    TwoRoomSecondChance(Room1_1NW, Room1_2N)


def RoomESETransporterRoom():
    # Ending room
    # From here we can go to... 1_1E and 1_2SE"
    # We can also die here if we don't have the correct equipment"
    P_S("\n-------------------------------------------\n", 3)
    print("\nYou are in room code: ESE (Transporter Room).")
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
