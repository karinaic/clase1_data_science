def km_millas(distancia):
    """vamos a crear un conversor de km a millas
    *args distancia = distancia en kilomentros"""
    millas = distancia * 0.62
    return millas



def factorial(x):
    """funcion recursiva, en su algoritmo hacen referencia a sí misma"""
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)