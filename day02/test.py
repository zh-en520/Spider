import pygame
import sys
def run_game():
    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption('飞船')
    bg_color=(230,0,0)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run_game()