import pygame as pg


class GameButton:
    def __init__(self, pos, text, color, width, height, callback, textHeight=20):
        self.pos = pos
        self.text = text
        self.callback = callback
        self.color = color
        self.width = width
        self.height = height
        self.textHeight = textHeight

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), pg.Rect(self.pos, (self.width, self.height)), border_radius=5)
        font = pg.font.SysFont("Arial", self.textHeight)
        text = font.render(self.text, True, self.color)
        screen.blit(text, self.pos)

    def checkPos(self, pos):
        if self.pos[0] <= pos[0] <= self.pos[0] + self.width and self.pos[1] <= pos[1] <= self.pos[1] + self.height:
            self.callback()

    def checkTrue(self, pos):
        if self.pos[0] <= pos[0] <= self.pos[0] + self.width and self.pos[1] <= pos[1] <= self.pos[1] + self.height:
            return True
        return False


# Control Functions
def run(sys):
    for planet in sys:
        planet.isRunning = True


def reset(sys):
    for planet in sys:
        planet.v = planet.initv
        planet.pos = planet.initpos
        planet.isRunning = False

def changeSelect(mass):
    global chosePlanet
    chosePlanet = mass
    print("changed")
    print(chosePlanet)
