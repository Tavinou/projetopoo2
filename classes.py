
import pygame
from random import randint
import math
class Bola:
    def __init__(self,x,y,raio,cor,velocidade_x,velocidade_y,tela):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.tela = tela
    def mudarcor(self):
        self.cor = (randint(0,255),randint(0,255),randint(0,255))
    def mover(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

        # Impede que a bola ultrapasse a tela
        if self.x - self.raio <= 0 or self.x + self.raio >= 800:
            self.velocidade_x *= -1  # Rebater nas bordas horizontai
            self.mudarcor()
        if self.y - self.raio <= 0 or self.y + self.raio >= 600:
            self.velocidade_y *= -1  # Rebater nas bordas verticais
            self.mudarcor()
    def verifica_colisao(self,outra_bola):
        distancia = math.sqrt((outra_bola.x - self.x) ** 2 + (outra_bola.y - self.y) ** 2)
        if distancia <= self.raio + outra_bola.raio:
            self.velocidade_x *= -1
            self.velocidade_y *= -1 
            outra_bola.velocidade_x*= -1
            outra_bola.velocidade_y *= -1
            self.mudarcor()
            outra_bola.mudarcor()
    def desenhar(self):
        pygame.draw.circle(self.tela,self.cor,(self.x,self.y),self.raio)




    
    

    