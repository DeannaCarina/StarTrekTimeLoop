#-- Developer: Deanna Sale
#-- Date of release: TBC
#-- Subject: Code Institute Portfolio Project 3 - Python
#-- Program Name: "Star Trek: Time Loop"

import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

health = 5
weapons = ["fists"]
name = None
comms = False
locator = False
transporter = False
key = False
batteries = False

def PlayGame():
    cls()
    WantToPlay = input("Would you like to play? (Y/N): \n")
    if WantToPlay == "Y":
        print("Comencing time loop in...")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        RoomEngineBay()
    elif WantToPlay == "N":
        print("*Beaming you out*")
        EndGame()
    else:
        print("That option does not compute, please try again.")
        PlayGame()    

# Starting room
def RoomEngineBay():
    #From here we can go to... 1_1N(1), 1_1E(2), 1_1S(3) and 1_1W(4)
    EngineBayOptions = ["1", "2", "3", "4"]
    UserChoice = ""
    while UserChoice not in EngineBayOptions:
        print("You are in the Engine Bay!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1N)
        2. Option 2 (1_1E)
        3. Option 3 (1_1S)
        4. Option 4 (1_1W)

        Where would you like to go?'''
        )
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


# Rooms around the outside of the engine bay
def Room1_1N():
    #Health -3 cannot be changed by weapons
    #From here we can go to... 1_1NW, NNW, 1_2N and NNE"
    
    Room1_1N_Options = ["1", "2", "3", "4"]
    UserChoice = ""
    while UserChoice not in Room1_1N_Options:
        print("You are in 1_1N!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1NW - Observation Deck)
        2. Option 2 (NNW - The Bridge)
        3. Option 3 (1_2N - Shuttle Bay [Kill Room])
        4. Option 4 (NNE)

        Where would you like to go?'''
        )
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
    #Health -2 unless knife (-1) or phaser (-0) in weapons
    #From here we can go to... RoomEngineBay, 1_1NE and 1_2E"
    
    Room1_1E_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1E_Options:
        print("You are in 1_1E!")
        print('''Room text here, with potential options.
        1. Option 1 (Engine Bay)
        2. Option 2 (1_1NE - Holodeck)
        3. Option 3 (1_2E)
        
        Where would you like to go?'''
        )
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
    #Health -1 cannot be changed by weapons
    #From here we can go to... 1_1W, 1_1E, 1_1SE and 1_2S"
    
    Room1_1S_Options = ["1", "2", "3", "4"]
    UserChoice = ""
    while UserChoice not in Room1_1S_Options:
        print("You are in 1_1S!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1W)
        2. Option 2 (1_1E)
        3. Option 3 (1_1SE - Sickbay)
        4. Option 4 (1_2S)

        Where would you like to go?'''
        )
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
    #Health -2 unless knife (-1) or phaser (-0) in weapons
    #From here we can go to... RoomEngineBay, 1_1SW and 1_2W"

    Room1_1W_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1W_Options:
        print("You are in 1_1W!")
        print('''Room text here, with potential options.
        1. Option 1 (Engine Bay)
        2. Option 2 (1_1SW - Crew Quarters)
        3. Option 3 (1_2W)

        Where would you like to go?'''
        )
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
    #Health +1
    #From here we can go to... 1_1N, NNE and ENE"
    
    Room1_1NE_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1NE_Options:
        print("You are in 1_1NE! (Holodeck")
        print('''Room text here, with potential options.
        1. Option 1 (1_1N)
        2. Option 2 (NNE)
        3. Option 3 (ENE)

        Where would you like to go?'''
        )
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
    #Health +1
    #From here we can go to... 1_1E, ESETransporterRoom and SSE"
    
    Room1_1SE_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1SE_Options:
        print("You are in 1_1SE! (Sickbay)")
        print('''Room text here, with potential options.
        1. Option 1 (1_1E)
        2. Option 2 (ESE Transporter Room)
        3. Option 3 (SSE)

        Where would you like to go?'''
        )
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
    #Health +1
    #From here we can go to... 1_1S, SSW and WSW"
    
    Room1_1SW_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1SW_Options:
        print("You are in 1_1SW! (Crew Quarters)")
        print('''Room text here, with potential options.
        1. Option 1 (1_1S)
        2. Option 2 (SSW)
        3. Option 3 (WSW [Kill Room])

        Where would you like to go?'''
        )
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
    #Health +1
    #From here we can go to... 1_1W, WNW and NNW"

    Room1_1NW_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_1NW_Options:
        print("You are in 1_1NW! (Observation Deck")
        print('''Room text here, with potential options.
        1. Option 1 (1_1W)
        2. Option 2 (WNW - Conference Lounge)
        3. Option 3 (NNW - The Bridge)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_1NW_Options[0]:
        Room1_1W()
    elif UserChoice == Room1_1NW_Options[1]:
        RoomWNW()
    elif UserChoice == Room1_1NW_Options[2]:
        RoomNNW()
    else:
        print("That it not a valid option, please chose 1, 2 or 3")

#Rooms around the outside of the map (not including transporter room)
def Room1_2N():
    #kill room
    #From here we can't go anywhere - we die!"
    print("You are in 1_2N! The Shuttle Bay.")
    print("You died!")
    time.sleep(1)
    print("Game Over!")
    time.sleep(1)
    print("Resetting time loop in...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    PlayGame()

def Room1_2E():
    #Health -1 unless phaser (-0) in weapons
    #From here we can go to... RoomEngineBay, 1_2NE and ESETransporterRoom"

    Room1_2E_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_2E_Options:
        print("You are in 1_2E!")
        print('''Room text here, with potential options.
        1. Option 1 (Engine Bay)
        2. Option 2 (1_2NE - Store Room [Kill Room])
        3. Option 3 (ESE Transporter Room)

        Where would you like to go?'''
        )
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
    #Health -3 unless phaser (-2) in weapons
    #From here we can go to... 1_2SE and SSW"
    
    Room1_2S_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2S_Options:
        print("You are in 1_2S!")
        print('''Room text here, with potential options.
        1. Option 1 (1_2SE - Captain's Quarters)
        2. Option 2 (SSW)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2S_Options[0]:
        Room1_2SE()
    elif UserChoice == Room1_2S_Options[1]:
        RoomSSW()
    else:
        print("That it not a valid option, please chose 1 or 2")

def Room1_2W():
    #Health -1 unless phaser or knife (-0) in weapons
    #From here we can go to... 1_2SW, WNW and RoomEngineBay"

    Room1_2W_Options = ["1", "2", "3"]
    UserChoice = ""
    while UserChoice not in Room1_2W_Options:
        print("You are in 1_2W!")
        print('''Room text here, with potential options.
        1. Option 1 (1_2SW - Mess Hall)
        2. Option 2 (WNW - Conference Lounge)
        3. Option 3 (Engine Bay)

        Where would you like to go?'''
        )
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
    #Kill Room
    #From here we can't go anywhere - we die!"
    print("You are in 1_2NE! (Store Room [Kill Room]")
    print("You died!")
    time.sleep(1)
    print("Game Over!")
    time.sleep(1)
    print("Resetting time loop in...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    PlayGame()

def Room1_2SE():
    #Health +3
    #From here we can go to... 1_2E and SSE"

    Room1_2SE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2SE_Options:
        print("You are in 1_2SE! (Captain's Quarters)")
        print('''Room text here, with potential options.
        1. Option 1 (1_2E)
        2. Option 2 (SSE)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2SE_Options[0]:
        Room1_2E()
    elif UserChoice == Room1_2SE_Options[1]:
        RoomSSE()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def Room1_2SW():
    #Health +2
    #From here we can go to... 1_2S and WSW"
    
    Room1_2SW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2SW_Options:
        print("You are in 1_2SW! (Mess Hall)")
        print('''Room text here, with potential options.
        1. Option 1 (1_2S)
        2. Option 2 (WSW [Kill Room])

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_2SW_Options[0]:
        Room1_2S()
    elif UserChoice == Room1_2SW_Options[1]:
        RoomWSW()
    else:
        print("That it not a valid option, please chose 1 or 2")

def Room1_2NW():
    #Health +3
    #From here we can go to... NNW and 1_2W"

    Room1_2NW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in Room1_2NW_Options:
        print("You are in 1_2NW")
        print('''Room text here, with potential options.
        1. Option 1 (NNW - The Bridge)
        2. Option 2 (1_2W)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == Room1_NW_Options[0]:
        RoomNNW()
    elif UserChoice == Room1_NW_Options[1]:
        Room1_2W()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def RoomNNE():
    #Knife weapon location
    #From here we can go to... 1_2NE and 1_1NE"

    RoomNNE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomNNE_Options:
        print("You are in NNE!")
        print('''Room text here, with potential options.
        1. Option 1 (1_2NE - Store room [Kill Room])
        2. Option 2 (1_1NE - Holodeck)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomNNE_Options[0]:
        Room1_2NE()
    elif UserChoice == RoomNNE_Options[1]:
        Room1_1NE()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def RoomENE():
    #Locator device location
    #From here we can go to... NNE and 1_2E"

    RoomENE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomENE_Options:
        print("You are in ENE!")
        print('''Room text here, with potential options.
        1. Option 1 (NNE)
        2. Option 2 (1_2E)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomENE_Options[0]:
        RoomNNE()
    elif UserChoice == RoomENE_Options[1]:
        Room1_2E()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def RoomSSE():
    #Batteries location
    #From here we can go to... 1_1SE and 1_2S"

    RoomSSE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomSSE_Options:
        print("You are in SSE!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1SE - Sickbay)
        2. Option 2 (1_2S)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomSSE_Options[0]:
        Room1_1SE()
    elif UserChoice == RoomSSE_Options[1]:
        Room1_2S()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def RoomSSW():
    #Transporter key location
    #From here we can go to... 1_1SW and 1_2SW"

    RoomSSW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomSSW_Options:
        print("You are in SSW!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1SW - Crew Quarters)
        2. Option 2 (1_2SW - Mess Hall)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomSSW_Options[0]:
        Room1_1SW()
    elif UserChoice == RoomSSW_Options[1]:
        Room1_2SW()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def RoomWSW():
    #kill room
    #From here we can't go anywhere - we die!"
    print("You are in WSW!")
    print("You died!")
    time.sleep(1)
    print("Game Over!")
    time.sleep(1)
    print("Resetting time loop in...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    PlayGame()

def RoomWNW():
    #Phaser Weapon location
    #From here we can go to... 1_2NW and NNW"

    RoomWNW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomWNW_Options:
        print("You are in WNW! (Conference Lounge)")
        print('''Room text here, with potential options.
        1. Option 1 (1_2NW)
        2. Option 2 (NNW - The Bridge)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomWNW_Options[0]:
        Room1_2NW()
    elif UserChoice == RoomWNW_Options[1]:
        RoomNNW()
    else:
        print("That it not a valid option, please chose 1 or 2")    

def RoomNNW():
    #Comms device location
    #From here we can go to... 1_1NW and 1_2N"

    RoomNNW_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomNNW_Options:
        print("You are in NNW! (The Bridge)")
        print('''Room text here, with potential options.
        1. Option 1 (1_1NW - Observation Deck)
        2. Option 2 (1_2N - Shuttle Bay [Kill Room])

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomNNW_Options[0]:
        Room1_1NW()
    elif UserChoice == RoomNNW_Options[1]:
        Room1_2N()
    else:
        print("That it not a valid option, please chose 1 or 2")
    


#Ending room
def RoomESETransporterRoom():
    #From here we can go to... 1_1E and 1_2SE"
    #We can also die here if we don't have the correct equipment"

    RoomESE_Options = ["1", "2"]
    UserChoice = ""
    while UserChoice not in RoomESE_Options:
        print("You are in ESE Transporter Room!")
        print('''Room text here, with potential options.
        1. Option 1 (1_1E)
        2. Option 2 (1_2SE - Captain's Quarters)

        Where would you like to go?'''
        )
        UserChoice = str(input("Enter option number: \n"))
    if UserChoice == RoomESE_Options[0]:
        Room1_1E()
    elif UserChoice == RoomESE_Options[1]:
        Room1_2SE()
    else:
        print("That it not a valid option, please chose 1 or 2")
    

def EndGame():
    exit()

#Calling Functions
PlayGame()
