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
    EndGame()
    

# Starting room
def RoomEngineBay():
    print("testEngineBay")


# Rooms around the outside of the engine bay
def Room1_1N():
    #Health -3 cannot be changed by weapons
    print("test1_1N")
def Room1_1E():
    #Health -2 unless knife (-1) or phaser (-0) in weapons
    print("test1_1E")
def Room1_1S():
    #Health -1  cannot be changed by weapons
    print("test1_1S")
def Room1_1W():
    #Health -2 unless knife (-1) or phaser (-0) in weapons
    print("test1_1W")
def Room1_1NE():
    #Health +1
    print("test1_1NE")
def Room1_1SE():
    #Health +1
    print("test1_1SE")
def Room1_1SW():
    #Health +1
    print("test1_1SW")
def Room1_1NW():
    #Health +1
    print("test1_1NW")

#Rooms around the outside of the map (not including transporter room)
def Room1_2N():
    #kill room
    print("test1_2N")
def Room1_2E():
    #Health -1 unless phaser (-0) in weapons
    print("test1_2E")
def Room1_2S():
    #Health -3 unless phaser (-2) in weapons
    print("test1_2S")
def Room1_2W():
    #Health -1 unless phaser or knife (-0) in weapons
    print("test1_2W")
def Room1_2NE():
    #Kill Room
    print("test1_2NE")
def Room1_2SE():
    #Health +3
    print("test1_2SE")
def Room1_2SW():
    #Health +2
    print("test1_2SW")
def Room1_2NW():
    #Health +3
    print("test1_2NW")
def RoomNNE():
    #Knife weapon location
    print("testNNE")
def RoomENE():
    #Locator device location
    print("testENE")
def RoomSSE():
    #Batteries location
    print("testSSE")
def RoomSSW():
    #Transporter key location
    print("testSSW")
def RoomWSW():
    #kill room
    print("testWSW")
def RoomWNW():
    #Phaser Weapon location
    print("testWNW")
def RoomNNW():
    #Comms device location
    print("testNNW")

#Ending room
def RoomESETransporterRoom():
    print("testESE")

def EndGame():
    print("testEndGame")

#Calling Functions
PlayGame()