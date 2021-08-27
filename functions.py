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
    P_S("reached a critical level of 0 or less). You can no", 2)
    P_S("longer carry on trying to reach Nova VII. You lay down", 2)
    P_S("and close your eyes, your body too broken to carry on.", 2)
    P_S('''
     _____ _____ _____ _____    _____ _____ _____ _____
    |   __|  _  |     |   __|  |     |  |  |   __| __  |
    |  |  |     | | | |   __|  |  |  |  |  |   __|    -|
    |_____|__|__|_|_|_|_____|  |_____|\___/|_____|__|__|
            \n
            ''', 1)
    P_S("Resetting time loop in...", 1)
    P_S("3...", 1)
    P_S("2...", 1)
    P_S("1...", 1)
    print("Press PLAY GAME to re-initialise time loop.")
    exit()


def Credits():
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
            ''', 1)
    P_S('''
                     Background Image
                      NATHAN ANDERSON
            ''', 3)
    P_S('''
                    Background Music (1)
                      JERRY GOLDSMITH
            ''', 3)
    P_S('''
                    Background Music (2)
                      JERRY GOLDSMITH
                        JAMES HORNER
                      ALEXANDER COURAGE
                        JAY CHATTAWAY
                       CLIFF EIDELMAN
                      LEONARD ROSENMAN
                      PAUL BAILLARGEON
                        GERALD FRIED
                      MICHAEL GIACCHINO
            ''', 3)
    P_S('''
                    Background Music (3)
                      MICHAEL GIACCHINO

            ''', 3)
    P_S('''
                        Peer Reviewers
                             TBC
            ''', 3)
    exit()
