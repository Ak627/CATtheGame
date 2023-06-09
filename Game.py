import pygame
import time
from Player import player
from Obstacles import obstacles
from hpPack import HealthPack
from coin import Coin
from ScrollingB import BG
import SplashScreens
import End
#screen setup
pygame.init()
pygame.display.set_caption("Cool Cat Game")
screen = pygame.display.set_mode((500, 700))
screen.fill((0,0,0))
clock = pygame.time.Clock()

collect = pygame.mixer.Sound('collect.wav')

#game variables
score = 0
gameover = False
LEFT = 0
RIGHT = 1
keys = [False, False]

#creations of objects(players, obstacles, ect.)
p1 = player()
hp = HealthPack()

obst = []
for i in range(10):
    obst.append(obstacles())
    
coins = []
for i in range(3):
    coins.append(Coin())


back = BG()


SplashScreens.PlayIntro(screen)
while not gameover:
    clock.tick(60)
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=True
            elif event.key == pygame.K_d:
                keys[RIGHT]=True
        
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys[LEFT]=False
            elif event.key == pygame.K_d:
                keys[RIGHT]=False   
    #physics section --------------------------------------------------------------
    p1.move(keys)
    hp.move()
    back.move()
    for i in range(len(obst)):
        obst[i].move()
        obst[i].atBottom = p1.collide(obst[i].xpos, obst[i].ypos, obst[i].width, obst[i].height, obst[i].atBottom)
    p1.hp = hp.collide(p1.xpos, p1.ypos, p1.frameHeight, p1.frameWidth, p1.hp)
    
    for i in range(len(coins)):
        coins[i].move()
        score = coins[i].collide(p1.xpos, p1.ypos, p1.frameHeight, p1.frameWidth, score)
     
    
        
    #render section ------------------------------------------------------------------------
    screen.fill((153, 217, 234))
    back.draw(screen)
    p1.draw(screen)
    hp.draw(screen)
    for i in range(len(obst)):
        obst[i].draw(screen)
    for i in range(len(coins)):
        coins[i].draw(screen)
    
    font = pygame.font.Font(None, 40)
    text = font.render(str(score),1, (255, 48, 55))
    screen.blit(text, (450,25))
    text = font.render(str("Score: "),1, (255, 48, 55))
    screen.blit(text, (360,25))
    
    if p1.lives == 0:
        End.end('L')
        gameover = True
        
    if score >= 20:
        End.end('W')
        gameover = True
            
    pygame.display.flip()
pygame.quit()