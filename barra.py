import pygame
class Barra:
    def __init__(self,tela,cor, x1y1,x2y2,grosura):
        self.cor = cor
        self.x1y1 =list(x1y1)
        self.x2y2 = list(x2y2)
        self.grosura = grosura
        self.tela = tela
        self.velocidade = 1
        
    def desenhar(self):
        pygame.draw.line(self.tela,self.cor,self.x1y1,self.x2y2,self.grosura)
    def mover(self):
        self.x1y1[1] -= self.velocidade
        self.x2y2[1] -= self.velocidade
    def __str__(self):
        return f"{self.cor};{self.x1y1};{self.x2y2};{self.grosura}"