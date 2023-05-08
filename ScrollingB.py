import pygame

B1 = pygame.image.load("B1.png")
B1.set_colorkey((153, 217, 234))
B2 = pygame.image.load("B2.png")
Static = pygame.image.load("Static.png")


class BG:
    def __init__(self):
        self.ypos1 = 0
        self.vy1 = 0
        self.vy2 = 0
        self.ypos2 = -100
        self.ypos3 = -800
        self.vy3 = 0
    def move(self):
        if self.ypos1 >= 0:
            self.vy1 = 5
        if self.ypos1 > 700:
            self.ypos1 = -700
        
        
        if self.ypos2 >= 0 or self.ypos2 < 0:
            self.vy2 = 14
        if self.ypos2 > 700:
            self.ypos2 = -700
            
        if self.ypos3 >= 0 or self.ypos3 < 0:
            self.vy3 = 14
        if self.ypos3 > 700:
            self.ypos3 = -700
            
        self.ypos1 += self.vy1
        self.ypos2 += self.vy2
        self.ypos3 += self.vy3
    def draw(self, screen):
        screen.blit(Static, (0,0))
        screen.blit(B1, (0, self.ypos1))
        screen.blit(B2, (0, self.ypos2))
        screen.blit(B2, (0, self.ypos3))