import pygame as pg

class Racket():
    """
    raqueta que golpea la pelota y la hace rebotar
    """
    def __init__(self, path_file, width, height):

        # Dimension del ancho y alto de la pantalla
        self.SCR_WIDTH = width
        self.SCR_HEIGHT = height

        self.image = pg.image.load(path_file).convert_alpha() # Imagen cargada

        # Dimensiones de la Raqueta
        self.width, self.height = self.image.get_size()

        # Posicion de la paleta
        self.x = 0
        self.y = (self.SCR_HEIGHT/2) - (self.height/2)

        # Direccion de movimiento de la raqueta
        self.dir_y = 0

    def move(self):
        """
        mover la raqueta y limitar que no salga fuera del rango de la visibilidad de la pantalla
        """
        self.y += self.dir_y

        if self.y <= 0:
            self.y = 0
        if self.y + self.height >= self.SCR_HEIGHT:
            self.y = self.SCR_HEIGHT - self.height
        
        
    def hit(self, ball):
        """
        golpear la pelota sólo cuando cumpla los requisitos correctos (mostrados debajo)
        """
        if (ball.x < (self.x+self.width)
            and ball.x > self.x 
            and ball.y < (self.y+self.height)
            and ball.y + ball.height > self.y
            ):

            ball.dir_x = -ball.dir_x
            ball.x = self.x + self.width

          
