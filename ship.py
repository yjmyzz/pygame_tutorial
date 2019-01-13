import math
import os
import sys

import pygame

pygame.init()

clock = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 400, 400
GRAY = (200, 200, 200)
RED = (255, 0, 0)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("ship")
img_base_path = os.getcwd() + '/img/'


class Ship(object):
    def __init__(self, img_base_path, screen):
        self.vx = 0
        self.vy = 0
        # 旋转角速度
        self.vr = 0
        # 推进力
        self.thrust = 0
        self.angle = 0
        self.show_flame = False
        self.scale = 1.0
        # 是否显示辅助边框
        self.show_rect = False

        self.img_src = pygame.image.load(img_base_path + 'ship.png')
        self.img_flame_src = pygame.image.load(img_base_path + 'ship_flame.png')

        self.img = self.img_src
        self.rect = self.img_src.get_rect()

        self.img_new = self.img
        self.rect_new = self.img_new.get_rect()

        self.rect = self.rect.move((WIDTH - self.rect.width) * 0.5, (HEIGHT - self.rect.height) * 0.5)

    def draw(self, screen):
        screen.blit(self.img_new, self.rect_new)
        if self.show_rect:
            pygame.draw.rect(screen, GRAY, ship.rect, 1)
            pygame.draw.rect(screen, RED, ship.rect_new, 1)

    def move(self):
        self.rect = self.rect.move(self.vx, self.vy)
        self.rect_new = self.rect_new.move(self.vx, self.vy)
        # 向左飞出边界
        if self.rect_new.right < 0 and ship.vx < 0:
            self.rect_new.left = WIDTH
            self.rect.left = WIDTH
        # 向右飞出边界
        if self.rect_new.left > WIDTH and ship.vx > 0:
            self.rect_new.right = 0
            self.rect.right = 0
        # 向下飞出边界
        if self.rect_new.top > HEIGHT and ship.vy > 0:
            self.rect_new.bottom = 0
            self.rect.bottom = 0
        # 向上飞出边界
        if self.rect_new.bottom < 0 and ship.vy < 0:
            self.rect_new.top = HEIGHT
            self.rect.top = HEIGHT

    def rotate_zoom(self):
        # rotozoom=旋转+缩放
        self.img_new = pygame.transform.rotozoom(self.img, self.angle, self.scale)
        self.rect_new = self.img_new.get_rect(center=self.rect.center)
        if math.fabs(self.angle) == 360:
            self.angle = 0

    def set_flame(self, show_flame=False):
        self.show_flame = show_flame
        if self.show_flame:
            self.img = self.img_flame_src
        else:
            self.img = self.img_src


def get_speed(speed):
    if speed > 0:
        return math.ceil(speed)
    if speed < 0:
        return math.floor(speed)
    return speed


ship = Ship(img_base_path, screen)
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
