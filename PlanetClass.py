import pygame as pg
import random
from math import log, pow

# The conversion of the mass to the radius, how much the mass is multiplied by to get the radius
from pygame.math import Vector2

#massToRadius = 1
G = 1


class Planet:
    v: Vector2
    pos: Vector2

    def __init__(self, pos, v, m, system: list, color=(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)), a=pg.Vector2(0, 0)):
        self.initpos = pg.math.Vector2(pos)
        self.initv = pg.math.Vector2(v)
        self.pos = pg.math.Vector2(pos)
        self.v = pg.math.Vector2(v)
        self.m = m
        self.color = color
        self.system = system
        self.a = a
        self.isRunning = False
        system.append(self)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, 12)
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
