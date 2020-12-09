import pygame as pg
from pygame.locals import QUIT

# Constantes para la inicialización de la superficie de dibujo
WIDTH = 800  # Ancho de la ventana
HEIGHT = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
WHITE = (255, 255, 255)  # Color del fondo de la ventana (RGB)


def main():
    # Inicialización de pg
    pg.init()

    # Inicialización de la superficie de dibujo (display surface)
    ventana = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Pong Game")

    # Bucle principal
    jugando = True
    while jugando:
        ventana.fill(WHITE)

        for event in pg.event.get():
            if event.type == QUIT:
                jugando = False

        pg.display.flip()
        pg.time.Clock().tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
