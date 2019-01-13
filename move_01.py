import math
import os
import sys

import pygame

from sprite.ship import Ship

pygame.init()

clock = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 400, 400
GRAY = (200, 200, 200)
RED = (255, 0, 0)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("ship")
img_base_path = os.getcwd() + '/img/'

ship = Ship(img_base_path, "ship_black.png", "ship_flame_black.png")
ship.scale = 0.5
ship.show_rect = True
# 摩擦系数
friction = 0.995
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            # KEYUP时，熄火，动力归0
            ship.vr = 0
            ship.thrust = 0
            ship.set_flame(False)
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                ship.vr = 5
            elif keys[pygame.K_RIGHT]:
                ship.vr = -5
            if keys[pygame.K_UP]:
                # 按向上键时，点火，动力为0.3
                ship.set_flame(True)
                ship.thrust = 0.3
            else:
                ship.set_flame(False)

    # 将每一帧的底色先填充成白色
    screen.fill((255, 255, 255))

    if ship.show_rect:
        pygame.draw.line(screen, GRAY, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), 1)
        pygame.draw.line(screen, GRAY, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 1)

    ship.angle += ship.vr
    ax = math.cos(ship.angle * math.pi / 180) * ship.thrust
    # 注：pygame中，角度是逆时针转的，所以垂直加速度要取反
    ay = -1 * math.sin(ship.angle * math.pi / 180) * ship.thrust
    ship.vx += ax
    ship.vy += ay

    # 摩擦系数
    if math.fabs(ship.vx) > 0.001:
        ship.vx = ship.vx * friction
    if math.fabs(ship.vy) > 0.001:
        ship.vy = ship.vy * friction

    print("vx:", ship.vx)

    ship.rotate_zoom()
    ship.move()
    ship.draw(screen)

    # 更新画布
    pygame.display.update()
