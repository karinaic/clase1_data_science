
from datetime import datetime
""" importamos la libreria datetime, creamos una fucion para que nos muestre la hora actual"""

def current_time():
    now = datetime.now().time()
    return now

def current_date_time():
    """ funcion que nos retorna la hora y la fecha actual"""
    time = datetime.now().time()
    date = datetime.now().date()
    return time, date


if __name__ == "__main__":
    print(current_time())


