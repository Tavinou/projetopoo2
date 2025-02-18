from classes import Bola
import pygame
from random import randint
def mudarcor():
        return (randint(0,255),randint(0,255),randint(0,255))
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
#listabolas = []
#for i in range(0,2):
    #listabolas.append(Bola(randint(40,770),randint(40,560),30,mudarcor(),5,5,tela))

bola = Bola(250, 300, 20, (255, 255, 0), 5, 5, tela)
bola1 = Bola(80, 200, 20, (255, 255, 0), 5, 5, tela)
bola2 = Bola(50,50, 20,(255, 255, 0), 5, 5, tela)
bola3 = Bola(159,50, 20,(255, 255, 0), 5, 5, tela)
rodando = True
while rodando:
    tela.fill((0, 0, 0))  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    bola.mover()
    bola1.mover()
    bola2.mover()
    bola3.mover()
    bola.verifica_colisao(bola1)
    bola.verifica_colisao(bola2)
    bola.verifica_colisao(bola3)
    bola1.verifica_colisao(bola3)
    bola1.verifica_colisao(bola2)
    bola2.verifica_colisao(bola3)
    bola.desenhar()
    bola1.desenhar()
    bola2.desenhar()
    bola3.desenhar()
    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()