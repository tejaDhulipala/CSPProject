import sys
import pygame as pg
from PlanetClass import *

# Initialize the library
pg.init()

size = width, height = 1600, 900
BLACK = 0, 0, 0

screen = pg.display.set_mode(size)

# Set up the planets
planetSystem = []
earth = Planet((800, 450), (0, 0), 200, planetSystem, color=(0, 255, 0))
mars = Planet((1000, 450), (0, 0), 1, planetSystem, color=(255, 100, 100))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

    # The drawing of stuff
    screen.fill(BLACK)
    for planet in planetSystem:
        planet.draw(screen)

    # Update variables
    for planet in planetSystem:
        planet.changePos(0.005)

    # Update every frame
    pg.display.flip()
