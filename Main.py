import sys
import pygame as pg
from PlanetClass import *
from math import pow
from Button import *
from ConsoleInput import *

# Initialize the library
pg.init()
pg.font.init()

size = width, height = 1600, 900
BLACK = 0, 0, 0
WHITE = 255, 255, 255

screen = pg.display.set_mode(size)

# Set up the planets
planetSystem = []
# Use User Input to Create Planets
print("Welcome to Gravity Simulator! You can create bodies and see how they interact")
print("Click Exit to Stop making Planets")
while input("Create New Body? ") != "exit":
    mass = intInput("Enter the mass of the body: ")
    xVal = intInput("Enter body X-Value (0-1100): ")
    yVal = intInput("Enter body Y-Value (0-900): ")
    xV = intInput("Enter the x value of the body's initial velocity: ")
    yV = intInput("Enter the y value of the body's initial velocity: ")
    r = intInput("Enter the radius of the body (in pixels): ")
    planetSystem.append(Planet((xVal, yVal), (xV, yV), mass, planetSystem, r=r))


#moon = Planet((925, 500), (0, -5), 1, planetSystem, color=(100, 100, 100), r=5)
#earth = Planet((700, 500), (0, -18), 100, planetSystem, color=(0, 255, 0)) # -18
#mars = Planet((1000, 500), (0, -50), 100, planetSystem, color=(255, 255, 100))
#jupiter = Planet((900, 500), (0, -0.5), 1e6, planetSystem, color=(255, 0, 0)) # 12
#sun = Planet((500, 500), (0, 0), 1e10, planetSystem, color=(255, 255, 255), r=15)
#mercury = Planet((550, 500), (0, -20), 100, planetSystem, (200, 100, 100), r=8)
#venus = Planet((600, 500), (0, -12), 50, planetSystem, color=(255, 50, 50), r=10)
#blackhole = Planet((1200, 500), (0, 0), 1e20, planetSystem, color=WHITE)
#planetX = Planet((950, 500), (0, 0), 1e10, planetSystem, (0, 0, 255), r=15)


# Set up menu and buttons
runButton = GameButton((1350, 50), "Run", (255, 0, 0), 90, 60, lambda: run(planetSystem), textHeight=50)
resetButton = GameButton((1350, 250), "Reset", (255, 0, 0), 120, 60, lambda: reset(planetSystem), textHeight=50)

# Past positions
pastPoss = [[] for i in range(len(planetSystem))]

running = True
frameNumber = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            runButton.checkPos(pg.mouse.get_pos())
            resetButton.checkPos(pg.mouse.get_pos())


    # The drawing of stuff
    screen.fill(BLACK)
    # Draw circles
    ind = 0
    for posList in pastPoss:
        if len(posList) > 2:
            pg.draw.aalines(screen, (planetSystem[ind].color), closed=False, points=posList)
        ind += 1
    for planet in planetSystem:
        planet.draw(screen)
    # Line drawn for settings
    pg.draw.line(screen, WHITE, (1200, 0), (1200, 900), width=7)
    # Draw Buttons
    runButton.draw(screen)
    resetButton.draw(screen)


    # Update variables
    for i in range(2):
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

    # Update every frame
    pg.display.flip()
    frameNumber += 1
    #print(frameNumber)