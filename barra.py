import pygame
class Barra:
    def __init__(self,tela,cor, x1y1,x2y2,grosura):
        self.cor = cor
        self.x1y1 =x1y1
        self.x2y2 = x2y2 
        self.grosura = grosura
        self.tela = tela
        
    def desenhar(self):
        pygame.draw.line(self.tela,self.cor,self.x1y1,self.x2y2,self.grosura)