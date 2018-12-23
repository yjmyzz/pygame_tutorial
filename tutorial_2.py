import pygame

pygame.init()

win = pygame.display.set_mode((480, 480))  # 画布窗口的大小
pygame.display.set_caption("first game")  # 窗口标题

x, y = 85, 300  # 方块的起点
width, height = 30, 30  # 方块的宽，高
speed = 5  # 速度

run = True
isJump = False
t = 10

while run:
    # 防止cpu占用过高
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # 方向箭头响应
    if not (isJump):
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed

        if keys[pygame.K_RIGHT] and x < win.get_size()[0] - width:
            x += speed

        if keys[pygame.K_UP] and y > 0:
            y -= speed

        if keys[pygame.K_DOWN] and y < win.get_size()[1] - height:
            y += speed

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if t >= -10:
            a = 1  # 前半段减速上跳
            if t < 0:
                a = -1  # 后半段加速下落
            y -= 0.5 * a * (t ** 2)  # 匀加速直线运动的位移公式

            if y < 0:
                y = 0  # 防止跳出边界
            t -= 1
        else:
            isJump = False
            t = 10

    # 将每一帧的底色先填充成黑色
    win.fill((0, 0, 0))
    # 画方块
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # 更新画布
    pygame.display.update()

pygame.quit()
