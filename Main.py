import sys
import pygame as pg
from PlanetClass import *
from math import pow
from Button import *
from ConsoleInput import *
import time

# Set up the planets
planetSystem = []
# Use User Input to Create Planets
print("Welcome to Gravity Simulator! You can create bodies and see how they interact")
#print("Click Exit to Stop making Planets")

'''
while input("Create New Body? ") != "exit":
    mass = intInput("Enter the mass of the body: ")
    xVal = intInput("Enter body X-Value (0-1100): ")
    yVal = intInput("Enter body Y-Value (0-900): ")
    xV = intInput("Enter the x value of the body's initial velocity: ")
    yV = intInput("Enter the y value of the body's initial velocity: ")
    r = intInput("Enter the radius of the body (in pixels): ")
    planetSystem.append(Planet((xVal, yVal), (xV, yV), mass, planetSystem, r=r))
'''

# Var saying if they chose a planet
chosePlanet = 0 # Mass of Planet, 0 if not selected

# Initialize the library
pg.init()
pg.font.init()

size = width, height = 1600, 900
BLACK = 0, 0, 0
WHITE = 255, 255, 255

screen = pg.display.set_mode(size)


#moon = Planet((925, 500), (0, -5), 1, planetSystem, color=(100, 100, 100), r=5)
#earth = Planet((700, 500), (0, -18), 100, planetSystem, color=(0, 255, 0)) # -18
#mars = Planet((1000, 500), (0, -50), 100, planetSystem, color=(255, 255, 100))
#jupiter = Planet((900, 500), (0, -0.5), 1e5, planetSystem, color=(255, 0, 0)) # 12
#sun = Planet((500, 500), (0.1, 0), 1e10, planetSystem, color=(255, 255, 255), r=15)
#mercury = Planet((550, 500), (0, -20), 100, planetSystem, (200, 100, 100), r=8)
#venus = Planet((600, 500), (0, -1), 50, planetSystem, color=(255, 50, 50), r=10)
#blackhole = Planet((1200, 500), (0, 0), 1e20, planetSystem, color=WHITE)
#planetX = Planet((950, 500), (0, 0), 1e10, planetSystem, (0, 0, 255), r=15)

# Set up menu and buttons
runButton = GameButton((1350, 50), "Run", (255, 0, 0), 90, 60, lambda: run(planetSystem), textHeight=50)
resetButton = GameButton((1350, 250), "Reset", (255, 0, 0), 120, 60, lambda: reset(planetSystem), textHeight=50)
newPlanetButton1 = GameButton((1350, 400), "New Body (Mass=100)", (0, 200, 0), 170, 30, lambda: changeSelect(100), textHeight=20)
newPlanetButton2 = GameButton((1350, 450), "New Body (Mass=1e3)", (0, 200, 0), 170, 30, lambda: changeSelect(1e3), textHeight=20)
newPlanetButton3 = GameButton((1350, 500), "New Body (Mass=1e4)", (0, 200, 0), 170, 30, lambda: changeSelect(1e4), textHeight=20)
newPlanetButton4 = GameButton((1350, 550), "New Body (Mass=1e5)", (0, 200, 0), 170, 30, lambda: changeSelect(1e5), textHeight=20)
newPlanetButton5 = GameButton((1350, 600), "New Body (Mass=1e6)", (0, 200, 0), 170, 30, lambda: changeSelect(1e6), textHeight=20)
newPlanetButton6 = GameButton((1350, 650), "New Body (Mass=1e7)", (0, 200, 0), 170, 30, lambda: changeSelect(1e7), textHeight=20)

# Past positions
pastPoss = [[] for i in range(len(planetSystem))]

