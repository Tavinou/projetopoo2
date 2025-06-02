from random import randint
import pygame
from barra import Barra
from bola import Bola
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
for i in range(0,bola): 
    listabolas.append(Bola(randint(40,770),randint(-1,100),randint(5,20),mudarcor(),randint(-5,5),randint(-5,5),tela))
listabarras = []
cont = 0
def ccw(A, B, C): #calcular sentido
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def segmentos_cruzam(A, B, C, D): #verificar se se cruzam/se tocam
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
while cont<barras:
    x1, y1 = randint(0, 800), randint(0, 600)
    x2, y2 = randint(0, 800), randint(0, 600)
    nova_barra = (x1, y1), (x2, y2)

    cruzam = False
    for barra in listabarras:
        if segmentos_cruzam(nova_barra[0], nova_barra[1], barra.x1y1, barra.x2y2):
            cruzam = True
            break

    if not cruzam:
        listabarras.append(Barra(tela, (0, 0, 0), nova_barra[0], nova_barra[1], 10))
        cont += 1
rodando = True