import pygame


# 子弹类
class Bullet(object):

    def __init__(self, x, y, direction, img_base_path):
        self.x = x
        self.y = y
        self.direction = direction
        self.vel = 8 * direction
        self.width = 24
        self.height = 6
        self.bullet_right = pygame.image.load(img_base_path + 'r_bullet.png')
        self.bullet_left = pygame.image.load(img_base_path + 'l_bullet.png')

    def draw(self, win):
        # 根据人物行进的方向，切换不同的子弹图片
        if self.direction == -1:
            win.blit(self.bullet_left, (self.x - 35, self.y))
        else:
            win.blit(self.bullet_right, (self.x + 10, self.y))
