import os
from bullet import *
from player import *
from enemy import *

WIN_WIDTH, WIN_HEIGHT = 500, 500
pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("first game")
img_base_path = os.getcwd() + '/img/'
bg = pygame.image.load(img_base_path + 'bg.jpg')

clock = pygame.time.Clock()


def redraw_game_window():
    win.blit(bg, (0, 0))

    you_win = font.render('YOU WIN! ', 1, (0, 0, 255))
    you_lost = font.render('YOU LOST! ', 1, (255, 0, 0))

    # 敌人消灭，结束
    if enemy.life <= 0:
        win.blit(you_win, (200, 230))
        pygame.display.update()
        return

    # 主角被打死，结束
    if man.life <= 0:
        win.blit(you_lost, (200, 230))
        pygame.display.update()
        return

    # 主角的生命值
    life_text = font.render('Life: ' + str(man.life), 1, (0, 0, 0))
    win.blit(life_text, (20, 10))

    # 显示击中后的得分
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (370, 10))
    man.draw(win)
    enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


def collision_check(a, b):
    temp1 = (b.x <= a.x + a.width <= b.x + b.width)
    temp2 = (b.y <= a.y + a.height <= b.y + b.height)
    return temp1 and temp2


# main
font = pygame.font.SysFont('comicsans', 30, True)
man = Player(200, 410, 64, 64, img_base_path)
enemy = Enemy(100, 414, 64, 64, 400, img_base_path)
run = True
score = 0
bullets = []
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 如果被敌人打到了，主角生命值-1
    if collision_check(man, enemy) or collision_check(enemy, man):
        man.life -= 1
        # 自动跳跃，防止血降得太快
        man.isJump = True

    for b in bullets:
        # 碰撞检测
        if collision_check(b, enemy) or collision_check(enemy, b):
            score += 1
            enemy.life -= 1
            bullets.pop(bullets.index(b))

        if WIN_WIDTH > b.x > 0:
            b.x += b.vel
        else:
            bullets.pop(bullets.index(b))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            direction = -1
        else:
            direction = 1

        if len(bullets) < 5:
            bullets.append(Bullet(man.x + man.width // 2, man.y + man.height // 2, direction, img_base_path))

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

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.t >= -10:
            a = 1
            if man.t < 0:
                a = -1
            man.y -= 0.5 * a * (man.t ** 2)

            man.t -= 1
        else:
            man.isJump = False
            man.t = 10

    redraw_game_window()

pygame.quit()
