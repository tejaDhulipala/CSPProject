import pygame as pg
import random
from math import log

# The conversion of the mass to the radius, how much the mass is multiplied by to get the radius
from pygame.math import Vector2

massToRadius = 5
G = 0.005


class Planet:
    v: Vector2
    pos: Vector2

    def __init__(self, pos, v, m, system: list, color=(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)), a=pg.Vector2(0, 0)):
        self.pos = pg.math.Vector2(pos)
        self.v = pg.math.Vector2(v)
        self.m = m
        self.color = color
        self.system = system
        self.a = a
        system.append(self)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.pos, log(self.m + 1) * massToRadius)

    def changePos(self, t):
        f = pg.Vector2(0, 0)
        # The sum of the forces acting on the planets
        # F = G * m1 * m2  r^2
        for planet in self.system:
            if planet != self:
                f += (G * self.m * planet.m / (self.pos - planet.pos).length_squared()) * (planet.pos - self.pos)
        # Now that we have the sum of the forces as a vector, we have to convert that into acceleration
        self.a += f / self.m * t
        self.v += self.a
        self.pos += self.v
