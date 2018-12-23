import pygame


class Enemy(object):

    def __init__(self, x, y, width, height, end, img_base_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.walkRight = [pygame.image.load(img_base_path + 'enemy/R1E.png'),
                          pygame.image.load(img_base_path + 'enemy/R2E.png'),
                          pygame.image.load(img_base_path + 'enemy/R3E.png'),
                          pygame.image.load(img_base_path + 'enemy/R4E.png'),
                          pygame.image.load(img_base_path + 'enemy/R5E.png'),
                          pygame.image.load(img_base_path + 'enemy/R6E.png'),
                          pygame.image.load(img_base_path + 'enemy/R7E.png'),
                          pygame.image.load(img_base_path + 'enemy/R8E.png'),
                          pygame.image.load(img_base_path + 'enemy/R9E.png'),
                          pygame.image.load(img_base_path + 'enemy/R10E.png'),
                          pygame.image.load(img_base_path + 'enemy/R11E.png')]

        self.walkLeft = [pygame.image.load(img_base_path + 'enemy/L1E.png'),
                         pygame.image.load(img_base_path + 'enemy/L2E.png'),
                         pygame.image.load(img_base_path + 'enemy/L3E.png'),
                         pygame.image.load(img_base_path + 'enemy/L4E.png'),
                         pygame.image.load(img_base_path + 'enemy/L5E.png'),
                         pygame.image.load(img_base_path + 'enemy/L6E.png'),
                         pygame.image.load(img_base_path + 'enemy/L7E.png'),
                         pygame.image.load(img_base_path + 'enemy/L8E.png'),
                         pygame.image.load(img_base_path + 'enemy/L9E.png'),
                         pygame.image.load(img_base_path + 'enemy/L10E.png'),
                         pygame.image.load(img_base_path + 'enemy/L11E.png')]
        self.hit_box = (self.x + 17, self.y + 2, 31, 57)
        #生命值
        self.life = 10

    def draw(self, win):
        if self.life > 0:
            self.move()
            if self.walkCount >= 11:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount % 11], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount % 11], (self.x, self.y))
                self.walkCount += 1
            self.hit_box = (self.x + 17, self.y + 2, 31, 57)
            # 血条
            pygame.draw.rect(win, (0, 128, 0), (self.hit_box[0], self.hit_box[1] - 12, 40, 8))
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hit_box[0] + self.life * 4, self.hit_box[1] - 12, 40 - self.life * 4, 8))

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
