import time


def P_S(text, delay):
    print(text)
    time.sleep(delay)


def FourRoomChoice(option1, option2, option3, option4, Room1, Room2, Room3,
                   Room4):
    print("")
    print(f"1. {option1}")
    print(f"2. {option2}")
    print(f"3. {option3}")
    print(f"4. {option4}")
    UserChoice = ""
    UserChoice = str(input("\nEnter option number: \n"))
    if UserChoice == str(1):
        Room1()
    elif UserChoice == str(2):
        Room2()
    elif UserChoice == str(3):
        Room3()
    elif UserChoice == str(4):
        Room4()
    else:
        print("That it not a valid option, please chose 1, 2, 3 or 4")


def FourRoomSecondChance(Room1, Room2, Room3, Room4):
    print("\nWhere would you like to go?")
    UserChoice = ""
    UserChoice = str(input("Enter option number: \n"))
    if UserChoice == str(1):
        Room1()
    elif UserChoice == str(2):
        Room2()
    elif UserChoice == str(3):
        Room3()
    elif UserChoice == str(4):
        Room4()
    else:
        print("That it not a valid option, please chose 1, 2, 3 or 4")
        FourRoomSecondChance(Room1, Room2, Room3, Room4)


def ThreeRoomChoice(option1, option2, option3, Room1, Room2, Room3):
    print("")
    print(f"1. {option1}")
    print(f"2. {option2}")
    print(f"3. {option3}")
    UserChoice = ""
    UserChoice = str(input("\nEnter option number: \n"))
    if UserChoice == str(1):
        Room1()
    elif UserChoice == str(2):
        Room2()
    elif UserChoice == str(3):
        Room3()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")


def ThreeRoomSecondChance(Room1, Room2, Room3):
    print("\nWhere would you like to go?")
    UserChoice = ""
    UserChoice = str(input("Enter option number: \n"))
    if UserChoice == str(1):
        Room1()
    elif UserChoice == str(2):
        Room2()
    elif UserChoice == str(3):
        Room3()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")
        ThreeRoomSecondChance(Room1, Room2, Room3)


def TwoRoomChoice(option1, option2, Room1, Room2):
    print("")
    print(f"1. {option1}")
    print(f"2. {option2}")
    UserChoice = ""
    UserChoice = str(input("\nEnter option number: \n"))
    if UserChoice == str(1):
        Room1()
    elif UserChoice == str(2):
        Room2()
    else:
        print("That it not a valid option, please chose 1 or 2")


def TwoRoomSecondChance(Room1, Room2):
    print("\nWhere would you like to go?")
    UserChoice = ""
    UserChoice = str(input("Enter option number: \n"))
    if UserChoice == str(1):
        Room1()
    elif UserChoice == str(2):
        Room2()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")
        TwoRoomSecondChance(Room1, Room2)


def NoHealth():
    P_S("\nYou have become gravely injured (your health has", 2)
    P_S("reached 0 or less). You can no longer carry on trying to reach", 2)
    P_S("Nova VII. You lay down and close your eyes, your body", 2)
    P_S("too broken to carry on.", 2)
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