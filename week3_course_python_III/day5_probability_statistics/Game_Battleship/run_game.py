
#Importamos librerias
import numpy as np 
import random
from time import sleep
from tqdm import tqdm

#importamos módulos propios
from Clases import *
import Constantes as cs
from time import sleep
from tqdm import tqdm
from Constantes import MENSAJES


def posicion_random(): #crea una posición en un tablero de 10 x 10 de fila-letra

    x = random.randint(1, 10)
    y = cs.LISTA_CARACTERES[random.randint(0, 9)]

    return (x, y)

#interpretamos las coordenadas introducidas por el jugador
def lee_input(jugador, posicion): 
    #se le pasa como parámetros un jugador y una posición. este método comprueba la validez del disparo,
    #no debe de haber disparado en esa misma posición y 
    # tiene que estar bien construido para que identifique una posición real del tablero

    resp = None

    try:
        if len(posicion) == 3:
            if int(posicion[0:2]) == 10 and posicion[2].upper() in cs.LISTA_CARACTERES:
                resp = (int(posicion[0:2]), posicion[2].upper())

        elif len(posicion) == 2:
            if int(posicion[0]) > 0 and int(posicion[0]) < 10 and posicion[1].upper() in cs.LISTA_CARACTERES:
                resp = (int(posicion[0]), posicion[1].upper())

        elif posicion == "0":

            resp = 0

        if resp in jugador.disparos:
            print("Ya has disparado en esta posicion")
            resp = None

        return resp
    except:
        return None

es_maquina = False

salir = False

#nuestros jugadores
#llamamos a la clase Jugador
jugador_1 = Jugador()

jugador_2 = Jugador()

#introducimos mensaje Bienvenida

print(MENSAJES["introduccion"])

sleep(0.5)

#introduciomos los símbolos a los que hacer referencia las marcas en el tablero

print("Los símbolos '~' hacen referncia al agua")

sleep(0.5)

print("El símbolo 'Ø' hace referencia a un disparo fallido")

sleep(0.5)

print("El símbolo 'X' hace referencia a un barco tocado")

sleep(0.5)

#introducimos las reglas del juego
print(MENSAJES["reglas"])

sleep(0.5)

print("           ARE YOU READY????....CARGANDO...\n ")
for i in tqdm(range(10)):
    sleep(0.5)

input("Presiona enter para continuar")

#instanciamos el juego

while jugador_1.vidas > 0 and jugador_2.vidas > 0 : #comprobamos que alguno de los dos aun tiene vidas
    
    if not es_maquina:
        jugador_1.imprimir_tablero()
        
        while True:
            print("Si deseas abandonar el juego sólo tienes que presionar = 0")
            posicion = str(input("Introduzca la coordenada a la que desea diparar: filas de 1 a 10 y columnas de A - J  \
                \nEjemplo: 1A ------->Intentelo aquí:  "))

            tupla_posicion = lee_input(jugador_1, posicion) #llamamos a la funcion que nos devuelve el imput con la coordenada ingresada por el jugador

            if tupla_posicion != None:

                break

            else:
                print ("Entrada no válida")

        if tupla_posicion == 0: #se acaba el juego, no se quiere seguir jugando

            salir = True

            break

        resultado = jugador_1.disparar(tupla_posicion, jugador_2) #comprobamos el tiro

        if resultado:

            es_maquina = False

            if jugador_2.vidas != 0:

                print("¡HAS ACERTADO!, te toca tirar de nuevo")

        else:

            print("No has acertado, pasa el turno a tú oponente: ")

            es_maquina = True

    else:
        print("Turno del oponente")

        apuntar = False

        while not apuntar: #toca turno al oponente

            tupla_posicion = posicion_random()

            if not tupla_posicion in jugador_2.disparos:

                apuntar =True

        print("Tú oponente está apuntando a: ", tupla_posicion)

        resultado = jugador_2.disparar(tupla_posicion, jugador_1)


        sleep(3)

        if not resultado:

            print(MENSAJES["fallo"] +" se pasa el turno al jugador: ")

            es_maquina = False

        else:
            print(MENSAJES["blanco"] + " le toca tirar de nuevo")

            es_maquina = True

            sleep(0.5)

if es_maquina and not salir:

    print(MENSAJES["perder"])

elif not es_maquina and not salir:

    print(MENSAJES["ganar"])

elif salir:

    print(MENSAJES["adios"])