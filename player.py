import pygame


# 主角
class Player(object):

    def __init__(self, x, y, width, height, img_base_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.left = False
        self.right = True
        self.isJump = False
        self.walkCount = 0
        self.t = 10
        self.speed = 5
        # 生命值
        self.life = 10
        self.char = pygame.image.load(img_base_path + 'standing.png')
        self.walkRight = [pygame.image.load(img_base_path + 'actor/R1.png'),
                          pygame.image.load(img_base_path + 'actor/R2.png'),
                          pygame.image.load(img_base_path + 'actor/R3.png'),
                          pygame.image.load(img_base_path + 'actor/R4.png'),
                          pygame.image.load(img_base_path + 'actor/R5.png'),
                          pygame.image.load(img_base_path + 'actor/R6.png'),
                          pygame.image.load(img_base_path + 'actor/R7.png'),
                          pygame.image.load(img_base_path + 'actor/R8.png'),
                          pygame.image.load(img_base_path + 'actor/R9.png')]

        self.walkLeft = [pygame.image.load(img_base_path + 'actor/L1.png'),
                         pygame.image.load(img_base_path + 'actor/L2.png'),
                         pygame.image.load(img_base_path + 'actor/L3.png'),
                         pygame.image.load(img_base_path + 'actor/L4.png'),
                         pygame.image.load(img_base_path + 'actor/L5.png'),
                         pygame.image.load(img_base_path + 'actor/L6.png'),
                         pygame.image.load(img_base_path + 'actor/L7.png'),
                         pygame.image.load(img_base_path + 'actor/L8.png'),
                         pygame.image.load(img_base_path + 'actor/L9.png')]
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount >= 9:
            self.walkCount = 0

        if self.left:
            win.blit(self.walkLeft[self.walkCount % 9], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount % 9], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.char, (self.x, self.y))
        self.hit_box = (self.x + 17, self.y + 11, 29, 52)
        # 血条(头顶的绿色背景矩形）
        pygame.draw.rect(win, (0, 128, 0), (self.hit_box[0], self.hit_box[1] - 10, 40, 8))
        # 血条(头顶的红色背景矩形，即：消耗的血）
        pygame.draw.rect(win, (255, 0, 0),
                         (self.hit_box[0] + self.life * 4, self.hit_box[1] - 10, 40 - self.life * 4, 8))
