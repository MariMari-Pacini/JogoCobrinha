import pygame
from pygame.locals import *

janela_jogo = (800, 600)
pixel_size = 10

pygame.init()
screen = pygame.display.set_mode(janela_jogo)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((pixel_size, pixel_size))
snake_surface.fill((37, 186, 55))

apple_surface = pygame.Surface((pixel_size, pixel_size))
apple_surface.fill((212, 32, 4))

clock = pygame.time.Clock()

while True:
    clock.tick(15)
    
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    
    for pos in snake_pos:
        screen.blit(snake_surface, pos)
    
    snake_pos[0] = snake_pos[0][0] + 10, snake_pos[0][1]
        
    pygame.display.update()
