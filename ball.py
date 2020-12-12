import pygame as pg
import random


class Ball():
    """
    Pelota que rebota en la pantalla, es golpeada por las raquetas y al sobrepasar el eje x en su 
    limite minimo y maximo anota un punto para un jugador, luego reaparece en el centro
    """
    def __init__(self, path_file, width, height):

        # Dimension del ancho y alto de la pantalla
        self.SCR_WIDTH = width
        self.SCR_HEIGHT = height

        self.image = pg.image.load(path_file).convert_alpha() # Imagen cargada

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

    def bounce(self, scoreboard):
        """
        cuando la pelota alcanza el limite de la pantalla, rebota o se resetea (desde el centro otra vez)
        cuando esto sucede, aumenta 1 punto en el scoreboard para el jugador que anotó
        """
        if self.y <= 0:
            self.dir_y = -self.dir_y
        
        if self.y+self.height >= self.SCR_HEIGHT:
            self.dir_y = -self.dir_y

        if self.x +self.width<= 0:
            scoreboard.punct_rightPlayer += 1
            self.reset()
            
        
        if self.x>= self.SCR_WIDTH:
            scoreboard.punct_leftPlayer += 1
            self.reset()
            
    def reset(self):
        """
        devuelve la pelota al centrode la pantalla
        """

        self.x = (self.SCR_WIDTH/2) - (self.width/2)
        self.y = (self.SCR_HEIGHT/2) - (self.height/2)

        self.dir_x = random.choice([-5, 5]) 
        self.dir_y = random.choice([-5, 5])


    