
#Import libraries
import numpy as np 
import random
from time import sleep
from tqdm import tqdm

#Import owns scripts
from Clases import *
import Constantes as cs
from time import sleep
from tqdm import tqdm
from Constantes import MESSAGES


def posicion_random(): #we make an array 10x10 of characteres and numbers lists.

    x = random.randint(1, 10)
    y = cs.LIST_CHARACTERS[random.randint(0, 9)]

    return (x, y)

#we interpret the coordinates entered by the player
def lee_input(jugador, posicion): 
    #A player and a position introduce them as parameters. this method checks the validity of the shot,
    # must not have fired in that same position and
    # has to be well constructed so that it identifies a real position on the board

    resp = None

    try:
        if len(posicion) == 3:
            if int(posicion[0:2]) == 10 and posicion[2].upper() in cs.LIST_CHARACTERS:
                resp = (int(posicion[0:2]), posicion[2].upper())

        elif len(posicion) == 2:
            if int(posicion[0]) > 0 and int(posicion[0]) < 10 and posicion[1].upper() in cs.LIST_CHARACTERS:
                resp = (int(posicion[0]), posicion[1].upper())

        elif posicion == "0":

            resp = 0

        if resp in jugador.disparos:
            print("Sorry, You have already shot in this position")
            resp = None

        return resp
    except:
        return None

es_maquina = False

salir = False

#our players
#calling Jugador Class
jugador_1 = Jugador()

jugador_2 = Jugador()

#we introduce welcome message

print(MESSAGES["introduction"])

sleep(0.5)

# we introduce the symbols to which the marks refer on the board

print("The symbols '~' refer to water")

sleep(0.5)

print("The 'Ø' symbol refers to a miss shot")

sleep(0.5)

print("The symbol 'X' refers to hit ship")

sleep(0.5)

# we introduce the rules of the game
print(MESSAGES["Rules"])

sleep(0.5)

print("           ARE YOU READY????....CHARGING...\n ")
for i in tqdm(range(10)):
    sleep(0.5)

input("Press enter to continue")

#instanciamos el juego

while jugador_1.vidas > 0 and jugador_2.vidas > 0 :# We check that one of us still has lives
    
    if not es_maquina:
        jugador_1.imprimir_tablero()
        
        while True:
            print("If you want to quit the game you just have to press = 0")
            posicion = str(input("Enter the coordinate to which you want to dip: rows from 1 to 10 and columns from A - J  \
                \nExample: 1A -------> Try it here: "))

            tupla_posicion = lee_input(jugador_1, posicion) #llamamos a la funcion que nos devuelve el imput con la coordenada ingresada por el jugador

            if tupla_posicion != None:

                break

            else:
                print ("unvalid entry, Try again")

        if tupla_posicion == 0: #the game is over, you don't want to continue playing

            salir = True

            break

        resultado = jugador_1.disparar(tupla_posicion, jugador_2) #comprobamos el tiro

        if resultado:

            es_maquina = False

            if jugador_2.vidas != 0:

                print("¡YOU'RE SUCCESSFUL! It's your turn to shoot again")

        else:

            print("You were not correct, pass the turn to your opponent:")

            es_maquina = True

    else:
        print("Opponent's turn")

        apuntar = False

        while not apuntar: #toca turno al oponente

            tupla_posicion = posicion_random()

            if not tupla_posicion in jugador_2.disparos:

                apuntar =True

        print("Your opponent is targeting: ", tupla_posicion)

        resultado = jugador_2.disparar(tupla_posicion, jugador_1)


        sleep(3)

        if not resultado:

            print(MESSAGES["Miss"] +" the turn is passed to the player: ")

            es_maquina = False

        else:
            print(MESSAGES["Hit"] + " shoot again")

            es_maquina = True

            sleep(0.5)

if es_maquina and not salir:

    print(MESSAGES["lose"])

elif not es_maquina and not salir:

    print(MESSAGES["win"])

elif salir:

    print(MESSAGES["goodbye"])