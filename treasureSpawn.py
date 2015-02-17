
import random
import time

class treasure():
    def __init__(self,spawnLocation,ValueOfTreasure,TypeOfTreasure):
        
        self.SpawnLocation= spawnLocation
        self.ValueOfTreasure= ValueOfTreasure 
        self.typeOfTreasure= TypeOfTreasure 

# the user choice where the treause is located by entering letter

    def treasureSpawnLocation(self):
        rspawn= 0
        rspawn = raw_input ('enter your rspawn:')        
        if rspawn == "a":
            self.SpawnLocation = 3
            print self.SpawnLocation
        elif rspawn == "b":
            self.SpawnLocation= 4
            print self.SpawnLocation
        elif rspawn == "c":
            self.SpawnLocation=5
            print self.SpawnLocation
        elif rspawn == "d":
            self.SpawnLocation=6
            print self.SpawnLocation
        elif rspawn == "e":
            self.SpawnLocation=7
            print self.SpawnLocation
        elif rspawn == "f":
            self.SpawnLocation=8
            print self.SpawnLocation
        elif rspawn == "g":
            self.SpawnLocation=9
            print self.SpawnLocation
        elif rspawn == "h":
            self.SpawnLocation=10
            print self.SpawnLocation
        elif rspawn == "i":
            self.SpawnLocation=11
            print self.SpawnLocation
        elif rspawn == "j":
            self.SpawnLocation=12
            print self.SpawnLocation

treasure_A = treasure(1,1,1)

treasure_A.treasureSpawnLocation()

