
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
        self.velocidade_y += 0.5 #aplica gravidade para fazer uma parabola
        self.y += self.velocidade_y
        if self.x - self.raio <= 0 or self.x + self.raio >= 800:
            self.velocidade_x *= -1  # Rebate nas bordas horizontai
            self.mudarcor()
        if self.y - self.raio <= 0:
            self.velocidade_y *= -1  # Rebate no teto
            self.mudarcor()
        if self.y + self.raio>=600: #se bater no chao
            self.y=600 - self.raio #para bola n entra em baixo
            self.velocidade_y = -20 #reseta altura/pulo sem perder velocidade
            self.mudarcor()
    def verifica_colisao(self,outra_bola):
        distancia = math.sqrt((outra_bola.x - self.x) ** 2 + (outra_bola.y - self.y) ** 2)
        if distancia <= self.raio + outra_bola.raio:
            self.velocidade_x, outra_bola.velocidade_x = outra_bola.velocidade_x, self.velocidade_x
            self.velocidade_y, outra_bola.velocidade_y = outra_bola.velocidade_y, self.velocidade_y
            #troca de energia 
            self.mudarcor()
            outra_bola.mudarcor()
    def desenhar(self):
        pygame.draw.circle(self.tela,self.cor,(self.x,self.y),self.raio)




    
    

    