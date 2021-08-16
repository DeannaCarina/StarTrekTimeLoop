health = 5
weapons = ["fists"]
name = None
comms = False
locator = False
transporter = False

def Playgame()

# Starting room
def Room0EngineBay()

# Rooms around the outside of the engine bay
def Room1.1N() #Health -3 cannot be changed by weapons
def Room1.1E() #Health -2 unless knife (-1) or phaser (-0) in weapons
def Room1.1S() #Health -1  cannot be changed by weapons
def Room1.1W() #Health -2 unless knife (-1) or phaser (-0) in weapons
def Room1.1NE() #Health +1
def Room1.1SE() #Health +1
def Room1.1SW() #Health +1
def Room1.1NW() #Health +1

#Rooms around the outside of the map (not including transporter room)
def Room1.2N() #kill room
def Room1.2E() #Health -1 unless phaser (-0) in weapons
def Room1.2S() #Health -3 unless phaser (-2) in weapons
def Room1.2W() #Health -1 unless phaser or knife (-0) in weapons
def Room1.2NE() #Kill Room
def Room1.2SE() #Health +3
def Room1.2SW() #Health +2
def Room1.2NW() #Health +3
def RoomNNE() #Knife weapon location
def RoomENE() #Locator device location
def RoomSSE() #Batteries location
def RoomSSW() #Transporter key location
def RoomWSW() #kill room
def RoomWNW() #Phaser Weapon location
def RoomNNW() #Comms device location

#Ending room
def RoomESETransporterRoom()

def EndGame()