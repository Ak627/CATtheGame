import pygame
LEFT = 0
RIGHT = 1


class player:
    def __init__(self):
        self.xpos = 250
        self.ypos = 575
        self.vx = 0
        self.isAlive = True
        self.hp = 100
        self.lives = 3
    def move(self, keys):        
        if keys[LEFT] == True:
            self.vx = -5
        elif keys[RIGHT] ==True:
            self.vx = 5
        else:
            self.vx = 0
            
        self.xpos += self.vx
    def collide(self, Ox, Oy, width, height, Bottom):
        #collision
        if self.ypos >= Oy and self.ypos <= Oy + height and self.xpos >= Ox and self.xpos <= Ox + width:
            self.hp -= 10
            print(self.hp)
            Bottom = True
        #losing a life
        if self.hp <= 0:
            pygame.time.wait(1000)
            self.isAlive = False
            self.lives -= 1
            self.xpos = 250
            self.ypos = 575
            self.hp = 100
            self.isAlive = True
        return Bottom
    def draw(self, screen):
        #health bar
        if self.hp > 60: 
            pygame.draw.rect(screen, (0, 255, 0), (20, 20, self.hp, 20))
        elif self.hp > 20:
            pygame.draw.rect(screen, (255, 255, 0), (20, 20, self.hp, 20))
        elif self.hp > 20:
            pygame.draw.rect(screen, (255, 0, 0), (20, 20, self.hp, 20))    
        pygame.draw.rect(screen, (0,0,0), (20, 20, 100, 20), 2)
        
        
        if self.isAlive == True:
            pygame.draw.rect(screen, (0, 255, 0), (self.xpos, self.ypos, 50, 50))
        