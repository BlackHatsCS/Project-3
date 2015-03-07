#importing necessary modules and starting up python
import random
import time
import pygame
import sys
pygame.init()

#initialising variables needed and drawing the window
size = [1280, 720]
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED =(255,0,0)
AMBER = (255,128,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
wishlistDraw = 0
font = pygame.font.SysFont(None, 40)
font1 = pygame.font.SysFont(None,30)
font2 = pygame.font.SysFont(None, 25)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test Window')
screen.fill(WHITE)



#defining coordinates used in the movement() function
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

#creating an array used with the above coordinates in the iteratepath() function
vardict = { 't': t, 'a': a,
            'b': b, 'e': e,
            'g': g, 's': s,
            'f': f, 'h': h,
            'c': c, 'j': j,
            'i': i, 'd': d}

#initialising the waitTime variable which is used to change the rate 
#at which the screen refreshes
global waitTime
waitTime = 0.015

#defining the class for the treasure/score counter
class Counter():
    def __init__(self, score, x, y):
        self.score = score
        self.x = x
        self.y = y

    #function used to draw the initial score and text box
    def drawCounter(self):
        pygame.draw.rect(screen, BLACK, (self.x,self.y,100,100), 5)
        screen.blit(font.render(str(self.score), True, BLACK),
                    (self.x+30, self.y+35))
        screen.blit(font.render("Score", True, BLACK),(1060,330))
        screen.blit(font.render("Treasures", True, BLACK),(990,450))

    #function to draw the score when the treasure is collected
    #also sets score to new score
    def addScore(self, addScore):

        pygame.draw.rect(screen, WHITE, (self.x+30, self.y+35,50,50))
        screen.blit(font.render(str(self.score+addScore), True, BLACK),
                    (self.x+30, self.y+35))
        self.score = self.score+addScore

#defining the functions to draw lines and diamonds on the screen
def line(coods1, coods2):
        pygame.draw.lines(screen, RED, False,[coods1,coods2], 5)

#function used to draw the diamond shaped landmarks
def drawDiamond(x,y,n,colour):
    pygame.draw.polygon(screen, colour,[[x,y],[x+n,y+n],[x, y+2*n],[x-n,y+n]])

#function to draw every landmark, line and label
def drawScreen():
    line1 = line((154, 137),(80, 265))
    line2 = line ((80,265),(280,265))
    line3 = line((150,140),(280,265))
    line4 = line((280,265),(170,385))
    line5 = line((80,265),(170,385))
    line6 = line((170,385),(100,505))
    line7 = line((100,505),(300,505))
    line8 = line((100,505),(400,380))
    line9 = line((280,265),(400,380))
    line10 = line((300,505),(540,505))
    line11 =line((400,380),(540,505))
    line12 =line((400,380),(500,260))
    line13 =line((540,505),(700,380))
    line14 =line((750,265),(700,380))
    line15 = line((500,260),(750,260))
    line16 = line((540,505),(800,505))
    line17 = line((800,505),(700,380))

    diamondt = drawDiamond(150,130,15,BLACK)
    diamonda = drawDiamond(80,250,15,BLACK)
    diamondb = drawDiamond(280,250,15,BLACK)
    diamonde = drawDiamond(170,370,15,BLACK)
    diamondg = drawDiamond(100,490,15,BLACK)
    diamond6 = drawDiamond(300,490,15,BLACK)
    diamondf = drawDiamond(400,370,15,BLACK)
    diamondh = drawDiamond(540,490,15,BLACK)
    diamondc = drawDiamond(500,250,15,BLACK)
    diamondj = drawDiamond(750,250,15,BLACK)
    diamondi = drawDiamond(800,490,15,BLACK)
    diamondd = drawDiamond(700,370,15,BLACK)

    screen.blit(font1.render('1', True, BLACK),(90,200))
    screen.blit(font1.render('5', True, BLACK),(230,190))
    screen.blit(font1.render('2', True, BLACK),(110,330))
    screen.blit(font1.render('1', True, BLACK),(125,420))
    screen.blit(font1.render('4', True, BLACK),(175,235))
    screen.blit(font1.render('4', True, BLACK),(235,325))
    screen.blit(font1.render('6', True, BLACK),(325,325))
    screen.blit(font1.render('7', True, BLACK),(300,435))
    screen.blit(font1.render('1', True, BLACK),(215,515))
    screen.blit(font1.render('2', True, BLACK),(400,515))
    screen.blit(font1.render('2', True, BLACK),(450,435))
    screen.blit(font1.render('3', True, BLACK),(450,325))
    screen.blit(font1.render('4', True, BLACK),(675,515))
    screen.blit(font1.render('6', True, BLACK),(600,425))
    screen.blit(font1.render('1', True, BLACK),(600,275))
    screen.blit(font1.render('5', True, BLACK),(700,325))
    screen.blit(font1.render('3', True, BLACK),(725,425))

    if wishlistDraw == 1:
        screen.blit(font.render('You picked up the wishlisted treasure', True, BLACK),(350,190))
    
    drawAllTreasures()
    trap1.drawAllTraps()
    pygame.display.update()

"""
This code has been adapted from code taken from the site
http://geekly-yours.blogspot.co.uk/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html
"""
def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    #calculates a shortest path tree routed in src
    
    global distan
    global path
    global curLocal
    # a few sanity checks
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')    
    # ending condition
    if src == dest:
        
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
            distan = distances[dest]
        #print('shortest path: '+str(path)+" cost="+str(distances[dest]))
            
    else :     
        # if it is the initial run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        
        curLocal=min(unvisited, key=unvisited.get)
        
        dijkstra(graph,curLocal,dest,visited,distances,predecessors)

#function to draw the information box to detail the treasure location

def drawBox(Type):
    pygame.draw.rect(screen, WHITE, (120,580,800,100))
    screen.blit(font2.render(Type, True, BLACK),(120,580))
    pygame.display.update()

global ax
global ay        
global listtreasure
ax = 0
ay = 0
local = ()
listtreasure = []

#function used to redraw objects on the screen
def iteratepath():
    
    global x
    global local
    x = len(path)
    if x > 1:
        if local == ():
            local = vardict[path[x-1]]
        
        movement(vardict[path[x-1]], local)
        local = vardict[path[x-1]]
        path.pop(x-1)
        x -= 1
        iteratepath()
        #pygame.event.wait()
        
    elif x==1:
        endpos = path[0]
        movement(vardict[path[0]], local)
        tscore = 0
        global wishlistDraw
        if endpos == wishlistLocation:
            wishlistDraw = 1
        if landmarkTreasureState[endpos] == 0:
            print 'here'
        if landmarkTreasureState[endpos] == 1:
            tscore = 10
            listtreasure.append('Bronze')
            drawBox(str(listtreasure))
            print " You Found some Bronze."
           
        elif landmarkTreasureState[endpos] == 2:
            tscore = 20
            listtreasure.append('Silver')
            drawBox(str(listtreasure))
            print " You Found some Silver."
          
        elif landmarkTreasureState[endpos] == 3:
            tscore = 30
            listtreasure.append('Gold')
            drawBox(str(listtreasure))
            print " You Found some Gold."
           
        elif landmarkTreasureState[endpos] == 4:
            tscore = 40
            listtreasure.append('Platinum')
            drawBox(str(listtreasure))
            print " You Found some Platinum."
          
        elif landmarkTreasureState[endpos] == 5:
            tscore = 50
            listtreasure.append('Diamond')
            drawBox(str(listtreasure))
            print " You Found some Diamond."
        

            
        landmarkTreasureState[endpos] = 0
        local = vardict[path[0]]
        treasureCounter.addScore(1)
        scoreCounter.addScore(tscore-(distan))
        pygame.event.wait()
    
    trapstate(path[len(path)-1])
    landmarkTrapState[path[len(path)-1]] = 0 
        
def trapstate(locat):
    if landmarkTrapState[locat] == 1:
        trap1.trapaction()
        drawBox(str(listtreasure))
        print " You lost your last Treasure."
    if landmarkTrapState[locat] == 2:
        trap2.trapaction()
        drawBox(str(listtreasure))
        print " You lost your first Treasure."
    if landmarkTrapState[locat] == 3:
        trap3.trapaction()
        drawBox(str(listtreasure))
        print " You lost a random Treasure."

        
#defining variables used within the movement() function
amberCounter = 0
test = 0
counter = 0

#function that makes the robot move along the lines and controls the traffic light
def movement(dest, start):
    ax,ay = (start)
    bx,by=(dest)
    steps_number = max( abs(bx-ax), abs(by-ay) )
    if steps_number < 1:
        steps_number =1
    stepx = float(bx-ax)/steps_number
    stepy = float(by-ay)/steps_number
    
    for i in range(steps_number+1):

        global currentx
        global currenty
        currentx = ax + stepx*i
        currenty = ay + stepy*i
        
        int(ax + stepx*i), int(ay + stepy*i)   
        
        drawScreen()
        rectangle = pygame.draw.rect(screen, BLUE,(currentx,currenty, 10,  10 ))
        global amberCounter
        global waitTime
        global counter
        treasureCounter.drawCounter()
        scoreCounter.drawCounter()
        if counter != 5:
            counter = random.randint(0,100)
        
        time.sleep(waitTime)
        
        pygame.display.update()


       
landmarkCoords ={'t' : (145, 138), 'a' : (75, 258) ,
                 'b' : (275, 258), 'e' : (165, 378),
                 'g' : (95 , 498), 's' : (295, 498),
                 'f' : (395, 378), 'h' : (535, 498),
                 'c' : (495, 258), 'j' : (745, 258),
                 'i' : (795, 498), 'd' : (695, 378)}

landmarkTreasureState ={'t' : 0, 'a' : 0,
                        'b' : 0, 'e' : 0,
                        'g' : 0, 's' : 0,
                        'f' : 0, 'h' : 0,
                        'c' : 0, 'j' : 0,
                        'i' : 0, 'd' : 0}

landmarkTrapState = {'t' : 0, 'a' : 0,
                     'b' : 0, 'e' : 0,
                     'g' : 0, 's' : 0,
                     'f' : 0, 'h' : 0,
                     'c' : 0, 'j' : 0,
                     'i' : 0, 'd' : 0}

TreasureLocations =[]
global wishlistLoop
wishlistLoop = 0

def userInputTreasureLocation():
    global treasureLocation
    global wishlistLocation
    global wishlistLoop
    treasureLocation = raw_input("Input treasure location(a,b,c,d,e,f,g,h,s,t): ")
    landmarkTreasureState[treasureLocation] = random.randint(1,5)
    while wishlistLoop == 0:
        print "This is your wishlist treasure."
        wishlistLocation = treasureLocation
        wishlistLoop = 1

def drawAllTreasures():
    for key in landmarkTreasureState:
        if landmarkTreasureState[key] > 0:
            x, y = (landmarkCoords[key])
            pygame.draw.rect(screen, YELLOW,(x,y,10,10))
        
    pygame.display.flip()


def trapLocation():
    global traploca
    if trspawn == 0:
         traploca = 't'
    elif trspawn == 1:
        traploca = 'a'
    elif trspawn == 2:
        traploca = 'b'
    elif trspawn == 3:
        traploca = 'e'
    elif trspawn == 4:
        traploca = 'g'
    elif trspawn == 5:
        traploca = 's'
    elif trspawn == 6:
        traploca = 'f'
    elif trspawn == 7:
        traploca = 'h'
    elif trspawn == 8:
        traploca = 'c'
    elif trspawn == 9:
        traploca = 'j'
    elif trspawn == 10:
        traploca = 'i'
    elif trspawn == 11:
        traploca = 'd'
        
class trap():
    def trapLocation(self):
        trapspawn = random.randint(0, 11)
        global traploca
        if trapspawn == 0:
             traploca = 't'
        elif trapspawn == 1:
            traploca = 'a'
        elif trapspawn == 2:
            traploca = 'b'
        elif trapspawn == 3:
            traploca = 'e'
        elif trapspawn == 4:
            traploca = 'g'
        elif trapspawn == 5:
            traploca = 's'
        elif trapspawn == 6:
            traploca = 'f'
        elif trapspawn == 7:
            traploca = 'h'
        elif trapspawn == 8:
            traploca = 'c'
        elif trapspawn == 9:
            traploca = 'j'
        elif trapspawn == 10:
            traploca = 'i'
        elif trapspawn == 11:
            traploca = 'd'
    def drawAllTraps(self):
        for key in landmarkTrapState:
            if landmarkTrapState[key] > 0:
                x, y = (landmarkCoords[key])
                pygame.draw.rect(screen, GREEN,(x+2,y+2,6,6))

class lasttrap(trap):
    def tstate(self):
        landmarkTrapState[traploca] = 1
    def trapaction(self):
        if len(listtreasure) > 0:
            listtreasure.pop(len(listtreasure) - 1)
            treasureCounter.score -= 1

class firsttrap(trap):
    def tstate(self):
        landmarkTrapState[traploca] = 2
    def trapaction(self):
        if len(listtreasure) > 0:
            listtreasure.pop(0)
            treasureCounter.score -= 1
class randtrap(trap):
    def tstate(self):
        landmarkTrapState[traploca] = 3
    def trapaction(self):
        if len(listtreasure) > 0:
            value = random.randrange(len(listtreasure))
            listtreasure.pop(value)
            treasureCounter.score -= 1


if __name__ == "__main__":
    
            #defining the array of nodes that the robot should navigate through
    graph = {'t': {'a': 1, 'b': 5},
            'a': {'t': 1, 'b': 4, 'e': 2},
            'b': {'a': 4, 't': 5, 'e': 4, 'f': 6},
            'e': {'a': 2, 'b': 4, 'g': 1},
            'c': {'f': 3, 'j': 1},
            'f': {'b': 6, 'c': 3, 'g': 7, 'h': 2},
            'j': {'c': 1, 'd': 5},
            'g': {'e': 1, 'f': 7, 's': 3},
            'd': {'j': 5, 'h': 6, 'i': 3},
            's': {'g': 3, 'h': 2},
            'h': {'s': 2, 'f': 2, 'i': 4, 'd':6},
            'i': {'h': 4, 'd': 3}}
    
    
    #defining the treasure/score counter and calling the draw function
    treasureCounter = Counter(0,1160,410)
    treasureCounter.drawCounter()
    scoreCounter = Counter(0,1160,300)
    scoreCounter.drawCounter()
    
    shortestdict = {}

    rspawn = raw_input("Input robot location(a,b,c,d,e,f,g,h,s,t): ")
    
    userInputTreasureLocation()
    dijkstra(graph,rspawn,treasureLocation , [], {}, {}) 
    shortestdict[treasureLocation] = distan
    
    userInputTreasureLocation()
    dijkstra(graph,rspawn,treasureLocation , [], {}, {})
    shortestdict[treasureLocation] = distan
             
    userInputTreasureLocation()
    dijkstra(graph,rspawn,treasureLocation , [], {}, {})
    shortestdict[treasureLocation] = distan
             
    userInputTreasureLocation()
    dijkstra(graph,rspawn,treasureLocation , [], {}, {})
    shortestdict[treasureLocation] = distan
             
    userInputTreasureLocation()
    dijkstra(graph,rspawn,treasureLocation , [], {}, {})
    shortestdict[treasureLocation] = distan


    
    trap1 = lasttrap()
    trap1.trapLocation()
    trap1.tstate()
    
    trap2 = firsttrap()
    trap2.trapLocation()
    trap2.tstate()
    
    trap3 = randtrap()
    trap3.trapLocation()
    trap3.tstate()
    
       
    drawScreen()
    pygame.event.wait()
    z = 0
    while len(shortestdict) > 0:
        if z < 1:
            dijkstra(graph,rspawn,min(shortestdict, key=shortestdict.get) , [], {}, {})
            z =1
            
        else:
            dijkstra(graph,curLocal,min(shortestdict, key=shortestdict.get) , [], {}, {})
            
        iteratepath()
        del shortestdict[min(shortestdict, key=shortestdict.get)]

    sortedlist = []
    
    def sortTreasuresAsc():
        if 'Bronze' in listtreasure:
            sortedlist.append('Bronze')
            listtreasure.pop(listtreasure.index('Bronze'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresAsc()
            
        if 'Silver' in listtreasure:
            sortedlist.append('Silver')
            listtreasure.pop(listtreasure.index('Silver'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresAsc()
            
        if 'Gold' in listtreasure:
            sortedlist.append('Gold')
            listtreasure.pop(listtreasure.index('Gold'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresAsc()
            
        if 'Platinum' in listtreasure:
            sortedlist.append('Platinum')
            listtreasure.pop(listtreasure.index('Platinum'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresAsc()
            
        if 'Diamond' in listtreasure:
            sortedlist.append('Diamond')
            listtreasure.pop(listtreasure.index('Diamond'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresAsc()

    def sortTreasuresDsc():
        if 'Diamond' in listtreasure:
            sortedlist.append('Diamond')
            listtreasure.pop(listtreasure.index('Diamond'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresDsc()
            
        if 'Platinum' in listtreasure:
            sortedlist.append('Platinum')
            listtreasure.pop(listtreasure.index('Platinum'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresDsc()
  
        if 'Gold' in listtreasure:
            sortedlist.append('Gold')
            listtreasure.pop(listtreasure.index('Gold'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresDsc()
            
        if 'Silver' in listtreasure:
            sortedlist.append('Silver')
            listtreasure.pop(listtreasure.index('Silver'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresDsc()
            
        if 'Bronze' in listtreasure:
            sortedlist.append('Bronze')
            listtreasure.pop(listtreasure.index('Bronze'))
            pygame.draw.rect(screen, WHITE, (120,580,500,200))
            screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
            screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))
            pygame.display.update()
            time.sleep(1)
            sortTreasuresDsc()

    pygame.draw.rect(screen, WHITE, (120,580,500,200))
    screen.blit(font2.render ('Sorting the list, please stand by...', True, BLACK),(120,580))
    pygame.display.update()
    
    sortOrder = raw_input("Sort ascending or descending? (a/d): ")
    pygame.event.wait()
    
    while len(listtreasure)>0:
        if sortOrder == "a":
            sortTreasuresAsc()
        elif sortOrder == "d":
            sortTreasuresDsc()

    time.sleep(1)
    pygame.draw.rect(screen, WHITE, (120,580,500,200))
    screen.blit(font2.render(str(listtreasure), True, BLACK),(120,580))
    screen.blit(font2.render(str(sortedlist), True, BLACK),(120,680))

    #script to easily close window if it runs through
    pygame.event.wait()
    pygame.display.update()
