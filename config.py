from random import randint
import pygame
from barra import Barra
from bola import Bola
import sys
import math
bola = int(sys.argv[1]) #pega o input do script q le o barrabola.txt
barras = int(sys.argv[2]) #pega o input do script q le o barrabola.txt
gera = bool(sys.argv[3])#pega o input do script q le o barrabola.txt
largura, altura = 1080, 600#defina altura e largura
tela = pygame.display.set_mode((largura, altura)) 
clock = pygame.time.Clock()
listabolas = [] #lista de bola
listacor = [(0, 255, 0),(255, 255, 0),(255, 0, 255),(0, 255, 255)]
#gerador de bolas
def mudarcor():
    return randint(0,255),randint(0,255),randint(0,255) #cria as cor random
def ccw(A, B, C): #calcular sentido
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def segmentos_cruzam(A, B, C, D): #verificar se se cruzam/se tocam
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
alt = altura-100
lar = largura-100
def gerabolas(): #funcao que gera as balas passa o um numero mais altura/largura - 50 para definir aonde a bola comeca, e a velocidade x e y inicias
    for i in range(0,bola):
        listabolas.append(Bola(randint(40,lar),randint(20,alt),20,mudarcor(),randint(-5,5),randint(-5,5),tela,largura,altura))
gerabolas() #gerra as barras
def gerar_barras(qtd, largura_tela, altura_tela, barras_existentes=None, max_tentativas=1000):
    barras = barras_existentes if barras_existentes is not None else []

    cont = 0
    tentativas = 0

    while cont < qtd and tentativas < max_tentativas:
        tentativas += 1
        
        x1 = randint(0, largura_tela)
        y1 = randint(0, altura_tela)
        
        comprimento = randint(100, 250)  # tamanho legal da barra
        angulo = randint(-70, 70) * (math.pi / 180)  # ângulo aleatório (radianos)
        
        x2 = int(x1 + comprimento * math.cos(angulo))
        y2 = int(y1 + comprimento * math.sin(angulo))
        
        # Ajusta pra ficar dentro da tela
        x2 = max(0, min(largura_tela, x2))
        y2 = max(0, min(altura_tela, y2))
        
        nova_barra = (x1, y1), (x2, y2)
        
        # Verifica se cruza com alguma barra existente
        cruzou = False
        for barra in barras:
            if segmentos_cruzam(nova_barra[0], nova_barra[1], barra.x1y1, barra.x2y2):
                cruzou = True
                break
        
        if not cruzou:
            barras.append(Barra(tela, listacor[randint(0,3)], nova_barra[0], nova_barra[1], 15))
            cont += 1
    
    if tentativas >= max_tentativas:
        pass
    
    return barras
listabarras = gerar_barras(barras,largura,altura)
listaclone = [] # crio um clone
for i in listabarras:
    x1x2 = [i.x1y1[0],i.x1y1[1] + altura] #crio um clone fora da tela para o loop funciionar
    x2y2 = [i.x2y2[0],i.x2y2[1] + altura] #crio um clone fora da tela para o loop funcionar
    b =  Barra(tela,i.cor, x1x2, x2y2, 10) #crio onj
    listaclone.append(b) #add
listabarras+=listaclone #so na lista barra para na fazer mais um for no main
def reset(barra): #ve se inicia o loop
    if barra.x1y1[1]<0 and barra.x2y2[1]<0:
        barra.x1y1[1]+=altura* 2 #joga para baixo fazendo o loop funcioar
        barra.x2y2[1]+=altura *2#joga para baixo
def matarbola(bola): #elimino se enconstar no 0
    if bola.y -bola.raio <=0:
        listabolas.remove(bola)

rodando = True