import pygame

pygame.init()

win = pygame.display.set_mode((320, 240))  # 画布窗口的大小
pygame.display.set_caption("first game")  # 窗口标题

x, y = 50, 50  # 方块的起点
width, height = 30, 30  # 方块的宽，高
speed = 5  # 速度

run = True
while run:
    # 防止cpu占用过高
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # 方向箭头响应
    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

    # 防止跑出边界
    if x > win.get_size()[0] - width:
        x = win.get_size()[0] - width

    if x < 0:
        x = 0

    if y > win.get_size()[1] - height:
        y = win.get_size()[1] - height

    if y < 0:
        y = 0

    # 将每一帧的底色先填充成黑色
    win.fill((0, 0, 0))
    # 画方块
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # 更新画布
    pygame.display.update()

pygame.quit()
