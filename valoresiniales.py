import pygame
from funcionespygame import *
from tablero import*
from preguntas import*


#INGRESO DE NOMBRE

ingreso_rect = pygame.Rect(226,300,300,40)
escribiendo = False


#TIEMPO
segundos = 20
fin_tiempo = False
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000) # 1000 = 1 segundo

mensaje_evento = ""
indice_jugador = 15
posicion_usuario = posiciones_del_tablero[indice_jugador]
preguntas_aleatorias = mesclar_preguntas(preguntas)
indice_pregunta = 0
pregunta = preguntas_aleatorias[indice_pregunta]

