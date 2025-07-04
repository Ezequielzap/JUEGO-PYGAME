import pygame

pygame.mixer.init()

#MUSICA DE FONDO
sonido_fondo = pygame.mixer.Sound("sonido de menu.mp3")
volumen_fondo = 0.1
sonido_fondo.set_volume(volumen_fondo)



#RESPUESTA CORRECTA 
sonido_respuesta_correcta = pygame.mixer.Sound("sonido correcto.mp3")
volumen_correcto = 0.1
sonido_respuesta_correcta.set_volume(volumen_correcto)



#RESPUESTA INCORRECTA 
sonido_respuesta_incorrecta = pygame.mixer.Sound("sonido incorrecto.mp3")
volumen_incorrecto = 0.1
sonido_respuesta_incorrecta.set_volume(volumen_incorrecto)
