##Aquí vamos a colocar todas nuestras variables que vamos a ir utilizando durante el juego, mensajes biemvenida, instrucciones,dimensiones de los barcos,etc.
##4 barcos 2x1, 3b 3x1, 2b 4x1, 1b 5x1.
#el diccionario Mensajes, lo he creado tambien en formato Json.
MENSAJES = {
    "introduccion": " **** Bienvenido al juego Battleship**** \
        \nLe presentamos su flota: \
        \n 1 Portador de 5x1 \
        \n 2 Acorazados de 4x1 \
        \n 3 Cruceros de 3x1 \
        \n 2 Submarinos de 2x1 \
        \n 2 Destructores de 2x2 ",

    "reglas" :" A continuación le indicamos las reglas del juego: \
        \n Coloque cada barco en cualquier posición horizontal o vertical pero no en diagonal \
        \n No coloque un barco de modo que cualquier parte de él se superponga a otro barco o al  borde de la cuadrícula \
        \n No se puede cambiar la posición del barco una vez empezado el juego. ",

    "blanco" : "Me ha dado en el blanco, buen tiro!",
    "fallo" :"Buen intento, pero has fallado, sigue intentando!",
    "ganar" : "¡¡¡¡¡¡Has  GANADO!!!!! muy BIEN HECHO!! FELICITACIONES",
    "perder": "Has PERDIDO, sigue intentando",
    "adios": "      Fín del juego \
        \n***Hasta la próxima***"
}

LISTA_CARACTERES = ['A','B','C','D','E','F','G','H','I','J'] #Sirve para traducir la posición de la letra a indice del tablero y para dibujar las referencias en la interfaz

LISTA_NUMEROS = [1,2,3,4,5,6,7,8,9,10] # Sirve para traducir la posición del número a indice del tablero y para dibujar las referencias en la interfaz

TIPOS_BARCO = [(4, 2), (3, 3), (2, 4), (1, 5)] #guarda un listado de tuplas con el eslora del barco y el número que hay que dibujar

BARCO_CHAR= "#"

AGUA_CHAR = "~"

TOCADO_CHAR = "X"

FALLO_CHAR = "Ø"
