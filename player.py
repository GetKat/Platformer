import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x = 0, y = 0):
        pg.sprite.Sprite.__init__(self)
        # player's rectangle
        self.image = pg.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # movement
        self.change_x = 0
        self.change_y = 0

        # level q o player ta
        self.level = None

    def update(self):
        # calcular gravidade
        self.calc_gravity()

        # atualiza a posicao
        self.rect.y += self.change_y
        self.rect.x += self.change_x

        self.change_x = 0

        # tenha certeza de q ele n passe do chao
        height = self.level.get_height()
        if self.rect.bottom >= height:
            self.change_y = 0
            self.rect.bottom = height

        # tenha certeza q ele n saia da tela
        width = self.level.get_width()
        if(self.rect.left < 0):
            self.rect.left = 0
        if(self.rect.right > width):
            self.rect.right = width

    # calcular o efeito da gravidade
    def calc_gravity(self):
        if(self.change_y == 0):
            self.change_y += 1
        else:
            self.change_y += .7
        
    # movimento
    def go_right(self):
        self.change_x += 10
    def go_left(self):
        self.change_x -= 10
    def stop(self):
        self.change_x = 0
    def jump(self):
        # precisa saber se o player esta no chao
        height = self.level.get_height()
        if(self.rect.bottom == height):
            self.change_y -= 10

