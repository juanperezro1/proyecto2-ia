
import pygame
from pygame.locals import *
import os
import sys
import numpy as np

negro = (0,0,0) 
naranja = (156, 108, 43)
azul = (53, 80, 200)
marron = (46, 43, 24)
amarillo =(162, 185, 41)
rojo = (161, 67, 59)
morado = (107, 47, 140)
rosado = (152, 91, 133)
verde = (50, 103, 77)

pixel = 10
ancho = 640
alto = 640

desplazamiento_xy = 3

tamano_cuadros = 80

mapa = [[1, 2, 6, 7, 4, 5, 8, 3],
        [5, 1, 7, 8, 2, 4, 3, 6],
        [8, 7, 1, 5, 6, 3, 4, 2],
        [7, 6, 2, 1, 3, 8, 5, 4],
        [4, 5, 8, 3, 1, 2, 6, 7],
        [2, 4, 3, 6, 5, 1, 7, 8],
        [6, 3, 4, 2, 8, 7, 1, 5],
        [3, 8, 5, 4, 7, 6, 2, 1]]

matriz_fichas_negras = [[1, 2, 3, 4, 5, 6, 7, 8],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]


matriz_fichas_blancas = [[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 2, 3, 4, 5, 6, 7, 8]]

ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Kamisado") 

