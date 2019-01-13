import math

import pygame


class Ship(object):
    def __init__(self, img_base_path, img_ship, img_flame_ship):
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

        self.img_src = pygame.image.load(img_base_path + img_ship)
        self.img_flame_src = pygame.image.load(img_base_path + img_flame_ship)

        self.img = self.img_src
        self.rect = self.img_src.get_rect()

        self.img_new = self.img
        self.rect_new = self.img_new.get_rect()

        screen_info = pygame.display.Info()
        self.rect = self.rect.move((screen_info.current_w - self.rect.width) * 0.5,
                                   (screen_info.current_h - self.rect.height) * 0.5)

    def draw(self, screen):
        screen.blit(self.img_new, self.rect_new)
        if self.show_rect:
            pygame.draw.rect(screen, (200, 200, 200), self.rect, 1)
            pygame.draw.rect(screen, (255, 0, 0), self.rect_new, 1)

    def move(self):
        self.rect = self.rect.move(self.vx, self.vy)
        self.rect_new = self.rect_new.move(self.vx, self.vy)
        screen_info = pygame.display.Info()
        # 向左飞出边界
        if self.rect_new.right < 0 and self.vx < 0:
            self.rect_new.left = screen_info.current_w
            self.rect.left = screen_info.current_w
        # 向右飞出边界
        if self.rect_new.left > screen_info.current_w and self.vx > 0:
            self.rect_new.right = 0
            self.rect.right = 0
        # 向下飞出边界
        if self.rect_new.top > screen_info.current_h and self.vy > 0:
            self.rect_new.bottom = 0
            self.rect.bottom = 0
        # 向上飞出边界
        if self.rect_new.bottom < 0 and self.vy < 0:
            self.rect_new.top = screen_info.current_h
            self.rect.top = screen_info.current_h

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
