import time
import pygame
pygame.init()

size = [1280, 720]
WHITE = (255,255,255)
BLUE = (0,0,255)

landmarkCoords ={'t' : (145, 138), 'a' : (75, 258) ,
                 'b' : (275, 258), 'e' : (165, 378),
                 'g' : (95 , 498), 's' : (295, 498),
                 'f' : (395, 378), 'h' : (535, 498),
                 'c' : (495, 258), 'j' : (745, 258),
                 'i' : (795, 498), 'd' : (695, 378)}

landmarkTreasureState ={'t' : False, 'a' : False,
                        'b' : False, 'e' : False,
                        'g' : False, 's' : False,
                        'f' : False, 'h' : False,
                        'c' : False, 'j' : False,
                        'i' : False, 'd' : False}



def userInputTreasureLocation():
    treasureLocation = raw_input("Input treasure location: ")
    #landmark(treasureLocation)
    landmarkTreasureState[treasureLocation] = True

def drawAllTreasures():
    for key in landmarkTreasureState:
        if landmarkTreasureState[key] == True:
            x, y = (landmarkCoords[key])
            pygame.draw.rect(screen, BLUE,(x,y,10,10))
    pygame.display.flip()
                 
def locationcheck(location):
    if landmarkTreasureState[location] == True :
            
        print 'There is a treasure at location ' + location + ' gain x amount of points.'
    else:
        print 'There is not a treaure at this location.'

screen = pygame.display.set_mode(size)
screen.fill(WHITE)

userInputTreasureLocation()
userInputTreasureLocation()
userInputTreasureLocation()
userInputTreasureLocation()
userInputTreasureLocation()
drawAllTreasures()              
pygame.event.wait()

locationcheck('a')
time.sleep(1)
locationcheck('b')
time.sleep(1)
locationcheck('c')
time.sleep(1)
locationcheck('d')
pygame.event.wait()
    



pygame.display.flip()

    
