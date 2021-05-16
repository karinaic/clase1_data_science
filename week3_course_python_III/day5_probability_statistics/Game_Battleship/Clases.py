##Aqui voy a modelizar mis clases: Tablero , Jugador
#importo librerias necesarias
import numpy as np
import random

#importo módulos propios
import Constantes as cs



class Barco:
    # Para construir el objeto Barco se le pasan los parámetros tupla posición,
    # el largo del barco y la propiedad axis que hace referencia a la disposición del barco en el eje x o en el eje y

    def __init__(self, posicion, largo, axis = 0):#axis == 0 Vertical, axis == 1 Horizontal

        self.posicion = posicion
        self.largo = largo
        self.axis = axis

class Jugador:
    ##esta formado por dos tableros, uno para los disparos y otro para los barcos, 
    #una propiedad de vidas que representa el número de disparos que hay que hacer para hundir todos los barcos, 
    # y una lista de disparos, que almacena los disparos que ha realizado el jugador.

    def __init__(self):

        self.tablero_barcos = Tablero(10)
        self.tablero_barcos.coloca_barcos_random()
        self.tablero_disparos = Tablero(10)
        self.vidas = 20
        self.disparos = []

    def imprimir_tablero(self): #printa los tableros
        titulo = np.array(cs.LISTA_CARACTERES) # pintamos las columnas de las pantallas de los jugadores
        print("  ",titulo, "           ",titulo)
        print("")
        for i in range(len(cs.LISTA_NUMEROS)): #pintamos las filas de los tableros
            if i != 9:
                numero = str(cs.LISTA_NUMEROS[i]) + " "
            else:
                numero = str(cs.LISTA_NUMEROS[i])

            print(numero, self.tablero_barcos.matriz[i],
                  "        ", numero, self.tablero_disparos.matriz[i])

        print("\n")


    def disparar(self, posicion, a_jugador): 
        #como parámetros se le pasa la posición a la que se dispara y el jugador al que se dispara. 
        # Comprueba si se ha acertado y en ese caso resta la variable vida del jugador afectado

        self.disparos.append(posicion) #guardo la posicion en la lista de disparos vacia

        posicion_traducida = self.traducir_posicion(posicion)


        if a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] == cs.BARCO_CHAR:

            self.tablero_disparos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.TOCADO_CHAR

            a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.TOCADO_CHAR

            a_jugador.vidas -= 1

            return True

        else:

            self.tablero_disparos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.FALLO_CHAR

            a_jugador.tablero_barcos.matriz[posicion_traducida[0], posicion_traducida[1]] = cs.FALLO_CHAR

            return False

    def traducir_posicion(self, posicion): #se pasa como parámetro la posición numero letra que pasa el jugador y se traduce para leer en la matriz

        x = posicion[0] - 1  #le restamos uno porque empieza en cero.

        y = cs.LISTA_CARACTERES.index(posicion[1]) #con el index.devuelve el índice del elemento dado en la lista.

        return (x, y)


class Tablero: #definimos la posicion de los barcos de manera aleatoria, se esperaba pasar una lista con  coordenada, pero no hemos conseguido implementarlo.

    def __init__(self, dimension, barcos=[]):  #posicionamos los barcos en el tablero

        self.dimension = dimension
        self.matriz = np.full((dimension, dimension), cs.AGUA_CHAR)
        self.barcos = barcos

    def posicion_random(self):
        #crea una posición dentro del tablero de forma aleatoria

        x = random.randint(0, 9)

        y = random.randint(0, 9)

        return (x, y)

    def coloca_barcos_random(self): #se encarga de colocar todos los barcos de forma aleatoria

        for propiedades in cs.TIPOS_BARCO:

            contador = 0

            while contador < propiedades[1]: #comprobamos que tenemos barcos de acuerdo al tipo de barcos

                posicion = self.posicion_random()

                x = posicion[0]

                y = posicion[1]

                slicing_sur = self.matriz[x: x + propiedades[0], y]   #comprobamos que la posicion de los barcos se ubiquen dentro del rango del tablero

                slicing_norte = self.matriz[x: x - propiedades[0]:-1, y]

                slicing_este = self.matriz[x, y: y + propiedades[0]]

                slicing_oeste = self.matriz[x, y:y - propiedades[0]:-1]

                if cs.BARCO_CHAR not in slicing_sur and len(slicing_sur) == propiedades[0]:

                    self.matriz[x: x + propiedades[0], y] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_norte and len(slicing_norte) == propiedades[0]:

                    self.matriz[x: x - propiedades[0]:-1, y] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_este and len(slicing_este) == propiedades[0]:

                    self.matriz[x, y: y + propiedades[0]] = cs.BARCO_CHAR
                    contador += 1

                elif cs.BARCO_CHAR not in slicing_oeste and len(slicing_oeste) == propiedades[0]:

                    self.matriz[x, y:y - propiedades[0]:-1] = cs.BARCO_CHAR
                    contador += 1

    def imprimir_tablero(self):

        print(self.matriz)

    def coloca_barco(self, barco):

        cadena_letras = "ABCDEFGHIJ"

        x = barco.posicion[0] - 1

        y = cadena_letras.index(barco.posicion[1])

        if barco.axis == 0:

            self.matriz[x:barco.largo + x, y] = cs.BARCO_CHAR

        else:

            self.matriz[x, y:barco.largo + y] = cs.BARCO_CHAR

    def coloca_barcos(self):

        for barco in self.barcos:

            self.coloca_barco(barco)
     



