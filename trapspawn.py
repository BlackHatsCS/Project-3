import random
import time

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
    trapspawn = random.choice(nodes)
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
    elif rspawn ==3:
        rstart = 'i'
    global trapspawn
    if rspawn == 'c':
        trapspawn != 'c'
    elif rspawn == 'j':
        trapspawn != 'j'
    elif rspawn == 'i':
        trapspawn != 'i'
    elif rspawn == 'd':
        trapspawn != 'd'
spawn()
