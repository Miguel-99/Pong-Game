import pygame as pg

class Scoredboard():
    """
    Indica la puntuacion de los jugadores en la pantalla
    """
    def __init__(self):

        # Fuente del texto
        self.font = pg.font.Font(None, 60) 

        # Ambas puntuaciones comienzan de 0
        self.punct_leftPlayer = 0   
        self.punct_rightPlayer = 0

        # cadena de texto
        self.text = f"{self.punct_leftPlayer} - {self.punct_rightPlayer}" 
        

    def update(self): 

        #actualizar los valores de la puntuacion de los jugadores
        self.text = f"{self.punct_leftPlayer} - {self.punct_rightPlayer}"
        self.textRendered = self.font.render(self.text, False, (0,0,0))