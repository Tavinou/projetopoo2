from classes import Bola
import pygame
from random import randint
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
#listabolas = []
#for i in range(0,2):
    #listabolas.append(Bola(randint(40,770),randint(40,560),30,mudarcor(),5,5,tela))
rodando = True
bola = Bola(250, 300, 20, (255, 255, 0), 5, 5, tela)
bola1 = Bola(704, 60, 20, (255, 255, 0), 5, 5, tela)
while rodando:
    tela.fill((0, 0, 0))  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    pygame.draw.circle(tela, (255, 0, 0), (400, 300), 90,2)
    bola.mover()
    bola1.mover()
    bola.verifica_colisao(bola1)
    bola1.desenhar()   
    bola.desenhar()
    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()