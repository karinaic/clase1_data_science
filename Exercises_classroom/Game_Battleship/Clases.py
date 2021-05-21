#Here I am going to model my classes: Board, Player
# import necessary libraries
import numpy as np
import random

# I import my own modules
import Constantes as cs



class Barco:
    # To build the Boat object, we give it the tuple position parameters,
    # the length of the ship and the axis property that refers to the position of the ship in the x-axis or in the y-axis.


    def __init__(self, posicion, largo, axis = 0):#axis == 0 Vertical, axis == 1 Horizontal

        self.posicion = posicion
        self.largo = largo
        self.axis = axis

class Jugador:
    #is made up of two boards, one for the shots and the other for the ships, 
    #a lives property that represents the number of shots to be fired to sink all the ships, 
    # and a shot list, which stores the shots the player has fired.


    def __init__(self):

        self.tablero_barcos = Tablero(10)
        self.tablero_barcos.coloca_barcos_random()
        self.tablero_disparos = Tablero(10)
        self.vidas = 20
        self.disparos = []

    def imprimir_tablero(self): #print the boards
        titulo = np.array(cs.LIST_CHARACTERS) # we display the columns of the player's screens
        print("  ",titulo, "           ",titulo)
        print("")
        for i in range(len(cs.LIST_NUMBERS)): # we display the rows of the board
            if i != 9:
                numero = str(cs.LIST_NUMBERS[i]) + " "
            else:
                numero = str(cs.LIST_NUMBERS[i])

            print(numero, self.tablero_barcos.matriz[i],
                  "        ", numero, self.tablero_disparos.matriz[i])

        print("\n")


    def disparar(self, posicion, a_jugador): 
        # as parameters, we enter the position to shoot at and the player to shoot at. 
        # checks to see if the boat has been hit and if the player was successful, it subtracts a life variable of the affected player.


        self.disparos.append(posicion) # I keep the position in the empty shot list.

        posicion_traducida = self.traducir_posicion(posicion)


        if a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] == cs.BOAT_BOARD:

            self.tablero_disparos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.HIT_BOARD

            a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.HIT_BOARD

            a_jugador.vidas -= 1

            return True

        else:

            self.tablero_disparos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.MISS_BOARD

            a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.MISS_BOARD

            return False

    def traducir_posicion(self, posicion): # the number-letter parameter the player enters is passed and is translated to be read in the array

        x = posicion[0] - 1 #we subtract one because it starts at zero.

        y = cs.LIST_CHARACTERS.index(posicion[1]) #with the index.returns the index of the element given in the list.

        return (x, y)


class Tablero: #we define the position of the boats randomly, we had planned to pass a list with coordinates, but we were not able to implement it.

    def __init__(self, dimension, barcos=[]):  #we position the ships on the board

        self.dimension = dimension
        self.matriz = np.full((dimension, dimension), cs.WATER_BOARD )
        self.barcos = barcos

    def posicion_random(self):
        #create a random position on the board.

        x = random.randint(0, 9)

        y = random.randint(0, 9)

        return (x, y)

    def coloca_barcos_random(self): # it positions all the ships randomly

        for propiedades in cs.BOATS_TYPE:

            contador = 0

            while contador < propiedades[1]: #we check to see if we have ships according to list of boat types

                posicion = self.posicion_random()

                x = posicion[0]

                y = posicion[1]

                slicing_sur = self.matriz[x: x + propiedades[0], y]   #we check that the position of the boats are placed within the range of the board.

                slicing_norte = self.matriz[x: x - propiedades[0]:-1, y]

                slicing_este = self.matriz[x, y: y + propiedades[0]]

                slicing_oeste = self.matriz[x, y:y - propiedades[0]:-1]

                if cs.BOAT_BOARD not in slicing_sur and len(slicing_sur) == propiedades[0]:

                    self.matriz[x: x + propiedades[0], y] = cs.BOAT_BOARD
                    contador += 1

                elif cs.BOAT_BOARD not in slicing_norte and len(slicing_norte) == propiedades[0]:

                    self.matriz[x: x - propiedades[0]:-1, y] = cs.BOAT_BOARD
                    contador += 1

                elif cs.BOAT_BOARD not in slicing_este and len(slicing_este) == propiedades[0]:

                    self.matriz[x, y: y + propiedades[0]] = cs.BOAT_BOARD
                    contador += 1

                elif cs.BOAT_BOARD not in slicing_oeste and len(slicing_oeste) == propiedades[0]:

                    self.matriz[x, y:y - propiedades[0]:-1] = cs.BOAT_BOARD
                    contador += 1

    def imprimir_tablero(self):

        print(self.matriz)

    def coloca_barco(self, barco):

        cadena_letras = "ABCDEFGHIJ"

        x = barco.posicion[0] - 1

        y = cadena_letras.index(barco.posicion[1])

        if barco.axis == 0:

            self.matriz[x:barco.largo + x, y] = cs.BOAT_BOARD

        else:

            self.matriz[x, y:barco.largo + y] = cs.BOAT_BOARD

    def coloca_barcos(self):

        for barco in self.barcos:

            self.coloca_barco(barco)
     



