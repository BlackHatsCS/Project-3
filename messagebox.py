#importing necessary modules and starting up python
import random
import time 
import pygame
import sys
from pygame.locals import *
pygame.init()

#initialising variables needed and drawing the window
size = [1280, 720]
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
font1 = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 36)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test Window')
screen.fill(WHITE)
screen.blit(font1.render("Score", True, BLACK),(1060,330))
screen.blit(font1.render("Treasures", True, BLACK),(990,450))
#screen.blit(font.render("land mark 1",True,BLACK),(1100,360))
pygame.display.update()
pygame.display.flip()

class treasure():
    def __init__(self,spawnLocation,ValueOfTreasure,TypeOfTreasure,TreasureLetter):
        
        self.SpawnLocation= spawnLocation
        self.ValueOfTreasure= ValueOfTreasure 
        self.typeOfTreasure= TypeOfTreasure
        self.TreasureLetter = TreasureLetter
        message = ""
        
    def treasureSpawnLocation(self):
        global rspawn
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

    def drawBox(self):
        pygame.draw.rect(screen, WHITE,(900,500,355,100),0)
        pygame.draw.rect(screen, BLACK, (900,550,355,100), 5)
        screen.blit(font2.render(("Treasure %s spawned at: %s" % (
             self.TreasureLetter, rspawn)), True, BLACK),(920,580))
        pygame.display.update()
         
treasure_A = treasure(1,1,1,'A')
treasure_A.treasureSpawnLocation()
pygame.event.wait()
treasure_A.drawBox()
treasure_B = treasure(1,1,1,'B')
treasure_B.treasureSpawnLocation()
pygame.event.wait()
treasure_B.drawBox()
treasure_C = treasure(1,1,1,'C')
pygame.event.wait()
treasure_C.treasureSpawnLocation()
treasure_C.drawBox()
treasure_D = treasure(1,1,1,'D')
pygame.event.wait()
treasure_D.treasureSpawnLocation()
treasure_D.drawBox()
treasure_E = treasure(1,1,1,'E')
pygame.event.wait()
treasure_E.treasureSpawnLocation()
treasure_E.drawBox()
pygame.display.update()
raw_input("Press enter to quit")
pygame.quit()

