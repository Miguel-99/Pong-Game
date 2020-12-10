import pygame as pg
import random

class Ball():
    def __init__(self, fichero_imagen, width, height):

        # Dimension del ancho y alto de la pantalla
        self.SCR_WIDTH = width
        self.SCR_HEIGHT = height

        self.sheet = pg.image.load("assets/ball.png").convert_alpha() # Imagen cargada
        self.image = self.sheet.subsurface(self.sheet.get_clip()) # dimension del recorte: ancho y alto
         
        # Dimensiones de la Pelota
        self.width, self.height = self.image.get_size()
        
        # Posición de la pelota
        self.x = (self.SCR_WIDTH/2) - (self.width/2)
        self.y = (self.SCR_HEIGHT/2) - (self.height/2)

        # Dirección de movimiento de la pelota
        self.dir_x = random.choice([-5, 5]) 
        self.dir_y = random.choice([-5, 5])

        # Cantidad de pelotas en juego
        self.inGameBalls = 1 

    def move(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def bounce(self):
        """
        when ball reaches the screen's limits, bounce or reset (start from the cencter again)
        """
        if self.y <= 0:
            self.dir_y = -self.dir_y
        
        if self.y+self.height >= self.SCR_HEIGHT:
            self.dir_y = -self.dir_y

        if self.x <= 0:
            self.reset()
        
        if self.x+self.width >= self.SCR_WIDTH:
            self.reset()
    def reset(self):

        self.x = (self.SCR_WIDTH/2) - (self.width/2)
        self.y = (self.SCR_HEIGHT/2) - (self.height/2)

        self.dir_x = random.choice([-5, 5]) 
        self.dir_y = random.choice([-5, 5])


    