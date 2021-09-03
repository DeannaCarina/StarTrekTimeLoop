import time


def P_S(text, delay):
    """
    To print a line of text and delay the next line for a certain amount
    of time.
    """
    print(text)
    time.sleep(delay)


def FourRoomChoice(option1, option2, option3, option4, Room1, Room2, Room3,
                   Room4):
    """
    If the user is in a room that has four potential exits, this will populate
    the options as a list, ask for the users choice, then take the user to the
    room they have chosen by comparing their option number choice with the
    option of where to go and take them there.
    """
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
    """
    If the user gave an incorrect or invalid choice as a room option - this is
    the function to re-ask the question but without the list of rooms (as they
    will already be visible to the user.)
    If the user is in a room that has four potential exits, this will ask for
    the users choice, then take the user to the room they have chosen by
    comparing their option number choice with the option of where to go and
    take them there.
    """
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
    """
    If the user is in a room that has three potential exits, this will populate
    the options as a list, ask for the users choice, then take the user to the
    room they have chosen by comparing their option number choice with the
    option of where to go and take them there.
    """
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
    """
    If the user gave an incorrect or invalid choice as a room option - this is
    the function to re-ask the question but without the list of rooms (as they
    will already be visible to the user.)
    If the user is in a room that has three potential exits, this will ask for
    the users choice, then take the user to the room they have chosen by
    comparing their option number choice with the option of where to go and
    take them there.
    """
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
    """
    If the user is in a room that has two potential exits, this will populate
    the options as a list, ask for the users choice, then take the user to the
    room they have chosen by comparing their option number choice with the
    option of where to go and take them there.
    """
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
    """
    If the user gave an incorrect or invalid choice as a room option - this is
    the function to re-ask the question but without the list of rooms (as they
    will already be visible to the user.)
    If the user is in a room that has two potential exits, this will ask for
    the users choice, then take the user to the room they have chosen by
    comparing their option number choice with the option of where to go and
    take them there.
    """
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
    """
    This function is called from within the CheckStats function in run.py.
    If the user has a health of 0 or below, then the user will die and the
    following text displayed.
    """
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
    Credits()


def Credits():
    """
    Any time the game ends either via a user death or game completion,
    the credits function will be called displaying the following text.
    """
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
            ''', 1)
    P_S('''
                    Background Music (1)
                      JERRY GOLDSMITH
            ''', 1)
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
            ''', 1)
    P_S('''
                    Background Music (3)
                      MICHAEL GIACCHINO
            ''', 1)
    P_S('''
                        Peer Reviewers
                          MATT BODDEN
            ''', 1)
    P_S("3...", 1)
    P_S("2...", 1)
    P_S("1...", 1)
    print("Press PLAY GAME to re-initialise time loop.")
    exit()


def Error():
    """
    I have tried to call the following function in places within the code
    that I feel could have a high chance of resulting in error due to user
    choices. This function is to display the following text and encourage
    the user to contact the developer so I can correct any coding errors.
    """
    print("AN ERROR OCCURRED.")
    print("We appologise for the inconvenience.")
    print("Please try restarting your game and trying again.")
    print("In the event of further errors, please contact the developer:")
    print("deannacarina@hotmail.com")
    print("Please copy and paste the text from the last 2 rooms you were in.")
    print("Thank you.")
    exit()
