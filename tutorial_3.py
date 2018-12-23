import pygame
import os

pygame.init()

WIN_WIDTH, WIN_HEIGHT = 600, 450
FRAME_PER_SECONDS = 27  # 每秒最大帧数

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("first game")

img_base_path = os.getcwd() + '/img/'

# 向右走的图片数组
walkRight = [pygame.image.load(img_base_path + 'actor/R1.png'),
             pygame.image.load(img_base_path + 'actor/R2.png'),
             pygame.image.load(img_base_path + 'actor/R3.png'),
             pygame.image.load(img_base_path + 'actor/R4.png'),
             pygame.image.load(img_base_path + 'actor/R5.png'),
             pygame.image.load(img_base_path + 'actor/R6.png'),
             pygame.image.load(img_base_path + 'actor/R7.png'),
             pygame.image.load(img_base_path + 'actor/R8.png'),
             pygame.image.load(img_base_path + 'actor/R9.png')]

# 向左走的图片数组
walkLeft = [pygame.image.load(img_base_path + 'actor/L1.png'),
            pygame.image.load(img_base_path + 'actor/L2.png'),
            pygame.image.load(img_base_path + 'actor/L3.png'),
            pygame.image.load(img_base_path + 'actor/L4.png'),
            pygame.image.load(img_base_path + 'actor/L5.png'),
            pygame.image.load(img_base_path + 'actor/L6.png'),
            pygame.image.load(img_base_path + 'actor/L7.png'),
            pygame.image.load(img_base_path + 'actor/L8.png'),
            pygame.image.load(img_base_path + 'actor/L9.png')]

# 背景
bg = pygame.image.load(img_base_path + 'bg.jpg')

# 站立时的图片
char = pygame.image.load(img_base_path + 'standing.png')

x, y = 50, 350  # 起点
width, height = 64, 64  # 宽，高
speed = 5  # 速度

run = True
isJump, left, right = False, False, False
t = 10

walkCount = 0

clock = pygame.time.Clock()


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))

    if walkCount >= FRAME_PER_SECONDS:
        walkCount = 0

    if left:
        # 切换向左走的图片
        win.blit(walkLeft[walkCount % 9], (x, y))
        walkCount += 1
    elif right:
        # 切换向右走的图片
        win.blit(walkRight[walkCount % 9], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()


while run:
    clock.tick(FRAME_PER_SECONDS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < win.get_size()[0] - width:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if t >= -10:
            a = 1
            if t < 0:
                a = -1
            y -= 0.5 * a * (t ** 2)

            t -= 1
        else:
            isJump = False
            t = 10

    redrawGameWindow()

pygame.quit()
