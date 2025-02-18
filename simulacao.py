import classes
import pygame

pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

bola = classes.Bola(250, 300, 30, (255,255,255), 5, 0, tela)
rodando = True
while rodando:
    tela.fill((0, 0, 0))  

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    bola.mover()  
    bola.desenhar()

    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()