import pygame
from random import randint
import math

class Bola:
    def __init__(self, x, y, raio, cor, velocidade_x, velocidade_y, tela):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.tela = tela

    def mudarcor(self):
        self.cor = (randint(0, 255), randint(0, 255), randint(0, 255))

    def mover(self):
        self.x += self.velocidade_x
        self.velocidade_y += 0.99  # aplica gravidade para fazer uma parabola
        self.velocidade_x*=0.99  #aplica gravidade no x se nao a bola n para
        self.y += self.velocidade_y

        if self.x - self.raio <= 0 or self.x + self.raio >= 800: # n deixa passar pros lado
            if self.x - self.raio < 0:
                self.x = self.raio
            if self.x + self.raio >= 800:
                self.x = 800 - self.raio
            self.velocidade_x *= -0.99

      

        if self.y + self.raio > 600: # n dx passar dio chao
            self.y = 600 - self.raio
            self.velocidade_y *= -0.6
        if abs(self.velocidade_x) < 0.1: #zera velcoidade evitar flik
            self.velocidade_x = 0
        if abs(self.velocidade_y) < 0.1: #zera velcoidade evitar flik
            self.velocidade_y = 0


    def colidir_barra(self, barra):
        cx, cy = self.x, self.y #centro da bola
        x1, y1 = barra.x1y1 #p1 da barra
        x2, y2 = barra.x2y2 #p2 da barra

        dx = x2 - x1 #distancia do x
        dy = y2 - y1 #distancia do y
        comprimento = math.hypot(dx, dy) #calcular a distancia da barra
        if comprimento == 0: #for nulo faz nbd
            return
        dirx = dx / comprimento #direcao do x
        diry = dy / comprimento  # direcao do y

        px = cx - x1 #diferenca de x entre o centro da bola e o comeco de x
        py = cy - y1 #diferenca de y entre o centro da bola e o comeco de y 
 
        t = (px * dx + py * dy) / (comprimento ** 2) #produto escalar
        t = max(0, min(1, t)) # garante q ta entre 0 e 1

        projx = x1 + t * dx #x preojetado na linha
        projy = y1 + t * dy #y preojetado na linha
 
        dist = math.hypot(projx - cx, projy - cy) #distancia entre a bola e a linhas

        if dist <= self.raio + barra.grosura / 2:
            # "Desliza"
            vel_dot = self.velocidade_x * dirx + self.velocidade_y * diry #produto escalar
            self.velocidade_x = dirx * vel_dot##att a velocidade da bola na direcao x
            self.velocidade_y = diry * vel_dot #att a velocidade da bola na direcao y

            empurrao = self.raio + barra.grosura / 2 - dist #n entrar na barra
            if dist != 0: #evita divisao por 0
                normalx = (cx - projx) / dist #normal no eixo x
                normaly = (cy - projy) / dist #normal no eixo y
                self.x += normalx * empurrao #att a posicao no eixo x 
                self.y += normaly * empurrao #att a posicao no eixo x 

    def verifica_colisao(self, outra_bola):
        distancia = math.sqrt((outra_bola.x - self.x) ** 2 + (outra_bola.y - self.y) ** 2)
        if distancia <= self.raio + outra_bola.raio: #colidiu?
            over = self.raio + outra_bola.raio - distancia #soprepos? >0 = true
            if over<0.1:
                return
            desloqx = ((self.x - outra_bola.x) / distancia) * over
            desloqy = ((self.y - outra_bola.y) / distancia) * over
            self.x += desloqx / 2 #empurao necessario para separar
            self.y += desloqy / 2 #mpurao necessario para separar
            outra_bola.x -= desloqx / 2 #empurao necessario para separar
            outra_bola.y -= desloqy / 2 #empurao necessario para separar
            self.velocidade_x, outra_bola.velocidade_x = outra_bola.velocidade_x, self.velocidade_x #troca de energia
            self.velocidade_y, outra_bola.velocidade_y = outra_bola.velocidade_y, self.velocidade_y #troca d energia
            if abs(self.velocidade_x) < 0.1: #evitart flik
                self.velocidade_x = 0

            if abs(self.velocidade_y) < 0.1: #evitart flik
                self.velocidade_y = 0

            

    def desenhar(self):
        pygame.draw.circle(self.tela, self.cor, (int(self.x), int(self.y)), self.raio)
