import math
import random
import sys

import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 200, 400
BACKGROUND_COLOR = (230, 255, 230)

screen = pygame.display.set_mode(SIZE)
leaves = []


class Leaf(object):
    def __init__(self, center=[10, 10], speed=[1, 1]):
        self.speed = speed
        self.angle = 0
        self.center = center

        self.img_src = pygame.image.load("leaf.png")
        self.rect_src = self.img_src.get_rect()
        self.img = self.img_src
        self.rect = self.img.get_rect()

        # 移动到初始位置
        self.rect_src = self.rect_src.move(center[0], center[1])
        self.rect = self.rect.move(center[0], center[1])

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        self.rect_src = self.rect_src.move(self.speed[0], self.speed[1])
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
            if self.rect.right > WIDTH:
                self.rect_src.left = WIDTH - self.rect.width
            if self.rect.left < 0:
                self.rect_src.left = 0
        if self.rect.top > HEIGHT:
            self.rect_src.bottom = 0

    def draw(self):
        screen.blit(self.img, self.rect)
        # 辅助观察
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)
        # pygame.draw.rect(screen, (0, 255, 0), self.rect_src, 1)

    def rotate(self):
        self.img = pygame.transform.rotate(self.img_src, self.angle)
        # 维护图片原来的中心点位置
        self.rect = self.img.get_rect(center=self.rect_src.center)
        self.angle += random.randint(1, 5)
        if math.fabs(self.angle) == 360:
            self.angle = 0


def init():
    for i in range(0, 5):
        leaf = Leaf([random.randint(50, WIDTH - 50), random.randint(30, HEIGHT)],
                    [random.randint(1, 2), random.randint(1, 2)])
        leaf.move()
        leaves.append(leaf)


clock = pygame.time.Clock()
init()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 根据第1片叶子的运动情况，随机切换背景色
    screen.fill(BACKGROUND_COLOR)

    # 将旋转后的图象，渲染到新矩形里
    for item in leaves:
        item.rotate()
        item.move()
        item.draw()

    # 正式渲染
    pygame.display.update()
    # 控制帧数<=100
    clock.tick(100)
