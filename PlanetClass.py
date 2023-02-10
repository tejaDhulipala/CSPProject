import pygame as pg
from random import randrange
from math import log, pow
from copy import deepcopy
from ConsoleInput import *

# The conversion of the mass to the radius, how much the mass is multiplied by to get the radius
from pygame.math import Vector2

#massToRadius = 1
G = 1 # whatever I want it to be screw u


class Planet:
    v: Vector2
    pos: Vector2

    def __init__(self, pos, v, m, system: list, color=(-1, -1, -1), a=pg.Vector2(0, 0), r=12):
        self.initpos = pg.math.Vector2(deepcopy(pos))
        self.initv = pg.math.Vector2(deepcopy(v))
        self.pos = pg.math.Vector2(pos)
        self.v = pg.math.Vector2(v)
        self.m = m
        self.color = color
        self.system = system
        self.a = a
        self.isRunning = False
        self.r = r
        self.color = (randrange(0, 256), randrange(0, 256), randrange(0, 256)) if color == (-1, -1, -1) else color
        system.append(self)

    def draw(self, screen, screenPos):
        pg.draw.circle(screen, self.color, toScreenPos(self.pos, screenPos), self.r)
        #pg.draw.line(screen, (255, 0, 0), self.pos, self.pos + self.a * 10000, 2)

    def changeVals(self, t):
        if self.isRunning:
            f = pg.Vector2(0, 0)
            # The sum of the forces acting on the planets
            # |F| = Gm1m2 ./ r ^2
            for planet in self.system:
                if planet != self:
                    mag = G * self.m * planet.m / (self.pos - planet.pos).length_squared()
                    if mag > (planet.pos - self.pos).length():
                        mag = (planet.pos - self.pos).length()
                    f += mag * (planet.pos - self.pos) / (planet.pos - self.pos).length()
            self.a = f / self.m
            self.v += self.a * t

    def changePos(self, t):
        if self.isRunning:
            self.pos += self.v * t
