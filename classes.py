import pygame
class Bola:
    def __init__(self,x,y,raio,cor,velocidade_x,velocidade_y,tela):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.tela = tela
    def mover(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

        # Impede que a bola ultrapasse a tela
        if self.x - self.raio <= 0 or self.x + self.raio >= 800:
            self.velocidade_x *= -1  # Rebater nas bordas horizontais
        if self.y - self.raio <= 0 or self.y + self.raio >= 600:
            self.velocidade_y *= -1  # Rebater nas bordas verticais
    

    def desenhar(self):
        pygame.draw.circle(self.tela,self.cor,(self.x,self.y),self.raio)
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()


    

    