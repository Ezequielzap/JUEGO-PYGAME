import random
import pygame







#ESTADO DE JUEGO INICIO
def mostrar_pantalla_inicio(pantalla,imagen_inicio,fuente,COLOR_NEGRO):
    pantalla.blit(imagen_inicio,(0,0))
    texto = fuente.render("¡haga Clic para JUGAR!",True,COLOR_NEGRO)
    pantalla.blit(texto,(235,600))


#ESTADO DE JUEGO MENU
def mostrar_menu(pantalla,imagen_inicio,imagen_jugar,imagen_puntaje,imagen_salir):
    pantalla.blit(imagen_inicio,(0,0))
    pantalla.blit(imagen_jugar,(232,408))
    pantalla.blit(imagen_puntaje,(232,499))
    pantalla.blit(imagen_salir,(232,590))


#ESTADO DE JUEGO NOMBRE
def mostrar_ingresar_nombre(pantalla,imagen_nombre,imagen_continuar,ingreso,COLOR_NEGRO,ingreso_rect,font_input,imagen_atras):
    pantalla.blit(imagen_nombre,(0,0))
    pantalla.blit(imagen_continuar,(253,408))
    font_input_surface = font_input.render(ingreso,True,COLOR_NEGRO)
    pantalla.blit(font_input_surface,(ingreso_rect.x + 15 , ingreso_rect.y + 6 ))
    pantalla.blit(imagen_atras,(0,20))




def mostrar_tablero(pantalla,imagen_fondo,imagen_neutral,imagen_especial):
    pantalla.blit(imagen_fondo,(0,0))
    pantalla.blit(imagen_neutral,(20,101))
    pantalla.blit(imagen_especial,(87,101))
    pantalla.blit(imagen_neutral,(154,101))
    pantalla.blit(imagen_neutral,(221,101))
    pantalla.blit(imagen_neutral,(288,101))
    pantalla.blit(imagen_especial,(355,101))
    pantalla.blit(imagen_neutral,(422,101))
    pantalla.blit(imagen_neutral,(489,101))
    pantalla.blit(imagen_neutral,(556,101))
    pantalla.blit(imagen_neutral,(623,101))
    pantalla.blit(imagen_neutral,(623,168))
    pantalla.blit(imagen_especial,(556,168))
    pantalla.blit(imagen_neutral,(489,168))
    pantalla.blit(imagen_neutral,(422,168))
    pantalla.blit(imagen_especial,(355,168))
    #inicio
    pantalla.blit(imagen_neutral,(288,168))
    pantalla.blit(imagen_neutral,(221,168))
    pantalla.blit(imagen_especial,(154,168))
    pantalla.blit(imagen_neutral,(87,168))
    pantalla.blit(imagen_neutral,(20,168))
    pantalla.blit(imagen_especial,(20,235))
    pantalla.blit(imagen_neutral,(87,235))
    pantalla.blit(imagen_neutral,(154,235))
    pantalla.blit(imagen_especial,(221,235))
    pantalla.blit(imagen_neutral,(288,235))
    pantalla.blit(imagen_neutral,(355,235))
    pantalla.blit(imagen_neutral,(422,235))
    pantalla.blit(imagen_especial,(489,235))
    pantalla.blit(imagen_neutral,(556,235))
    pantalla.blit(imagen_neutral,(623,235))
    #FINAL
    pantalla.blit(imagen_neutral,(623,302))


#PREGUNTAS
def mesclar_preguntas(lista:list)->list:
    random.shuffle(lista)
    return lista

def mostrar_opcines(pantalla,imagen_opcion_A,imagen_opcion_B,imagen_opcion_C,rect_opcion_A,rect_opcion_B,rect_opcion_C,pregunta,COLOR_NEGRO,fuente_opcion):
    pantalla.blit(imagen_opcion_A,(232,408))
    pantalla.blit(imagen_opcion_B,(232,499))
    pantalla.blit(imagen_opcion_C,(232,590))

    texto_a = fuente_opcion.render(pregunta["respuesta_a"], True, COLOR_NEGRO)
    pantalla.blit(texto_a, (rect_opcion_A.x + 60, rect_opcion_A.y + 30))

    texto_b = fuente_opcion.render(pregunta["respuesta_b"], True, COLOR_NEGRO)
    pantalla.blit(texto_b, (rect_opcion_B.x + 60, rect_opcion_B.y + 30))

    texto_c = fuente_opcion.render(pregunta["respuesta_c"], True, COLOR_NEGRO)
    pantalla.blit(texto_c, (rect_opcion_C.x + 60, rect_opcion_C.y + 30))


