import pygame


import random

class obstacles:
    def __init__(self):
        self.xpos = random.randrange(10, 490)
        self.ypos = 0
        self.vy = 0
        self.width = random.randrange(25, 125)
        self.height = 10
        self.atBottom = False
    def move(self):
        if self.atBottom == False:
            self.vy = 5
        else:
            self.vy = 0
            self.ypos = 0
            self.xpos = random.randrange(10, 490)
            self.width = random.randrange(25, 125)
        self.ypos += 5

        if self.ypos >= 700:
            self.atBottom = True
        else:
            self.atBottom = False
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xpos, self.ypos, self.width, self.height), 5)