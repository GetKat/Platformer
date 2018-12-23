import pygame as pg

from platform import Platform

class Level():
    def __init__(self, player, width, height):
        self.player = player
        self.platform_sprites = pg.sprite.Group()

        # saving width and hight
        self.width = width
        self.height = height

        # plataformas no level
        platforms = [
            [40, height - 40, 100, 20],
            [60, height - 80, 100, 20]
        ]

        # adiciona as plataformas da lista acima
        for platform in platforms:
            new_plat = Platform(platform)
            self.platform_sprites.add(new_plat)


    # atualiza tudo no level
    def update(self):
        self.platform_sprites.update()
        self.player.update()

    # desenha na tela
    def draw(self, screen):
        screen.fill([126, 126, 126])
        self.platform_sprites.draw(screen)

    # pegar coordenadas
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width