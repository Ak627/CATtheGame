import pygame
import random

c = pygame.image.load("Coin.png")
c.set_colorkey((255,255,255))

class Coin:
    def __init__(self):
        self.xpos = random.randrange(0, 480)
        self.ypos = 0
        
        self.width = 20
        self.height = 20
        self.aniticker = 0
        self.RowNum = 0
        self.frameNum = 0
        
        self.vy = 0
        self.ticker = 0
        
        self.isAlive = False
    def move(self):
        if self.ypos < 700:
            self.vy = 6
        else:
            self.ticker += 1
            if self.ticker % 600 == 0:
                self.ypos = 0
                self.xpos = random.randrange(0,480)
                self.ticker = 0
                self.isAlive = True
                
        self.ypos += self.vy
    def collide(self, Px, Py, Pw, Ph, score):
        if Py + Ph >= self.ypos and Py <= self.ypos + self.height and Px + Pw >= self.xpos and Px <= self.xpos + self.width:
            if self.isAlive == True:
                score += 1
                self.ypos = 0
                self.isAlive = False
        return score
    def draw(self, screen):
        if self.ypos > 0 and self.ypos < 700: #animate when moving
            self.aniticker+=1
        else:
            self.aniticker = 0
        if self.aniticker % 10 == 0: #only change frames every 10 ticks
          self.frameNum+=1
        if self.frameNum > 5: 
           self.frameNum = 0
           
        if self.isAlive == True:
            #pygame.draw.rect(screen, (0, 255, 150), (self.x, self.y, self.width, self.height))
            screen.blit(c, (self.xpos, self.ypos), (self.width * self.frameNum, self.RowNum * self.height, self.width, self.height))