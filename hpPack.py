import pygame
import random
pygame.mixer.init()
Health = pygame.image.load("Health.png")

heal = pygame.mixer.Sound('Heal.wav')
class HealthPack:
    def __init__(self):
        self.x = random.randrange(0, 475)
        self.y = 0
        self.vy = 0
        self.width = 25
        self.height = 25
        self.frameNum = 0
        self.RowNum = 0
        self.aniticker = 0
        
        self.ticker = 0
        
        self.isAlive = False
        
    def move(self):
        if self.y < 700:
            self.vy = 5
        else:
            self.ticker += 1
            if self.ticker % 1000 == 0:
                self.y = 0
                self.x = random.randrange(0,475)
                self.ticker = 0
                self.isAlive = True
                
        self.y += self.vy

    def collide(self, Px, Py, Pw, Ph, health):
        if Py + Ph >= self.y and Py <= self.y + self.height and Px + Pw >= self.x and Px <= self.x + self.width:
            if health < 100:
                if self.isAlive == True:
                    pygame.mixer.Sound.play(heal)
                    health += 14
                    self.y = 0
                    self.isAlive = False
                
        return health
    def draw(self, screen):
        if self.y > 0 and self.y < 700: #animate when moving
            self.aniticker+=1
        else:
            self.aniticker = 0
        if self.aniticker % 20 == 0: #only change frames every 10 ticks
          self.frameNum+=1
        if self.frameNum > 1: 
           self.frameNum = 0
           
        if self.isAlive == True:
            #pygame.draw.rect(screen, (0, 255, 150), (self.x, self.y, self.width, self.height))
            screen.blit(Health, (self.x, self.y), (self.width * self.frameNum, self.RowNum * self.height, self.width, self.height))
