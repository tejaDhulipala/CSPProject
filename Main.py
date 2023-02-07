import sys
import pygame as pg
from PlanetClass import *
from math import pow
from Button import *

# Initialize the library
pg.init()
pg.font.init()

size = width, height = 1600, 900
BLACK = 0, 0, 0
WHITE = 255, 255, 255

screen = pg.display.set_mode(size)

# Set up the planets
planetSystem = []
#moon = Planet((925, 500), (0, -5), 1, planetSystem, color=(100, 100, 100), r=5)
#earth = Planet((700, 500), (0, -18), 100, planetSystem, color=(0, 255, 0)) # -18
#mars = Planet((1000, 450), (0, 2), 100, planetSystem, color=(255, 100, 100))
jupiter = Planet((900, 500), (0, 2), 1e4, planetSystem, color=(255, 0, 0)) # 12
sun = Planet((500, 500), (0, 0), 1e10, planetSystem, color=(255, 255, 255), r=15)
mercury = Planet((550, 500), (0, -8), 100, planetSystem, (200, 100, 100), r=8)
venus = Planet((600, 500), (0, -12), 50, planetSystem, color=(255, 50, 50), r=10)
#blackhole = Planet((700, 700), (0, 0), 1e10, planetSystem, color=(0, 0, 0))
planetX = Planet((950, 500), (0, 0), 1e10, planetSystem, (0, 0, 255), r=15)
print(planetSystem)

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
            planet.changeVals(0.1)
        for planet in planetSystem:
            planet.changePos(0.1)
    #print("Earth pos: " + str(earth.initpos))
    for i in range(len(pastPoss)):
        if not frameNumber % 10:
            pastPoss[i].append(deepcopy(planetSystem[i].pos))
        if len(pastPoss[i]) > 200:
            pastPoss[i].pop(0)

    # Update every frame
    pg.display.flip()
    frameNumber += 1
    #print(frameNumber)