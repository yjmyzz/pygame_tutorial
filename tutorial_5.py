import os
from player import *
from bullet import *

WIN_WIDTH, WIN_HEIGHT = 600, 500

pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # 画布窗口的大小
pygame.display.set_caption("first game")  # 窗口标题
img_base_path = os.getcwd() + '/img/'
bg = pygame.image.load(img_base_path + 'bg.jpg')

clock = pygame.time.Clock()


def redraw_game_window():
    win.blit(bg, (0, 0))
    man.draw(win)
    for b in bullets:
        b.draw(win)
    pygame.display.update()


# main
man = Player(200, 410, 64, 64, img_base_path)
run = True
bullets = []
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if WIN_WIDTH > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            # 子弹不足5个时，自动填充
            bullets.append(Bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), facing, img_base_path))

    if keys[pygame.K_LEFT] and man.x > 0:
        man.x -= man.speed
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < win.get_size()[0] - man.width:
        man.x += man.speed
        man.left = False
        man.right = True
    else:
        man.walkCount = 0

    # 方向箭头响应
    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.t >= -10:
            a = 1  # 前半段减速上跳
            if man.t < 0:
                a = -1  # 后半段加速下落
            man.y -= 0.5 * a * (man.t ** 2)  # 匀加速直线运动的位移公式

            man.t -= 1
        else:
            man.isJump = False
            man.t = 10

    redraw_game_window()

pygame.quit()
