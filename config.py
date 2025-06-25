from random import randint
import pygame
from barra import Barra
from bola import Bola
import math
with open("barrabola.txt","r") as f:
    bola = int(f.readline())
    barras = int(f.readline())
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
listabolas = [] #lista de bola
#gerador de bolas
def mudarcor():
    return randint(0,255),randint(0,255),randint(0,255)
cont = 0
def ccw(A, B, C): #calcular sentido
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def segmentos_cruzam(A, B, C, D): #verificar se se cruzam/se tocam
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
def gerabolas():
    for i in range(0,bola): 
        listabolas.append(Bola(randint(40,770),randint(-1,100),20,mudarcor(),randint(-5,5),randint(-5,5),tela))
gerabolas()
def gerar_barras(qtd, largura_tela, altura_tela, barras_existentes=None, max_tentativas=1000):
    barras = barras_existentes if barras_existentes is not None else []
    cont = 0
    tentativas = 0

    while cont < qtd and tentativas < max_tentativas:
        tentativas += 1
        
        x1 = randint(0, largura_tela)
        y1 = randint(0, altura_tela)
        
        comprimento = randint(50, 150)  # tamanho legal da barra
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
            barras.append(Barra(tela, (0, 0, 0), nova_barra[0], nova_barra[1], 10))
            cont += 1
    
    if tentativas >= max_tentativas:
        print("Limite de tentativas para gerar barras atingido.")
    
    return barras
listabarras = gerar_barras(barras,largura,altura)
listaclone = []
for i in listabarras:
    x1x2 = [i.x1y1[0],i.x1y1[1] + altura]
    x2y2 = [i.x2y2[0],i.x2y2[1] + altura]
    b =  Barra(tela, (0, 0, 0), x1x2, x2y2, 10)
    listaclone.append(b)
listabarras+=listaclone
def reset(barra):
    if barra.x1y1[1]<0 and barra.x2y2[1]<0:
        barra.x1y1[1]+=1200
        barra.x2y2[1]+=1200
def matarbola(bola):
    if bola.y -bola.raio <=0:
        listabolas.remove(bola)

rodando = True