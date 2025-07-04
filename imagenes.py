import pygame

#
#inicio
imagen_inicio = pygame.image.load("INICIO.png")
imagen_inicio = pygame.transform.scale(imagen_inicio,(700,700))


#JUGAR

imagen_jugar = pygame.image.load("jugar.png")
imagen_jugar = pygame.transform.scale(imagen_jugar,(200,100))
rect_jugar = imagen_jugar.get_rect()
rect_jugar.x = 232
rect_jugar.y = 408


#PUNTAJE
imagen_puntaje = pygame.image.load("puntaje.png")
imagen_puntaje = pygame.transform.scale(imagen_puntaje,(200,100))
rect_puntaje = imagen_puntaje.get_rect()
rect_puntaje.x = 232
rect_puntaje.y = 499



#SALIR
imagen_salir = pygame.image.load("salir.png")
imagen_salir = pygame.transform.scale(imagen_salir,(200,100))
rect_salir = imagen_salir.get_rect()
rect_salir.x = 232
rect_salir.y = 590



#NOMBRE
imagen_nombre = pygame.image.load("ingrese-nombre.png")
imagen_nombre = pygame.transform.scale(imagen_nombre,(700,700))


#CONTINUAR
imagen_continuar = pygame.image.load("CONTINUAR.png")
imagen_continuar = pygame.transform.scale(imagen_continuar,(200,100))
rect_continuar = imagen_continuar.get_rect()
rect_continuar.x = 253
rect_continuar.y = 408


#FONDO 
imagen_fondo = pygame.image.load("FONDO DE JUEGO.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(700,700))


#ATRAS
imagen_atras = pygame.image.load("ATRAS.png")
imagen_atras = pygame.transform.scale(imagen_atras,(150,100))
rect_atras = imagen_atras.get_rect()
rect_atras.x = 0
rect_atras.y = 20




#OPCIONES
imagen_opcion_A = pygame.image.load("OPCION.png")
imagen_opcion_A = pygame.transform.scale(imagen_opcion_A,(300,100))
rect_opcion_A = imagen_opcion_A.get_rect()
rect_opcion_A.x = 232
rect_opcion_A.y = 408



imagen_opcion_B = pygame.image.load("OPCION.png")
imagen_opcion_B = pygame.transform.scale(imagen_opcion_B,(300,100))
rect_opcion_B = imagen_opcion_B.get_rect()
rect_opcion_B.x = 232
rect_opcion_B.y = 499


imagen_opcion_C = pygame.image.load("OPCION.png")
imagen_opcion_C = pygame.transform.scale(imagen_opcion_C,(300,100))
rect_opcion_C = imagen_opcion_C.get_rect()
rect_opcion_C.x = 232
rect_opcion_C.y = 590



#CUADRADO VERDE
imagen_neutral = pygame.image.load("escalera.png")
imagen_neutral = pygame.transform.scale(imagen_neutral,(60,60))

#CUADRADO AZUL
imagen_especial = pygame.image.load("neutral.png")
imagen_especial = pygame.transform.scale(imagen_especial,(60,60))



#BOTON DE TIEMPO
imagen_boton_tiempo = pygame.image.load("boton rojo.png")
imagen_boton_tiempo = pygame.transform.scale(imagen_boton_tiempo,(60,60))


#IMAGEN DE REGLA
imagen_reglas = pygame.image.load("REGLAS.png")
imagen_reglas = pygame.transform.scale(imagen_reglas,(700,700))



#SEGUIR JUGANDO
imagen_seguir_jugando = pygame.image.load("SEGUIR JUGANDO.png")
imagen_seguir_jugando = pygame.transform.scale(imagen_seguir_jugando,(200,200))


#BOTON DE NO
imagen_boton_no = pygame.image.load("BOTON DE NO.png")
imagen_boton_no = pygame.transform.scale(imagen_boton_no,(60,60))
rect_boton_no = imagen_boton_no.get_rect()
rect_boton_no.x = 75
rect_boton_no.y = 610


#JUEGO TERMINADO
imagen_juego_terminado = pygame.image.load("JUEGO TERMINADO.png")
imagen_juego_terminado = pygame.transform.scale(imagen_juego_terminado,(700,700))

#USUARIO
imagen_usuario = pygame.image.load("JUGADOR.png")
imagen_usuario = pygame.transform.scale(imagen_usuario,(50,50))
