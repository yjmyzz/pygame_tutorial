import pygame

pygame.init()
pygame.display.set_mode((400, 400))
pygame.display.set_caption("first game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
