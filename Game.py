import pygame
from Player import player
from Obstacles import obstacles


pygame.init()
pygame.display.set_caption("Cool Cat Game")
screen = pygame.display.set_mode((500, 700))
screen.fill((0,0,0))
clock = pygame.time.Clock()


gameover = False
LEFT = 0
RIGHT = 1
keys = [False, False]


p1 = player()

obst = []
for i in range(5):
    obst.append(obstacles())

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
    
    p1.move(keys)
    for i in range(len(obst)):
        obst[i].move()
        obst[i].atBottom = p1.collide(obst[i].xpos, obst[i].ypos, obst[i].width, obst[i].height, obst[i].atBottom)
    
    if p1.lives == 0:
        gameover = True
    screen.fill((0, 100, 100))
    p1.draw(screen)
    for i in range(len(obst)):
        obst[i].draw(screen)
    pygame.display.flip()
pygame.quit()