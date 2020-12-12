import pygame as pg
from racket import Racket

class IA(Racket):
    """
    raqueta que intenta devolver la pelota como si fuera una ia, moviendose para buscar la pelota
    """
    def __init__(self,path_file, width, height):
        super().__init__(path_file, width, height)
        self.x = self.SCR_WIDTH - self.width
        self.y = (self.SCR_HEIGHT/2) - (self.height/2)

        self.dir_y = 0

    def move_ia(self, ball):
        # limitar el movimiento y no salga del mapa

        if self.y <= 0:
            self.y = 0
        if self.y + self.height >= self.SCR_HEIGHT:
            self.y = self.SCR_HEIGHT - self.height

        # Seguir a la pelota
        if self.y > ball.y:
            self.dir_y = -4
        elif self.y < ball.y:
            self.dir_y = 4
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def hit_ia(self, ball):
        if (
            ball.x + ball.width > self.x
            and ball.x < self.x + self.width
            and ball.y + ball.height > self.y
            and ball.y < self.y + self.height
        ):
            ball.dir_x = -ball.dir_x
            ball.x = self.x - ball.width
