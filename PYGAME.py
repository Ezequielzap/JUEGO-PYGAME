#

from  tablero import posiciones_del_tablero,valores_del_tablero
from funcionespygame import *
from preguntas import *
from constantes import*
from sonidos import*
from imagenes import*
import pygame
pygame.init()
from FUENTES import *
from valoresiniales import*



#PANTALLA
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

#defino el nombre
pygame.display.set_caption("SERPIENTES Y ESCALERAS")


estado_actual = "esperando_click"
flag_correr = True

sonido_fondo.play(-1)  #el (-1) indica que se reporduce en bucle infinito

while flag_correr:
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == timer_segundos:
            if estado_actual == "juego":
                if fin_tiempo == False:
                    segundos -= 1
                    if segundos == 0:
                        fin_tiempo = True                               #para que sea incorrecta
                        sonido_respuesta_incorrecta.play()
                        indice_jugador,mensaje_evento = retroceder_y_avanzar(False, indice_jugador, valores_del_tablero)
                        #actualizo la posicion visual del usuario
                        posicion_usuario = posiciones_del_tablero[indice_jugador]
                        


                        if debe_continuar_el_juego(indice_jugador) == "no":
                            guardar_score(ingreso,indice_jugador)
                            estado_actual = "fin"
                        else:
                            indice_pregunta += 1
                            
                            if indice_pregunta < len(preguntas_aleatorias):
                                pregunta = preguntas_aleatorias[indice_pregunta]
                                segundos,fin_tiempo = reiniciar_contador(timer_segundos)
                            else:
                                estado_actual = "fin"


        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicin_click_usuario = evento.pos
            if estado_actual == "esperando_click":
                estado_actual = "menu"

            elif estado_actual == "menu":

                if rect_jugar.collidepoint(posicin_click_usuario):
                    ingreso = ""
                    pygame.time.set_timer(timer_segundos,0) #Apago temporizador si venía de otra partida
                    indice_jugador, posicion_usuario, preguntas_aleatorias, indice_pregunta, pregunta = reiniciar_juego(posiciones_del_tablero,preguntas)
                    estado_actual = "nombre"


                elif rect_puntaje.collidepoint(posicin_click_usuario):
                    estado_actual = "mostrar_puntaje"

                elif rect_salir.collidepoint(posicin_click_usuario):
                    flag_correr = False
        
            elif estado_actual == "nombre":

                if ingreso_rect.collidepoint(posicin_click_usuario):
                    escribiendo = True

                elif rect_continuar.collidepoint(posicin_click_usuario):
                    estado_actual = "mostrar reglas"

                elif rect_atras.collidepoint(posicin_click_usuario):
                    estado_actual = "menu"
                    pygame.time.set_timer(timer_segundos,0)
            elif estado_actual == "mostrar reglas":
                estado_actual = "juego"
                segundos,fin_tiempo = reiniciar_contador(timer_segundos)


            elif estado_actual == "mostrar_puntaje":
                if rect_atras.collidepoint(posicin_click_usuario):
                    estado_actual = "menu"
                    pygame.time.set_timer(timer_segundos,0)

            elif estado_actual == "juego":
                respuesta_usuario = "" 
                
                if rect_opcion_A.collidepoint(posicin_click_usuario):
                    respuesta_usuario = "a"
                elif rect_opcion_B.collidepoint(posicin_click_usuario):
                    respuesta_usuario = "b"
                elif rect_opcion_C.collidepoint(posicin_click_usuario):
                    respuesta_usuario = "c"

                elif rect_boton_no.collidepoint(posicin_click_usuario):
                    guardar_score(ingreso,indice_jugador)
                    estado_actual = "fin"

                if respuesta_usuario == "a" or respuesta_usuario == "b" or respuesta_usuario == "c":

                    respuesta_correcta = verificar_pregunta_correcta(pregunta,respuesta_usuario)
                    #REPRODUSCO LOS SONIDOS
                    if respuesta_correcta:
                        sonido_respuesta_correcta.play()
                    else:
                        sonido_respuesta_incorrecta.play()
                    
                    indice_jugador,mensaje_evento = retroceder_y_avanzar(respuesta_correcta,indice_jugador,valores_del_tablero)
                    #actualizo la posicion visual del usuario
                    posicion_usuario = posiciones_del_tablero[indice_jugador]

            
                    if debe_continuar_el_juego(indice_jugador) == "no":
                        guardar_score(ingreso,indice_jugador)
                        estado_actual = "fin"
                        pygame.time.set_timer(timer_segundos,0)     #apago el timer si el jugador gana o pierde
                    else:
                        indice_pregunta += 1
                        if indice_pregunta < len(preguntas_aleatorias):
                            pregunta = preguntas_aleatorias[indice_pregunta]
                            segundos,fin_tiempo = reiniciar_contador(timer_segundos)

                        else:
                            guardar_score(ingreso,indice_jugador)
                            estado_actual = "fin"
                            pygame.time.set_timer(timer_segundos,0) 

            elif estado_actual == "fin":
                estado_actual = "menu"
                pygame.time.set_timer(timer_segundos,0)

        elif evento.type == pygame.KEYDOWN:
            if estado_actual == "nombre":
                if evento.key == pygame.K_RETURN:
                    estado_actual = "mostrar reglas"
                elif escribiendo:
                    if evento.key == pygame.K_BACKSPACE:
                        ingreso = ingreso[0:-1]
                    else:
                        ingreso += evento.unicode



    if estado_actual == "esperando_click":
        mostrar_pantalla_inicio(pantalla,imagen_inicio,fuente,COLOR_NEGRO)

    elif estado_actual == "menu":
        mostrar_menu(pantalla,imagen_inicio,imagen_jugar,imagen_puntaje,imagen_salir)

    elif estado_actual == "nombre":
        mostrar_ingresar_nombre(pantalla,imagen_nombre,imagen_continuar,ingreso,COLOR_NEGRO,ingreso_rect,font_input,imagen_atras)

    elif estado_actual == "mostrar_puntaje":
        mostrar_puntaje(pantalla,imagen_fondo,imagen_atras,fuente_titulo,fuente_puntaje,COLOR_NEGRO)

    elif estado_actual == "mostrar reglas":
        mostrar_reglas(pantalla,imagen_reglas,fuente,COLOR_NEGRO)

    elif estado_actual == "juego":
        mostrar_juego(pantalla,imagen_fondo,imagen_neutral,imagen_especial,imagen_usuario,posicion_usuario,fuente_numeros,COLOR_NEGRO,pregunta,imagen_opcion_A,imagen_opcion_B,imagen_opcion_C,rect_opcion_A,rect_opcion_B,rect_opcion_C,fuente_tiempo,imagen_boton_tiempo,COLOR_BLANCO,segundos,fuente_mensaje_serpientes_escaleras,mensaje_evento,COLOR_ROJO,imagen_seguir_jugando,imagen_boton_no,fuente_opcion,fuente_pregunta)

    elif estado_actual == "fin":
        mostrar_mesaje_fin_juego(pantalla,imagen_juego_terminado,fuente_volver_menu,COLOR_NEGRO)



    pygame.display.flip()
    #actualiza la pantalla
sonido_fondo.stop()
pygame.quit()


