#funcion que decide quien empieza primero
import random 

def definir_turno(nombre1, nombre2): #definimos el turno del jugador.
    """Funcion para definir que jugador empieza el juego"""
    turno1 = random.randint(1, 6)
    print(f'El numero de {nombre1} es {turno1}')
    turno2 = random.randint(1, 6)
    print(f'El numero de {nombre2} es {turno2}')
    if turno1 > turno2:
        jugador = nombre1
        oponente = nombre2
        print(f'{nombre1} start the game and is the jugador')
        return jugador, oponente
    else:
        jugador = nombre2
        oponente = nombre1
        print(f'{nombre2} start the game and is the jugador')
        return jugador, oponente