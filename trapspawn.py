import random
import time
import pygame


t = 145, 138
a = 75, 258
b = 275, 258
e = 165, 378
g = 95, 498
s = 295, 498
f = 395, 378
h = 535, 498
c = 495, 258
j = 745, 258
i = 795, 498
d = 695, 378

nodes = [t, a, b, e, g, s, f, h, c, j, i, d]

def spawn():
    rspawn = random.randint(0,3)
    tspawn = random.randint(0,3)
    trspawn = random.randint(0,11)
    global treasure
    if tspawn == 0:
         treasure = 't'
    elif tspawn == 1:
        treasure = 'a'
    elif tspawn == 2:
        treasure = 'e'
    elif tspawn ==3:
        treasure = 'g'
    global rstart
    if rspawn == 0:
        rstart = 'c'
    elif rspawn == 1:
        rstart = 'j'
    elif rspawn == 2:
        rstart = 'd'
    elif rspawn == 3:
        rstart = 'i'
    global trap
    if trspawn == 0:
        trap = 't'
        pygame.draw.rect(screen, RED, [145, 138, 50, 50])
    elif trspawn == 1:
        trap = 'a'
        rstart != 'a'
        pygame.draw.rect(screen, RED, [75, 258, 50, 50])
    elif trspawn == 2:
        trap = 'b'
        rstart != 'b'
        pygame.draw.rect(screen, RED, [275, 258, 50, 50])
    elif trspawn == 3:
        trap = 'e'
        rstart != 'e'
        pygame.draw.rect(screen, RED, [165, 378, 50, 50])
    elif trspawn == 4:
        trap = 'g'
        rstart != 'g'
        pygame.draw.rect(screen, RED, [95, 498, 50, 50])
    elif trspawn == 5:
        trap = 's'
        rstart != 's'
        pygame.draw.rect(screen, RED, [295, 498, 50, 50])
    elif trspawn == 6:
        trap = 'f'
        rstart != 'f'
        pygame.draw.rect(screen, RED, [395, 378, 50, 50])
    elif trspawn == 7:
        trap = 'h'
        rstart != 'h'
        pygame.draw.rect(screen, RED, [535, 498, 50, 50])
    elif trspawn == 8:
        trap = 'c'
        rstart != 'c'
        pygame.draw.rect(screen, RED, [495, 258, 50, 50])
    elif trspawn == 9:
        trap = 'j'
        rstart != 'j'
        pygame.draw.rect(screen, RED, [745, 258, 50, 50])
    elif trspawn == 10:
        trap = 'i'
        rstart != 'i'
        pygame.draw.rect(screen, RED, [795, 498, 50, 50])
    elif trspawn == 11:
        trap = 'd'
        rstart != 'd'
        pygame.draw.rect(screen, RED, [695, 378, 50, 50])
    
spawn()