running = True
frameNumber = 0
screenPos = [0, 0]
adj = 0.5
mousecolor = (randrange(50, 255), randrange(50, 255), randrange(50, 255))
settingInitVelocity = False
planetSetLoc = (0, 0)
vSetCoeff = 0.1
while running:
    start = time.time()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            runButton.checkPos(pg.mouse.get_pos())
            resetButton.checkPos(pg.mouse.get_pos())
            if newPlanetButton1.checkTrue(pg.mouse.get_pos()):
                chosePlanet = 100
            elif newPlanetButton2.checkTrue(pg.mouse.get_pos()):
                chosePlanet = 1e3
            elif newPlanetButton3.checkTrue(pg.mouse.get_pos()):
                chosePlanet = 1e4
            elif newPlanetButton4.checkTrue(pg.mouse.get_pos()):
                chosePlanet = 1e5
            elif newPlanetButton5.checkTrue(pg.mouse.get_pos()):
                chosePlanet = 1e6
            elif newPlanetButton6.checkTrue(pg.mouse.get_pos()):
                chosePlanet = 1e7
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        adj = 1
    else:
        adj = 0.5
    if keys[pg.K_LEFT]:
        screenPos[0] -= adj
    elif keys[pg.K_RIGHT]:
        screenPos[0] += adj
    if keys[pg.K_UP]:
        screenPos[1] -= adj
    elif keys[pg.K_DOWN]:
        screenPos[1] += adj

    # The drawing of stuff
    screen.fill(BLACK)
    # Draw circles
    ind = 0
    for posList in pastPoss:
        if len(posList) > 2:
            newPosList = [toScreenPos(pos, screenPos) for pos in posList]
            pg.draw.aalines(screen, (planetSystem[ind].color), closed=False, points=newPosList)
        ind += 1
    for planet in planetSystem:
        planet.draw(screen, screenPos)
    # Line drawn for settings
    pg.draw.line(screen, WHITE, (1200, 0), (1200, 900), width=7)
    # Draw Buttons
    runButton.draw(screen)
    resetButton.draw(screen)
    newPlanetButton1.draw(screen)
    newPlanetButton2.draw(screen)
    newPlanetButton3.draw(screen)
    newPlanetButton4.draw(screen)
    newPlanetButton5.draw(screen)
    newPlanetButton6.draw(screen)

    # Update variables
    for i in range(10):
        for planet in planetSystem:
            planet.changeVals(0.05)
        for planet in planetSystem:
            planet.changePos(0.05)
    #print("Earth pos: " + str(earth.initpos))
    for i in range(len(pastPoss)):
        if not frameNumber % 5:
            pastPoss[i].append(deepcopy(planetSystem[i].pos))
        if len(pastPoss[i]) > 100:
            pastPoss[i].pop(0)

    # Putting the Planets in
    if chosePlanet:
        pg.draw.circle(screen, mousecolor, pg.mouse.get_pos(), (8 + 1 * log(chosePlanet, 10)))
        if pg.mouse.get_pos()[0] <= 1200 and pg.mouse.get_pressed()[0]:
            latest = Planet(pg.mouse.get_pos(), (0, 0), chosePlanet, planetSystem, mousecolor, r=(8 + 1 * log(chosePlanet, 10)))
            pastPoss.append([])
            mousecolor = (randrange(50, 255), randrange(50, 255), randrange(50, 255))
            chosePlanet = 0
            settingInitVelocity = True
            planetSetLoc = pg.mouse.get_pos()
    if settingInitVelocity:
        pg.draw.line(screen, (255, 0, 0), planetSetLoc, pg.mouse.get_pos())
        if pg.mouse.get_pos()[0] <= 1200 and pg.mouse.get_pressed()[0]:
            latest.v = (vSetCoeff * (pg.mouse.get_pos()[0] - planetSetLoc[0]), vSetCoeff * (pg.mouse.get_pos()[1] - planetSetLoc[1]))
            settingInitVelocity = False


    timePerRun = time.time() - start
    font = pg.font.SysFont("Arial", 20)
    text = font.render(str(round(1 / timePerRun)), True, WHITE)
    if len(planetSystem) > 0:
        runningText = font.render("Is running " + str(planetSystem[0].isRunning), True, WHITE)
    else:
        runningText = font.render("Is running: " + str(False), True, WHITE)
    screen.blit(text, (1550, 875))
    screen.blit(runningText, (1220, 875))

    # Update every frame
    pg.display.flip()
    frameNumber += 1