def mostrar_pregunta(pantalla,pregunta,COLOR_NEGRO,fuente_pregunta):
    texto_pregunta = fuente_pregunta.render(pregunta["pregunta"], True,COLOR_NEGRO)
    pantalla.blit(texto_pregunta, (10, 30))




def verificar_pregunta_correcta(pregunta,respuesta_usuario):
    retorno = False
    if respuesta_usuario == pregunta["respuesta_correcta"]:
        retorno = True
    return retorno



#MOVIMIENTO TABLERO
def retroceder_y_avanzar(respuesta:bool,posicion:int,tablero:list):
    mensaje = ""
    if respuesta:
        posicion += 1
        if posicion < len(tablero):
            posicion,mensaje = subir_escalera(posicion,tablero)

    else:
        posicion -= 1
        if posicion >= 0:
            posicion,mensaje = bajar_serpientes(posicion,tablero)

    return posicion,mensaje


#AVANZAR
def subir_escalera(posicion:int,tablero:list)->int:
    mensaje = ""
    while 0 <= posicion < len(tablero):
        if tablero[posicion] == 1:
            mensaje = "ESCALERA , avanzas 1 posicion"
            posicion += 1
        elif tablero[posicion] == 2:
            mensaje = "ESCALERA, avanzas 2 posiciones"
            posicion += 2
        elif tablero[posicion] == 3:
            mensaje = "ESCALERA, avanzas 3 posiciones"
            posicion += 3
        else:
            break
    return posicion,mensaje



#RETROSEDER
def bajar_serpientes(posicion:int,tablero:list)->int:
    mensaje = ""
    while 0 <= posicion < len(tablero):
        if tablero[posicion] == 1:
            mensaje = "SERPIENTE, retrocedes 1 posicion"
            posicion -= 1
        elif tablero[posicion] == 2:
            mensaje = "SERPIENTE, retrocedes 2 pociones"
            posicion -= 2
        elif tablero[posicion] == 3:
            mensaje = "SERPIENTE, retrocedes 3 posiciones"
            posicion -= 3
        else:
            break
    return posicion,mensaje


def debe_continuar_el_juego(posicion:int)->str:
    resultado = "si"
    if posicion == 30:
        resultado = "no"
    elif posicion == 0:
        resultado = "no"
    return resultado



def reiniciar_juego(posiciones_del_tablero,preguntas):
    
    indice_jugador = 15
    posicion_usuario = posiciones_del_tablero[indice_jugador]
    preguntas_aleatorias = mesclar_preguntas(preguntas)
    indice_pregunta = 0
    pregunta = preguntas_aleatorias[indice_pregunta]
    return indice_jugador, posicion_usuario, preguntas_aleatorias, indice_pregunta, pregunta



def mostrar_valores_tablero(pantalla,fuente_numeros,COLOR_NEGRO):
    numero1 = fuente_numeros.render("1",True,COLOR_NEGRO)
    numero2 = fuente_numeros.render("2",True,COLOR_NEGRO)
    numero3 = fuente_numeros.render("3",True,COLOR_NEGRO)

    pantalla.blit(numero1,(99,110))
    pantalla.blit(numero3,(365, 110))
    pantalla.blit(numero1,(565, 177))
    pantalla.blit(numero2,(365, 177))

    pantalla.blit(numero1,(156, 177))
    pantalla.blit(numero1,(29, 242))
    pantalla.blit(numero2,(232, 242))
    pantalla.blit(numero1,(505, 242))

#ESTADO JUEGO
def mostrar_juego(pantalla,imagen_fondo,imagen_neutral,imagen_especial,imagen_usuario,posicion_usuario,fuente_numeros,COLOR_NEGRO,pregunta,imagen_opcion_A,imagen_opcion_B,imagen_opcion_C,rect_opcion_A,rect_opcion_B,rect_opcion_C,fuente_tiempo,imagen_boton_tiempo,COLOR_BLANCO,segundos,fuente_mensaje_serpientes_escaleras,mensaje_evento,COLOR_ROJO,imagen_seguir_jugando,imagen_boton_no,fuente_opcion,fuente_pregunta):
    
    mostrar_tablero(pantalla,imagen_fondo,imagen_neutral,imagen_especial)
    pantalla.blit(imagen_usuario,posicion_usuario)
    mostrar_valores_tablero(pantalla,fuente_numeros,COLOR_NEGRO)
    mostrar_pregunta(pantalla,pregunta,COLOR_NEGRO,fuente_pregunta)
    mostrar_opcines(pantalla,imagen_opcion_A,imagen_opcion_B,imagen_opcion_C,rect_opcion_A,rect_opcion_B,rect_opcion_C,pregunta,COLOR_NEGRO,fuente_opcion)
    mostrar_segundos(pantalla,fuente_tiempo,imagen_boton_tiempo,COLOR_BLANCO,segundos)
    mostrar_mesaje_escalera_serpiente(pantalla,fuente_mensaje_serpientes_escaleras,mensaje_evento,COLOR_ROJO)
    mostrar_seguir_jugando(pantalla,imagen_seguir_jugando,imagen_boton_no)






