import sys
sys.path 

ruta_absoluta_z = "C:\\Users\\Karina\\Desktop\\data_science_apr_2021\\clase1_data_science\\week3_course_python_III\\day2_python_VIII\\exercises\\imports"

sys.path.append(ruta_absoluta_z)
sys.path

import b.y
def f1z():
    b.y.f1y()
    print("f1z")
    
    
import a.x
def f2z():
    a.x.f2x()
    print("f2z")

var_1y = "hola"
var_2y = "mundo"