def movimiento_fichas():
    
    ficha_elegida = int(input("¿Cual ficha desea mover (1-8)?: "))

    print(ficha_elegida)
    print()
    print("Ingrese la nueva posicion ")
    pos_x = int(input("Posicion x: "))
    pos_y = int(input("Posicion y: "))

    posicion_ficha_marron = []
    posicion_ficha_verde = []
    posicion_ficha_rojo = []
    posicion_ficha_amarilla = []
    posicion_ficha_rosa = []
    posicion_ficha_morada = []
    posicion_ficha_azul = []
    posicion_ficha_naranja = []
    aux_pos_x_y = [0,0]

    for i in range(8):
        for j in range(8):

            if matriz_fichas_blancas[i][j] == 1:

                matriz_fichas_blancas[i][j] = 0

                posicion_ficha_marron.append(i)
                posicion_ficha_marron.append(j)
                print(posicion_ficha_marron)

                matriz_fichas_blancas[pos_x][pos_y] = 1
                
                aux_pos_x_y[0] = pos_x
                aux_pos_x_y[1] = pos_y

                actualizar_mapa(aux_pos_x_y,marron) 
            
            if matriz_fichas_blancas[i][j] == 2:

                
                matriz_fichas_blancas[i][j] = 0

                posicion_ficha_verde.append(i)
                posicion_ficha_verde.append(j)

                matriz_fichas_blancas[pos_x][pos_y] = 2

                aux_pos_x_y[0] = pos_x
                aux_pos_x_y[1] = pos_y
                actualizar_mapa(aux_pos_x_y,verde) 
            
            # if matriz_fichas_blancas[i][j] == 3:

            #     matriz_fichas_blancas[i][j] = 0
            #     posicion_ficha_rojo.append(i)
            #     posicion_ficha_rojo.append(j)

            #     matriz_fichas_blancas[pos_x][pos_y] = 3

            #     aux_pos_x_y[0] = pos_x
            #     aux_pos_x_y[1] = pos_y
            #     actualizar_mapa(aux_pos_x_y,rojo) 

            # if matriz_fichas_blancas[i][j] == 4:
            #     matriz_fichas_blancas[i][j] = 0
            #     posicion_ficha_amarilla.append(i)
            #     posicion_ficha_amarilla.append(j)

            #     matriz_fichas_blancas[pos_x][pos_y] = 4

            #     aux_pos_x_y[0] = pos_x
            #     aux_pos_x_y[1] = pos_y
            #     actualizar_mapa(aux_pos_x_y,amarillo) 
            
            # if matriz_fichas_blancas[i][j] == 5:
            #     matriz_fichas_blancas[i][j] = 0
            #     posicion_ficha_rosa.append(i)
            #     posicion_ficha_rosa.append(j)

            #     matriz_fichas_blancas[pos_x][pos_y] = 5

            #     aux_pos_x_y[0] = pos_x
            #     aux_pos_x_y[1] = pos_y
            #     actualizar_mapa(aux_pos_x_y,rosado) 
            
            # if matriz_fichas_blancas[i][j] == 6:
            #     matriz_fichas_blancas[i][j] = 0
            #     posicion_ficha_morada.append(i)
            #     posicion_ficha_morada.append(j)

            #     matriz_fichas_blancas[pos_x][pos_y] = 6

            #     aux_pos_x_y[0] = pos_x
            #     aux_pos_x_y[1] = pos_y
            #     actualizar_mapa(aux_pos_x_y,morado) 
            
            # if matriz_fichas_blancas[i][j] == 7:
            #     matriz_fichas_blancas[i][j] = 0
            #     posicion_ficha_azul.append(i)
            #     posicion_ficha_azul.append(j)

            #     matriz_fichas_blancas[pos_x][pos_y] = 7

            #     aux_pos_x_y[0] = pos_x
            #     aux_pos_x_y[1] = pos_y

            #     actualizar_mapa(aux_pos_x_y,azul) 
            
            # if matriz_fichas_blancas[i][j] == 8:
            #     matriz_fichas_blancas[i][j] = 0
            #     posicion_ficha_naranja.append(i)
            #     posicion_ficha_naranja.append(j)

            #     matriz_fichas_blancas[pos_x][pos_y] = 8

            #     aux_pos_x_y[0] = pos_x
            #     aux_pos_x_y[1] = pos_y

            #     actualizar_mapa(aux_pos_x_y,naranja) 

    if(ficha_elegida == 1):

        color_matriz = mapa[posicion_ficha_marron[0][posicion_ficha_marron[1]
        ficha_blanca_mo = ficha_blanca_marron(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_mo.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_marron,color_matriz)
        
    if(ficha_elegida == 2):

        color_matriz = mapa[posicion_ficha_verde[0]][posicion_ficha_verde[1]]
        ficha_blanca_ve = ficha_blanca_verde(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ve.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_verde,color_matriz)
        
    if(ficha_elegida == 3):
        color_matriz = mapa[posicion_ficha_rojo[0]][posicion_ficha_rojo[1]]
        ficha_blanca_ro = ficha_blanca_rojo(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ro.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_rojo,color_matriz)

    if(ficha_elegida == 4):
        color_matriz = mapa[posicion_ficha_amarilla[0]][posicion_ficha_amarilla[1]]
        ficha_blanca_ro = ficha_blanca_amarillo(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ro.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_amarilla,color_matriz)

    if(ficha_elegida == 5):
        color_matriz = mapa[posicion_ficha_rosa[0]][posicion_ficha_rosa[1]]
        ficha_blanca_ro = ficha_blanca_rosa(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ro.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_rosa,color_matriz)

    if(ficha_elegida == 6):
        color_matriz = mapa[posicion_ficha_morada[0]][posicion_ficha_morada[1]]
        ficha_blanca_ro = ficha_blanca_morada(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ro.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_morada,color_matriz)

    if(ficha_elegida == 7):
        color_matriz = mapa[posicion_ficha_azul[0]][posicion_ficha_azul[1]]
        ficha_blanca_ro = ficha_blanca_azul(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ro.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_azul,color_matriz)

    if(ficha_elegida == 8):
        color_matriz = mapa[posicion_ficha_naranja[0]][posicion_ficha_naranja[1]]
        ficha_blanca_ro = ficha_blanca_naranja(pos_x * tamano_cuadros, pos_y* tamano_cuadros)
        ficha_blanca_ro.dibujar_ficha(ventana)
        actualizar_mapa(posicion_ficha_naranja,color_matriz)
    
    
def actualizar_mapa(pos_ficha,color):
    
    if (color == 3):
        
        pygame.draw.rect(ventana,marron,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
        #pygame.display.update()

    if (color == 8):
        
        pygame.draw.rect(ventana,verde,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
    
    if (color == 5):
        
        pygame.draw.rect(ventana,rojo,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
    
    if (color == 4):
        
        pygame.draw.rect(ventana,amarillo,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
    
    if (color == 7):
        
        pygame.draw.rect(ventana,rosado,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
    
    if (color == 6):
        
        pygame.draw.rect(ventana,morado,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
   
    if (color == 2):
        
        pygame.draw.rect(ventana,azul,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))

    if (color == 1):
        
        pygame.draw.rect(ventana,naranja,pygame.Rect(pos_ficha[1] * tamano_cuadros, pos_ficha[0] *tamano_cuadros,tamano_cuadros,tamano_cuadros))
   
   
    pygame.display.update()
       
def construir_mapa(mapa):
    x = 0
    y = 0 
    for fila in range(8):
        for columna in range(8):
            if mapa[fila][columna] == 1:
                pygame.draw.rect(ventana,naranja,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 2:
                pygame.draw.rect(ventana,azul,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 3:
                pygame.draw.rect(ventana,marron,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 4:
                pygame.draw.rect(ventana,amarillo,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 5:
                pygame.draw.rect(ventana,rojo,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 6:
                pygame.draw.rect(ventana,morado,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 7:
                pygame.draw.rect(ventana,rosado,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            if mapa[fila][columna] == 8:
                pygame.draw.rect(ventana,verde,pygame.Rect(x,y,tamano_cuadros,tamano_cuadros))
            x += 80
        x = 0
        y += 80

def construir_fichas_blancas(matriz_fichas):

    for i in range(8):

        if matriz_fichas[i] == 8:
            ficha_blanca_n = ficha_blanca_naranja(i * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_n.dibujar_ficha(ventana)

        if matriz_fichas[i] == 7:
            ficha_blanca_a = ficha_blanca_azul(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_a.dibujar_ficha(ventana)
        
        if matriz_fichas[i] == 6:
            ficha_blanca_mo = ficha_blanca_morada(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_mo.dibujar_ficha(ventana)

        if matriz_fichas[i] == 5:
            ficha_blanca_mo = ficha_blanca_rosa(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_mo.dibujar_ficha(ventana)

        if matriz_fichas[i] == 4:
            ficha_blanca_a = ficha_blanca_amarillo(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_a.dibujar_ficha(ventana)

        if matriz_fichas[i] == 3:
            ficha_blanca_r = ficha_blanca_rojo(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_r.dibujar_ficha(ventana)

        if matriz_fichas[i] == 2:
            ficha_blanca_ve = ficha_blanca_verde(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_ve.dibujar_ficha(ventana)

        if matriz_fichas[i] == 1:
            ficha_blanca_mo = ficha_blanca_marron(7 * tamano_cuadros, i * tamano_cuadros)
            ficha_blanca_mo.dibujar_ficha(ventana)


def construir_fichas_negras(matriz_fichas):
    for i in range(8):
        if matriz_fichas[i] == 1:
            ficha_negra_n = ficha_negra_naranja(i * tamano_cuadros, i * tamano_cuadros)
            ficha_negra_n.dibujar_ficha(ventana)
        
        if matriz_fichas[i] == 2:
            ficha_negra_a = ficha_negra_azul(i, i * tamano_cuadros)
            ficha_negra_a.dibujar_ficha(ventana)
        
        if matriz_fichas[i] == 3:
            ficha_negra_m = ficha_negra_morada(i, i * tamano_cuadros)
            ficha_negra_m.dibujar_ficha(ventana)

        if matriz_fichas[i] == 4:
            ficha_negra_r = ficha_negra_rosa(i, i * tamano_cuadros)
            ficha_negra_r.dibujar_ficha(ventana)

        if matriz_fichas[i] == 5:
            ficha_negra_am = ficha_negra_amarillo(i, i * tamano_cuadros)
            ficha_negra_am.dibujar_ficha(ventana) 
        
        if matriz_fichas[i] == 6:
            ficha_negra_ro = ficha_negra_rojo(i - desplazamiento_xy, i * tamano_cuadros + desplazamiento_xy)
            ficha_negra_ro.dibujar_ficha(ventana)     
        
        if matriz_fichas[i] == 7:
            ficha_negra_v = ficha_negra_verde(i - desplazamiento_xy, i * tamano_cuadros + desplazamiento_xy)
            ficha_negra_v.dibujar_ficha(ventana)  

        if matriz_fichas[i] == 8:
            ficha_negra_ma = ficha_negra_marron(i - desplazamiento_xy, i * tamano_cuadros + desplazamiento_xy)
            ficha_negra_ma.dibujar_ficha(ventana)        

class ficha_negra_naranja(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/orangeTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_negra_azul(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/blueTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_negra_morada(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/purpleTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_negra_rosa(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/pinkTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_negra_amarillo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/yellowTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_negra_rojo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/redTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)
    
class ficha_negra_verde(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/greenTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_negra_marron(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/brownTower_black.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

# Fichas blancas

class ficha_blanca_naranja(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/orangeTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_blanca_azul(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/blueTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_blanca_morada(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/purpleTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_blanca_rosa(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/pinkTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_blanca_amarillo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/yellowTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_blanca_rojo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/redTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)
    
class ficha_blanca_verde(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/greenTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

class ficha_blanca_marron(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.imagenMuro = pygame.image.load("fichas/brownTower_white.png")
        self.rect = self.imagenMuro.get_rect()
        self.rect.top = posX
        self.rect.left = posY

    def dibujar_ficha(self, superficie):
        superficie.blit(self.imagenMuro, self.rect)

ventana.fill(negro)

construir_mapa(mapa)
construir_fichas_negras(matriz_fichas_negras[0])
construir_fichas_blancas(matriz_fichas_blancas[7])

pygame.display.update()

while True:
    

    movimiento_fichas()
    pygame.display.update()
    #pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
  







