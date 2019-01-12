import os
import pygame

pygame.init()

clock = pygame.time.Clock()

WIN_SIZE = 400, 400
win = pygame.display.set_mode(WIN_SIZE)  # 画布窗口的大小
pygame.display.set_caption("first game")  # 窗口标题
img_base_path = os.getcwd() + '/img/'


class Ship(object):

    def __init__(self, x, y, img_base_path):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
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
        # self.x += self.vx
        # self.y += self.vy
        rect = self.img_shutdown.get_rect()
        rect.move(self.vx, self.vy)

    def scale(self, scale):
        if scale == self.img_scale:
            pass
        else:
            scale_size = (int(self.img_size[0] * scale), int(self.img_size[1] * scale))
            self.img_shutdown = pygame.transform.smoothscale(self.img_shutdown, scale_size)
            self.img_flame = pygame.transform.smoothscale(self.img_flame, scale_size)
            self.img_scale = scale

    def rotate(self, angle):
        # if angle == self.img_rotate:
        #     pass
        # else:
        # origin_pos = self.x, self.y
        self.img_shutdown = pygame.transform.rotate(self.img_shutdown, angle)
        self.img_flame = pygame.transform.rotate(self.img_flame, angle)
        self.img_rotate = angle
        # self.x = origin_pos[0]
        # self.y = origin_pos[1]

    def start(self):
        self.flame = True

    def shutdown(self):
        self.flame = False


ship = Ship(WIN_SIZE[0] / 2, WIN_SIZE[1] / 2, img_base_path)
# ship.scale(0.5)
rotate = 0
ship.vx = 1
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rotate += 1
            ship.rotate(rotate)
        elif keys[pygame.K_RIGHT]:
            rotate -= 1
            ship.rotate(rotate)
        elif keys[pygame.K_UP]:
            ship.vy = -1
            ship.start()
        elif keys[pygame.K_DOWN]:
            ship.vy = 0
            ship.shutdown()

    # 将每一帧的底色先填充成黑色
    win.fill((255, 255, 255))

    ship.draw(win)
    ship.move()

    # ship.rotate(90)
    # print(ship.img_shutdown.get_rect())

    # 更新画布
    pygame.display.update()
