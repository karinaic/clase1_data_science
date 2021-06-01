##que contiene la funcionalidad que inicia la API de Flask. Esto
#el archivo solo se ejecutará si se le pasa un argumento "-x 8642" (argparse), de lo contrario
#mostrará "contraseña incorrecta".
import argparse

####AQUI TENGO QUE PONER LA FUNCION DE FLASK
UPLOAD_FOLDER = os.sep + "AQUI VA LA CARPETA QUE QUIERO USAR" + os.sep

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hellohello' 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x", type=int, help="wrong pasword", required=True)

    args = vars(parser.parse_args())
    x = args["x"] 
    if x == 8642:
        main()
    

