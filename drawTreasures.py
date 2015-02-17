import time
import pygame
pygame.init()

size = [1280, 710]
WHITE = (255,255,255)
BLUE = (0,0,255)
coord ={'t' : (145, 138), 'a' : (75, 258) ,
       'b' : (275, 258), 'e' : (165, 378),
       'g' : (95 , 498), 's' : (295, 498),
       'f' : (395, 378), 'h' : (535, 498),
       'c' : (495, 258), 'j' : (745, 258),
       'i' : (795, 498), 'd' : (695, 378)}

landmarks ={'t' : False, 'a' : False,
           'b' : False, 'e' : False,
           'g' : False, 's' : False,
           'f' : False, 'h' : False,
           'c' : False, 'j' : False,
           'i' : False, 'd' : False}

def landmark(location):
    landmarks[location] = 1
    x, y = (coord[location])
    rectangle = pygame.draw.rect(screen, BLUE,(x,y, 10,  10 ))

    
def location():
    treasure1 = raw_input("Input treasure location: ")
    landmark(treasure1)
    
def locationcheck(location):
    if landmarks[location] == 1:
        
        print 'There is a treasure at location ' + location + ' gain x amount of points.'
    else:
        print 'There is not a treaure at this location.'

screen = pygame.display.set_mode(size)

screen.fill(WHITE)
location()
location()
location()
location()
location()
location()
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

    
