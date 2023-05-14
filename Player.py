import pygame
pygame.mixer.init()


LEFT = 0
RIGHT = 1


Super = pygame.image.load("SuperCat.png")
Super.set_colorkey((255,255,255))
ls = pygame.image.load("lives.png")
hurt = pygame.mixer.Sound('Hit.mp3')
class player:
    def __init__(self):
        self.xpos = 250
        self.ypos = 575
        self.vx = 0
        self.isAlive = True
        self.hp = 100
        self.lives = 3
        
        self.movingx = False
        #animation variables
        self.frameWidth = 27
        self.frameHeight = 49
        self.RowNum = 0 #for left animation, this will need to change for other animations
        self.frameNum = 0
        self.ticker = 0
        
    def move(self, keys):        
        if keys[LEFT] == True:
            self.vx = -5
            self.movingx = True
        elif keys[RIGHT] ==True:
            self.vx = 5
            self.movingx = True
        else:
            self.vx = 0
            
        self.xpos += self.vx
    def collide(self, Ox, Oy, width, height, Bottom):
        #collision
        if self.ypos + self.frameHeight >= Oy and self.ypos <= Oy + height and self.xpos + self.frameWidth >= Ox and self.xpos <= Ox + width:
            self.hp -= 10
            pygame.mixer.Sound.play(hurt)
#             print(self.hp)
            Bottom = True
        #check the sides of the screen to see if we're within the bounds
        if self.xpos + self.frameWidth >= 500:
            self.xpos = 500 - self.frameWidth
        if self.xpos <= 0:
            self.xpos =0 
        #losing a life
            
        if self.hp >= 100:
            self.hp = 100
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
        lframe = 0
        lrow = 0
        lwidth = 15
        lheight = 15
        
        
        #animation
        if self.movingx == True: #animate when moving
            self.ticker+=1
        if self.ticker % 10 == 0: #only change frames every 10 ticks
          self.frameNum+=1
        if self.frameNum > 2: 
           self.frameNum = 0
        
        
        #health bar
        if self.hp > 60: 
            pygame.draw.rect(screen, (0, 255, 0), (20, 20, self.hp, 20))
        elif self.hp > 30:
            pygame.draw.rect(screen, (255, 255, 0), (20, 20, self.hp, 20))
        elif self.hp > 0:
            pygame.draw.rect(screen, (255, 0, 0), (20, 20, self.hp, 20))    
        pygame.draw.rect(screen, (0,0,0), (20, 20, 100, 20), 5)
        
        #lives
        if self.lives == 3:
            screen.blit(ls, (21, 40), (lwidth * lframe, lrow * lheight, lwidth, lheight))
            screen.blit(ls, (41, 40), (lwidth * lframe, lrow * lheight, lwidth, lheight))
            screen.blit(ls, (61, 40), (lwidth * lframe, lrow * lheight, lwidth, lheight))
        if self.lives == 2:
            screen.blit(ls, (21, 40), (lwidth * lframe, lrow * lheight, lwidth, lheight))
            screen.blit(ls, (41, 40), (lwidth * lframe, lrow * lheight, lwidth, lheight))
            screen.blit(ls, (61, 40), (lwidth * lframe+15, lrow * lheight, lwidth, lheight))
        if self.lives == 1:
            screen.blit(ls, (21, 40), (lwidth * lframe, lrow * lheight, lwidth, lheight))
            screen.blit(ls, (41, 40), (lwidth * lframe+15, lrow * lheight, lwidth, lheight))
            screen.blit(ls, (61, 40), (lwidth * lframe+15, lrow * lheight, lwidth, lheight))
            
        #draws player if they are alive
        if self.isAlive == True:
            #pygame.draw.rect(screen, (0, 255, 0), (self.xpos, self.ypos, 50, 50))
            screen.blit(Super, (self.xpos, self.ypos), (self.frameWidth * self.frameNum, self.RowNum * self.frameHeight, self.frameWidth, self.frameHeight))
        