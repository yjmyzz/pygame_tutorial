import sys

import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 200, 400
BLACK = 0, 0, 0
angle = 1

screen = pygame.display.set_mode(SIZE)
leaf = pygame.image.load("leaf.png")
leafRect = leaf.get_rect()
# 定位到舞台中心
leafRect = leafRect.move((WIDTH - leafRect.width) / 2, (HEIGHT - leafRect.height) / 2)

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 旋转图片
    leaf = pygame.transform.rotate(leaf, angle)
    angle += 1

    # 默认背景为白色，所以每渲染一帧，要对背景重新填充，否则会有上一帧的残影
    screen.fill(BLACK)
    # 将旋转后的图象，渲染矩形里
    screen.blit(leaf, leafRect)
    # 正式渲染
    pygame.display.update()
    # 控制帧数<=100
    clock.tick(100)

version-1