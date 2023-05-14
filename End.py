import pygame
import time
import moviepy
from moviepy.editor import *
import os

pygame.display.set_caption("Cool Cat Game")
screen = pygame.display.set_mode((500, 700))
screen.fill((153, 217, 234))

death = pygame.image.load(r'Death.png')
daeth_size = death.get_rect().size

def end(choice):
    if choice == 'W':
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        clip = VideoFileClip('Winning.mp4')


        clip.preview()
    elif choice == 'L':
        music = pygame.mixer.music.load('Sad.mp3')
        pygame.mixer.music.play()
        for x in range(255):
            screen.fill((0,0,0))
            death.set_alpha(x)    
            screen.blit(death, (0,0))   
            pygame.display.flip()
            time.sleep(10 / 1000)
        for x in range(255):
            screen.fill((0,0,0))
            death.set_alpha(255)    
            screen.blit(death, (0,0))   
            pygame.display.flip()
            time.sleep(10 / 1000)
        for x in range(255):
            screen.fill((0,0,0))
            death.set_alpha(255-x)    
            screen.blit(death, (0,0))   
            pygame.display.flip()
            time.sleep(10 / 1000)
