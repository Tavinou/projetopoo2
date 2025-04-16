from config import *
pygame.init()
while rodando:
    tela.fill((255, 255,255))   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    ba.desenhar()
    #pygame.draw.circle(tela, (255, 0, 0), (400, 300), 90,2)
    #chama todos os metodos das bolas
    for b in listabolas: # percore a lista de bolas
        b.mover() #chama metedo mover
        b.colidir_barra(ba) #verifica se colidiu na barra
        b.desenhar() #ndesenha
        
        for i in listabolas: #percore dnv
            if b==i: #se for o mesmo objeto n faz nd
                None
            else: # diferente passa o objeto para verificar a colisao
                 b.verifica_colisao(i)

    pygame.display.flip()  
    clock.tick(60)  

pygame.quit()