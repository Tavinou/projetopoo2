from classes import Bola
import pygame
from random import randint
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
def mudarcor():
        return randint(0,255),randint(0,255),randint(0,255)
clock = pygame.time.Clock()
listabolas = [] #lista de bola
#gerador de bolas
for i in range(0,20): #n botar 250
    listabolas.append(Bola(randint(40,770),randint(40,560),randint(5,20),mudarcor(),randint(-5,5),randint(-5,5),tela))

rodando = True
while rodando:
    tela.fill((0, 0, 0))  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    #pygame.draw.circle(tela, (255, 0, 0), (400, 300), 90,2)
    #chama todos os metodos das bolas
    for b in listabolas: # percore a lista de bolas
        b.mover() #chama metedo mover
        b.desenhar() #ndesenha
        for i in listabolas: #percore dnv
            if b==i: #se for o mesmo objeto n faz nd
                None
            else: # diferente passa o objeto para verificar a colisao
                 b.verifica_colisao(i)
    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()