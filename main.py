from config import *
from salvar import salvar
import time
pygame.init()
frames = 0
framos = 0
conc = False
fonte = pygame.font.SysFont('Calibri', 30)
texto = fonte.render('Bola Ganhadora!!', True, (255, 255, 255))
while rodando:
    tela.fill((0,0,0))   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    for i in listabolas: #verifica se uma bola ta no teto
        matarbola(i)
    if len(listabolas) ==1: #verifica se alg ganhhou
        listabolas[0].x = largura//2
        listabolas[0].y = altura//2
        listabolas[0].raio = 20
        listabolas[0].desenhar()
        tela.blit(texto, ((largura//2)-100, (altura//2)+150))
        pygame.display.flip() 
        time.sleep(5)
        conc = True
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
        i.mover() #mova a barra
        reset(i) # ver se resetar
        i.desenhar() #desenhar
    for p in listabolas: #
        if (p.y + p.raio)>=altura: #se for maior ou = ta no chao move a barra para der efeito de queda
          p.y = altura - p.raio
          for barra in listabarras:
              barra.mover()
              barra.desenhar()
    
    segundos = frames // 60 #segundio
    if segundos==120 : #for 3 minuto encerra
        rodando = False
    if gera: #ver a cada 15seg gera bola ou n
        if framos//60==15:
            framos = 0
            gerabolas()
    frames+=1 #ver o tempo da simulacao
    framos+=1 #para gerar a cade 15s
    pygame.display.flip()  
    clock.tick(60)
pygame.quit()
salvar(listabarras,bola,segundos,conc) 

