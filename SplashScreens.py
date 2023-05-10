import pygame
import time
back = pygame.image.load(r'Company logo.png')
back_size = back.get_rect().size

title = pygame.image.load(r'title.png')
title_size = title.get_rect().size


def PlayIntro(screen):
    ticker = 0
    frameNum = 0
    RowNum = 0
    width = 500
    height = 700
    for x in range(255):
        screen.fill((0,0,0))
        back.set_alpha(x)    
        screen.blit(back, (0,0))   
        pygame.display.flip()
        time.sleep(10 / 1000)
    for x in range(255):
        screen.fill((0,0,0))
        back.set_alpha(255-x)    
        screen.blit(back, (0,0))   
        pygame.display.flip()
        time.sleep(10 / 1000)
    for x in range(255):
        if x <= 255:
            ticker += 1
        if ticker%50 == 0:
            frameNum += 1
        if frameNum > 1:
            frameNum = 0
        screen.fill((0,0,0))
        title.set_alpha(x)    
        screen.blit(title, (0,0),(width * frameNum, RowNum * height, width, height))   
        pygame.display.flip()
        time.sleep(10 / 1000)
    for x in range(255):
        if x <= 255:
            ticker += 1
        if ticker%50 == 0:
            frameNum += 1
        if frameNum > 1:
            frameNum = 0
        screen.fill((0,0,0))
        title.set_alpha(255-x)    
        screen.blit(title, (0,0),(width * frameNum, RowNum * height, width, height))   
        pygame.display.flip()
        time.sleep(10 / 1000)