def guardar_score(nombre:str,posicion:int):
    if nombre.strip() != "":
        with open("score.csv","a") as archivo:
            archivo.write(f"{nombre},{posicion}\n")


def leer_scores():
    lista = []
    try:
        with open("score.csv","r") as archivo:
            lista = archivo.readlines()
    except FileNotFoundError:
        pass
    
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):

            parte_i = lista[i].strip().split(",")
            parte_j = lista[j].strip().split(",")


            pos_i = int(parte_i[1])
            pos_j = int(parte_j[1])

            if pos_i < pos_j:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista


#ESTADO DE JUEGO MOSTRAR PUNTAJE
def mostrar_puntaje(pantalla,imagen_fondo,imagen_atras,fuente_titulo,fuente_puntaje,COLOR_NEGRO):
    pantalla.blit(imagen_fondo,(0,0))
    pantalla.blit(imagen_atras,(0,10))
    puntajes = leer_scores()
    y = 100

    titulo = fuente_titulo.render("PUNTAJES",True,COLOR_NEGRO)
    pantalla.blit(titulo,(250,40))

    for linea in puntajes:
        partes = linea.strip().split(",")
        if len(partes) == 2:
            nombre = partes[0].strip()
            puntaje = partes[1].strip()
            texto = fuente_puntaje.render(f"{nombre} - posicion alcanzada: {puntaje}",True,COLOR_NEGRO)            
            pantalla.blit(texto,(100,y))
        
            y += 40

    '''
    linea.strip().split(","): separa cada línea del archivo por coma → ["Ezequiel", "23"].
    nombre = partes[0], puntaje = partes[1]: toma los valores.
    Luego lo dibuja en la pantalla con blit.
    '''


def reiniciar_contador(timer_segundos):
    segundos = 20
    fin_tiempo = False
    pygame.time.set_timer(timer_segundos, 1000)
    return segundos,fin_tiempo



#ESTADO DE JUEG MOSTRAR REGLAS
def mostrar_reglas(pantalla,imagen_reglas,fuente,COLOR_NEGRO):
    pantalla.blit(imagen_reglas,(0,0))
    texto_continuar_reglas = fuente.render("Haga clic para comenzar",True,COLOR_NEGRO)
    pantalla.blit(texto_continuar_reglas,(235,600))


def mostrar_segundos(pantalla,fuente_tiempo,imagen_boton_tiempo,COLOR_BLANCO,segundos):
    segundos_texto = fuente_tiempo.render(str(segundos),True,COLOR_BLANCO)
    pantalla.blit(imagen_boton_tiempo,(620,629))
    pantalla.blit(segundos_texto,(630,630))

def mostrar_mesaje_escalera_serpiente(pantalla,fuente_mensaje_serpientes_escaleras,mensaje_evento,COLOR_ROJO):
    mensaje_texto = fuente_mensaje_serpientes_escaleras.render(mensaje_evento,True,COLOR_ROJO)
    pantalla.blit(mensaje_texto,(200,350))

def mostrar_seguir_jugando(pantalla,imagen_seguir_jugando,imagen_boton_no):
    pantalla.blit(imagen_seguir_jugando,(10,480))
    pantalla.blit(imagen_boton_no,(75,610))   





#ESTADO DE JUEGO FIN
def mostrar_mesaje_fin_juego(pantalla,imagen_juego_terminado,fuente_volver_menu,COLOR_NEGRO):
    pantalla.blit(imagen_juego_terminado,(0,0))
    texto_volver_menu = fuente_volver_menu.render("¡Hacé clic para volver al MENÚ PRINCIPAL!",True,COLOR_NEGRO)
    pantalla.blit(texto_volver_menu,(150,630))

