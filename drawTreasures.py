import time
import pygame
pygame.init()

size = [1280, 710]
WHITE = (255,255,255)
BLUE = (0,0,255)
test ={'t' : (145, 138), 'a' : (75, 258),
       'b' : (275, 258), 'e' : (165, 378),
       'g' : (95, 498), 's' : (295, 498),
       'f' : (395, 378), 'h' : (535, 498),
       'c' : (495, 258), 'j' : (745, 258),
       'i' : (795, 498), 'd' : (695, 378)}

    
def drawDiamond(coords):
    x, y = (test[coords])
    rectangle = pygame.draw.rect(screen, BLUE,(x,y, 10,  10 ))
    pygame.display.update()
    pygame.event.wait()
def location():
    treasure1 = raw_input("j")
    drawDiamond(treasure1)

screen = pygame.display.set_mode(size)

screen.fill(WHITE)
location()
location()
location()
location()
location()
location()

pygame.display.flip()

    
