import pygame
import sys
import random
import math

pygame.init()

SIZE = WIDTH, HEIGHT = 200, 400
BACKGROUND_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(SIZE)
leaves = []


class Leaf(object):
    def __init__(self, pos=[10, 10], speed=[1, 1]):
        self.imageSrc = pygame.image.load("leaf.png")
        self.rect = self.imageSrc.get_rect()
        self.image = self.imageSrc
        self.speed = speed
        self.angle = 0
        self.pos = pos
        self.rect = self.rect.move(pos[0], pos[1])

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        new_rect = self.image.get_rect()
        new_rect.left, new_rect.top = self.rect.left, self.rect.top
        if new_rect.left < 0 or new_rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
            if new_rect.right > WIDTH:
                self.rect.left = WIDTH - new_rect.width
            if new_rect.left < 0:
                self.rect.left = 0
        if new_rect.top < 0 or new_rect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]
            if new_rect.bottom > HEIGHT:
                self.rect.top = HEIGHT - new_rect.height

    def draw(self):
        screen.blit(self.image, self.rect)

    def rotate(self):
        self.image = pygame.transform.rotate(self.imageSrc, self.angle)
        self.angle += random.randint(1, 5)
        if math.fabs(self.angle) == 360:
            self.angle = 0


def init():
    for i in range(0, 3):
        leaf = Leaf([random.randint(50, WIDTH - 50), random.randint(30, HEIGHT - 200)],
                    [random.randint(1, 2), random.randint(1, 2)])
        leaf.move()
        leaves.append(leaf)


def to255(x):
    if x > 1:
        x = 1
    return int(255 * math.fabs(x))


clock = pygame.time.Clock()
init()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    first_rect = leaves[0].rect

    # 根据第1片叶子的运动情况，随机切换背景色
    color_r = to255(first_rect.top / HEIGHT)
    color_g = to255(first_rect.left / WIDTH)
    color_b = to255(math.fabs(first_rect.left) / (math.fabs(first_rect.top) + math.fabs(first_rect.left) + 1))
    # print(color_r, color_g, color_b)
    screen.fill((color_r, color_g, color_b))

    # 将旋转后的图象，渲染到新矩形里
    for item in leaves:
        item.rotate()
        item.move()
        item.draw()

    # 正式渲染
    pygame.display.update()
    # 控制帧数<=100
    clock.tick(100)
