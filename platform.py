import pygame as pg

class Platform(pg.sprite.Sprite):
    def __init__(self, rect_coords):
        x, y, width, height = rect_coords
        print(width, height)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([width, height])
        self.image.fill([0, 126, 0])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y