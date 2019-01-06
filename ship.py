import pygame
import os

pygame.init()

win = pygame.display.set_mode((400, 400))  # 画布窗口的大小
pygame.display.set_caption("first game")  # 窗口标题
img_base_path = os.getcwd() + '/img/'


class Ship(object):

    def __init__(self, x, y, vx, vy, img_base_path):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.flame = False
        self.img_shutdown = pygame.image.load(img_base_path + 'ship.png')
        self.img_flame = pygame.image.load(img_base_path + 'ship_flame.png')
        self.img_size = self.img_flame.get_size()
        self.img_rotate = 0
        self.img_scale = 1

    def draw(self, win):
        win.blit(self.img_shutdown, (self.x, self.y))
        if self.flame:
            win.blit(self.img_flame, (self.x, self.y))

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def scale(self, scale):
        if scale == self.img_scale:
            pass
        else:
            scale_size = (int(self.img_size[0] * scale), int(self.img_size[1] * scale))
            self.img_shutdown = pygame.transform.smoothscale(self.img_shutdown, scale_size)
            self.img_flame = pygame.transform.smoothscale(self.img_flame, scale_size)
            self.img_scale = scale

    def rotate(self, angle):
        if angle == self.img_rotate:
            pass
        else:
            self.img_shutdown = pygame.transform.rotate(self.img_shutdown, angle)
            self.img_flame = pygame.transform.rotate(self.img_flame, angle)
            self.img_rotate = angle

    def start(self):
        self.flame = True

    def shutdown(self):
        self.flame = False


run = True
ship = Ship(100, 100, 1, 0, img_base_path)
while run:
    # 防止cpu占用过高
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 将每一帧的底色先填充成黑色
    win.fill((255, 255, 255))

    ship.draw(win)
    ship.move()
    ship.start()
    ship.scale(0.8)
    ship.rotate(90)

    # 更新画布
    pygame.display.update()

pygame.quit()
