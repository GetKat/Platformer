import pygame as pg
import sys

from player import Player
# from player2 import Player

# colors :D
black = [0, 0, 0]
white = [255, 255, 255]
gray = [128, 128, 128]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

# widht and height of main screen
WIDTH = 800
HEIGHT = 400

def main():
    # init
    pg.display.init()

    # screen setup
    screen = pg.display.set_mode([WIDTH, HEIGHT])
    pg.display.set_caption("Plataformando")

    # sprites
    sprites = pg.sprite.Group()
    
    # player object
    player = Player()
    player.level = screen
    sprites.add(player)

    # clock
    clock = pg.time.Clock()

    moving_left, moving_right = False, False

    # main loop
    while True:
        for event in pg.event.get():
            if(event.type == pg.QUIT):
                pg.quit()
                sys.exit("Flw")
            
            if(event.type == pg.KEYDOWN):
                if(event.key == pg.K_LEFT):
                    moving_left = True
                if(event.key == pg.K_RIGHT):
                    moving_right = True
                if(event.key == pg.K_SPACE or event.key == pg.K_UP):
                    player.jump()
            if(event.type == pg.KEYUP):
                if(event.key == pg.K_LEFT):
                    moving_left = False
                if(event.key == pg.K_RIGHT):
                    moving_right = False

        if(moving_left):
            player.go_left()
        if(moving_right):
            player.go_right()
        if(not moving_left and not moving_right):
            player.stop()

        screen.fill(gray)
        sprites.update()

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # current_level.draw(screen)
        sprites.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        clock.tick(30)
        pg.display.flip()
        
        
if(__name__ == "__main__"):
    main()