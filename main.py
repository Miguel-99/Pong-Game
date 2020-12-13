# Credits: assets from DeathsbreedGames organization (http://deathsbreedgames.github.io/)

import pygame as pg
from pygame.locals import QUIT
from ball import Ball
from racket import Racket
from ia import IA
from scoreboard import Scoredboard

# Constantes para la inicialización de la superficie de dibujo
WIDTH = 800  # Ancho de la ventana
HEIGHT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
WHITE = (255, 255, 255)  # Color del fondo de la ventana (RGB)


def main():
    # Inicialización de pygame
    pg.init()

    # Inicialización de la superficie de dibujo (display surface)
    SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

    # Nombre de la ventana
    pg.display.set_caption("Pong Game")

    # Imagen de fondo
    background = pg.image.load("assets/bg_blue.png").convert_alpha()

    # objetos necesarios para el juego
    ball = Ball("assets/ball.png",WIDTH,HEIGHT)
    player1 = Racket("assets/racket1.png",WIDTH,HEIGHT)
    opponentIA = IA("assets/racket2.png",WIDTH,HEIGHT)
    scoreboard = Scoredboard()

    # Bucle principal
    run = True
    while run:
        pg.time.Clock().tick(FPS) # 60 actualizaciones de pantalla por segundo
        
        ball.move()
        ball.bounce(scoreboard)

        player1.hit(ball)
        player1.move()

        opponentIA.move_ia(ball)
        opponentIA.hit_ia(ball)
        
        scoreboard.update()

        SCREEN.blit(background, (0,0))
        SCREEN.blit(ball.image, (ball.x, ball.y))
        SCREEN.blit(player1.image, (player1.x, player1.y))
        SCREEN.blit(opponentIA.image, (opponentIA.x, opponentIA.y))
        SCREEN.blit(scoreboard.textRendered, (WIDTH/2 - scoreboard.font.size(scoreboard.text)[0]/2, 50))

        for event in pg.event.get():
            if event.type == QUIT:
                run = False
            
            # Deteccion de pulsacion de una tecla
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    player1.dir_y -= 5
                if event.key == pg.K_s:
                    player1.dir_y += 5
            
            # Deteccion de levantamiento de una tecla
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    player1.dir_y = 0
                if event.key == pg.K_s:
                    player1.dir_y = 0

        pg.display.flip()
        

    pg.quit()


if __name__ == "__main__":
    main()
