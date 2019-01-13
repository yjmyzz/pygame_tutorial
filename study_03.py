import os
import sys

import pygame

pygame.init()

clock = pygame.time.Clock()

SIZE = WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode(SIZE)
img_base_path = os.getcwd() + '/img/'


class MyRect(object):
    def __init__(self, img_base_path):
        self.img_src = pygame.image.load(img_base_path + 'rect.png')
        self.rect_src = self.img_src.get_rect()
        self.img = self.img_src
        self.rect = self.img.get_rect()
        # 初始化时，先定位到舞台中央
        self.center = (WIDTH - self.rect_src.width) * 0.5, (HEIGHT - self.rect_src.height) * 0.5
        self.rect_src = self.rect_src.move(self.center[0], self.center[1])
        self.rect = self.rect.move(self.center[0], self.center[1])

    def draw(self, screen):
        screen.blit(self.img, self.rect)
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 1)
        pygame.draw.rect(screen, (0, 0, 255), self.rect_src, 1)

    def rotate(self, angle):
        self.img = pygame.transform.rotate(self.img_src, angle)
        # 将旋转后的图片，维持在原来的中心点
        self.rect = self.img.get_rect(center=self.rect_src.center)


my_rect = MyRect(img_base_path)
angle = 1

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 将每一帧的底色先填充成黑色
    screen.fill((230, 250, 230))

    # 辅助线
    pygame.draw.line(screen, (255, 0, 0), (0, 200), (400, 200), 1)
    pygame.draw.line(screen, (255, 0, 0), (200, 0), (200, 400), 1)

    my_rect.rotate(angle)
    my_rect.draw(screen)
    angle += 3

    # 更新画布
    pygame.display.update()
