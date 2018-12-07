import pygame
from DisplayScale import screen_width, screen_height
from Characters import Player

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.Surface((screen_width, screen_height))

player = Player(0, 0, 'Images/Tanks/Player_image.PNG')

done = True
clock = pygame.time.Clock()

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.ESCAPE:
            done = False

    win.blit(screen, (0, 0))
    
    clock.tick(40)
