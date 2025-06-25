from config import *
from salvar import salvar
import time
pygame.init()
frames = 0
framos = 0
while rodando:
    tela.fill((255, 255,255))   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    for i in listabolas:
        matarbola(i)
    if len(listabolas) ==0:
        time.sleep(5)
        rodando = False
    #chama todos os metodos das bolas
    for b in listabolas: # percore a lista de bolas
        b.mover()
        for t in listabarras:
            b.colidir_barra(t)#chama metedo mover #verifica se colidiu na barra
        b.desenhar() #ndesenha
        
        for i in listabolas: #percore dnv
            if b==i: #se for o mesmo objeto n faz nd
                None
            else: # diferente passa o objeto para verificar a colisao
                 b.verifica_colisao(i)
    for i in listabarras:
        i.mover()
        i.desenhar()
        reset(i)
    for p in listabolas:
        if (p.y + p.raio)>=600:
          p.y = 600 - p.raio
          for barra in listabarras:
              barra.mover()
    
    frames += 1
    framos +=1 
    segundos = frames // 60
    print(segundos)
    """if segundos==15:
        frames=0
        gerabolas()"""
    
    pygame.display.flip()  
    clock.tick(60)
pygame.quit()
fim = framos//60
salvar(listabarras,bola,fim) 

