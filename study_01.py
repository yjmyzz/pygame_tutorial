import pygame
import sys

pygame.init()

SIZE = WIDTH, HEIGHT = 200, 400
BLACK = 0, 0, 0
RED = 255, 0, 0
SPEED = [1, 1]
angle = 1

screen = pygame.display.set_mode(SIZE)
originLeaf = pygame.image.load("leaf.png")
originRect = originLeaf.get_rect()

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 利用矩形对象的move方法，让rect移动
    originRect = originRect.move(SPEED[0], SPEED[1])
    # 注意：这里一定要用一个新变量newLeaf，保存旋转后的image对象
    newLeaf = pygame.transform.rotate(originLeaf, angle)
    angle += 1

    # 注意：这里要定义一个新rect对象，因为图象旋转后，其外切的矩形尺寸会变化
    newRect = newLeaf.get_rect()
    # 默认的newRect位置在(0,0)，要实现矩形外框跟随，必须赋值到新位置
    newRect.left, newRect.top = originRect.left, originRect.top

    # 左右边界反弹的处理
    if newRect.left <= 0 or newRect.right >= WIDTH:
        SPEED[0] = -SPEED[0]
        # 图片移动到接近右边界时(比如:right=198)，由于旋转的作用，可能导致叶子一下横过来了，
        # right突然会变成210，这样就算速度取反了，由于SPEED[0]=-1,需要10帧后，才能从视觉上真正看到反弹成功(即：210减到200，需要10次)
        if newRect.right > WIDTH:
            originRect.left = WIDTH - newRect.width

    # 上下边界反弹的处理
    if newRect.top <= 0 or newRect.bottom >= HEIGHT:
        SPEED[1] = -SPEED[1]
        # 类似右边界的校正处理，防止叶子接近下边界时，由于旋转，一下从横到竖，高度突然加大，导致越界
        if newRect.bottom > HEIGHT:
            originRect.top = HEIGHT - newRect.height

    # 默认背景为白色，所以每渲染一帧，要对背景重新填充，否则会有上一帧的残影
    screen.fill(BLACK)
    # 画新矩形
    pygame.draw.rect(screen, RED, newRect, 1)
    # 将旋转后的图象，渲染到新矩形里
    screen.blit(newLeaf, originRect)
    # 正式渲染
    pygame.display.update()
    # 控制帧数<=100
    clock.tick(100)
