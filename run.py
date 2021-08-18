#-- Developer: Deanna Sale
#-- Date of release: TBC
#-- Subject: Code Institute Portfolio Project 3 - Python
#-- Program Name: "Star Trek: Time Loop"

health = 5
weapons = ["fists"]
name = None
comms = False
locator = False
transporter = False
key = False
batteries = False

def PlayGame():
    print("Testing from within PlayGame")    

# Starting room
def RoomEngineBay():
    print("testEngineBay")
    print("From here we can go to... 1_1N, 1_1E, 1_1S and 1_1W")
    print("")

# Rooms around the outside of the engine bay
def Room1_1N():
    #Health -3 cannot be changed by weapons
    print("test1_1N")
    print("From here we can go to... 1_1NW, NNW, 1_2N and NNE")
    print("")
def Room1_1E():
    #Health -2 unless knife (-1) or phaser (-0) in weapons
    print("test1_1E")
    print("From here we can go to... RoomEngineBay, 1_1NE and 1_2E")
    print("")
def Room1_1S():
    #Health -1 cannot be changed by weapons
    print("test1_1S")
    print("From here we can go to... 1_1W, 1_1E, 1_1SE and 1_2S")
    print("")
def Room1_1W():
    #Health -2 unless knife (-1) or phaser (-0) in weapons
    print("test1_1W")
    print("From here we can go to... RoomEngineBay, 1_1SW and 1_2W")
    print("")
def Room1_1NE():
    #Health +1
    print("test1_1NE")
    print("From here we can go to... 1_1N, NNE and ENE")
    print("")
def Room1_1SE():
    #Health +1
    print("test1_1SE")
    print("From here we can go to... 1_1E, ESETransporterRoom and SSE")
    print("")
def Room1_1SW():
    #Health +1
    print("test1_1SW")
    print("From here we can go to... 1_1S, SSW and WSW")
    print("")
def Room1_1NW():
    #Health +1
    print("test1_1NW")
    print("From here we can go to... 1_1W, WNW and NNW")
    print("")

#Rooms around the outside of the map (not including transporter room)
def Room1_2N():
    #kill room
    print("test1_2N")
    print("From here we can't go anywhere - we die!")
    print("")
def Room1_2E():
    #Health -1 unless phaser (-0) in weapons
    print("test1_2E")
    print("From here we can go to... RoomEngineBay, 1_2NE and ESETransporterRoom")
    print("")
def Room1_2S():
    #Health -3 unless phaser (-2) in weapons
    print("test1_2S")
    print("From here we can go to... 1_2SE and SSW")
    print("")
def Room1_2W():
    #Health -1 unless phaser or knife (-0) in weapons
    print("test1_2W")
    print("From here we can go to... 1_2SW, WNW and RoomEngineBay")
    print("")
def Room1_2NE():
    #Kill Room
    print("test1_2NE")
    print("From here we can't go anywhere - we die!")
    print("")
def Room1_2SE():
    #Health +3
    print("test1_2SE")
    print("From here we can go to... 1_2E and SSE")
    print("")
def Room1_2SW():
    #Health +2
    print("test1_2SW")
    print("From here we can go to... 1_2S and WSW")
    print("")
def Room1_2NW():
    #Health +3
    print("test1_2NW")
    print("From here we can go to... NNW and 1_2W")
    print("")
def RoomNNE():
    #Knife weapon location
    print("testNNE")
    print("From here we can go to... 1_2NE and 1_1NE")
    print("")
def RoomENE():
    #Locator device location
    print("testENE")
    print("From here we can go to... NNE and 1_2E")
    print("")
def RoomSSE():
    #Batteries location
    print("testSSE")
    print("From here we can go to... 1_1SE and 1_2S")
    print("")
def RoomSSW():
    #Transporter key location
    print("testSSW")
    print("From here we can go to... 1_1SW and 1_2SW")
    print("")
def RoomWSW():
    #kill room
    print("testWSW")
    print("From here we can't go anywhere - we die!")
    print("")
def RoomWNW():
    #Phaser Weapon location
    print("testWNW")
    print("From here we can go to... 1_2NW and NNW")
    print("")
def RoomNNW():
    #Comms device location
    print("testNNW")
    print("From here we can go to... 1_1NW and 1_2N")
    print("")

#Ending room
def RoomESETransporterRoom():
    print("testESE")
    print("From here we can go to... 1_1E and 1_2SE")
    print("We can also die here if we don't have the correct equipment")
    print("")

def EndGame():
    print("testEndGame")

#Calling Functions
PlayGame()
RoomEngineBay()
Room1_1N()
Room1_1E()
Room1_1S()
Room1_1W()
Room1_1NE()
Room1_1SE()
Room1_1SW()
Room1_1NW()
Room1_2N()
Room1_2E()
Room1_2S()
Room1_2W()
Room1_2NE()
Room1_2SE()
Room1_2SW()
Room1_2NW()
RoomNNE()
RoomENE()
RoomSSE()
RoomSSW()
RoomWSW()
RoomWNW()
RoomNNW()
RoomESETransporterRoom()
Endgame()