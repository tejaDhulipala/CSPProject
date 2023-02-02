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
earth = Planet((800, 500), (0, 0), 10, planetSystem, color=(0, 255, 0))
#mars = Planet((1000, 450), (0, 2), 100, planetSystem, color=(255, 100, 100))
#jupiter = Planet((450, 450), (0, 0), 1000, planetSystem, color=(255, 0, 0))
sun = Planet((500, 500), (0, 0), 10000, planetSystem, color=(255, 255, 255))

# Set up menu and buttons
runButton = GameButton((1350, 50), "Run", (255, 0, 0), 90, 60, lambda: run(planetSystem), textHeight=50)
resetButton = GameButton((1350, 250), "Reset", (255, 0, 0), 120, 60, lambda: reset(planetSystem), textHeight=50)

running = True
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
    for planet in planetSystem:
        planet.draw(screen)
    # Line drawn for settings
    pg.draw.line(screen, WHITE, (1200, 0), (1200, 900), width=7)
    # Draw Buttons
    runButton.draw(screen)
    resetButton.draw(screen)

    # Update variables
    for planet in planetSystem:
        planet.changeVals(0.1)
    for planet in planetSystem:
        planet.changePos(0.1)

    # Update every frame
    pg.display.flip()
