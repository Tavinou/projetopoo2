from random import randint
import pygame
from barra import Barra
from bola import Bola
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
listabolas = [] #lista de bola
#gerador de bolas
def mudarcor():
    return randint(0,255),randint(0,255),randint(0,255)
for i in range(0,50): #n botar 250
    listabolas.append(Bola(randint(40,770),randint(-1,100),randint(5,20),mudarcor(),randint(-5,5),randint(-5,5),tela))
ba =Barra(tela,(0,0,0),(200,400),(500,200),10) 
rodando = True