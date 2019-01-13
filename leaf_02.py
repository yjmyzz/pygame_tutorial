import sys

import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 200, 400
BLACK = 0, 0, 0
angle = 1

screen = pygame.display.set_mode(SIZE)
leaf = pygame.image.load("leaf.png")
leafRect = leaf.get_rect()
leafRect = leafRect.move((WIDTH - leafRect.width) / 2, (HEIGHT - leafRect.height) / 2)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    # 旋转图片(注意：这里要搞一个新变量，存储旋转后的图片）
    newLeaf = pygame.transform.rotate(leaf, angle)
    newRect = newLeaf.get_rect()
    angle += 1

    screen.fill(BLACK)
    screen.blit(newLeaf, leafRect)
    pygame.draw.rect(screen, (255, 0, 0), leafRect, 1)
    pygame.draw.rect(screen, (0, 255, 0), newRect, 1)
    pygame.display.update()
    clock.tick(100)
