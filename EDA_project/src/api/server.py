from flask import Flask, request, render_template
import os
import sys
import argparse
import json

dir = os.path.dirname
src_path = dir(dir(dir(__file__))) #SUBO DOS CARPETAS
sys.path.append(src_path)

from src.utils.folders_tb import read_json


# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    #return app.send_static_file('greet.html')
    return "Country Vaccinations"

json_project = dir(dir(os.path.dirname(__file__))) + os.sep + 'reports' + os.sep + "json_project.json"

# localhost:6060/token_id?token_id=W51163571
@app.route('/token_id', methods=['GET'])                                                                                                                                                                          
def give_tokenid():
    s = request.args['token_id']
    json_file = read_json(fullpath=json_project)
    if s == "W51163571":
        return json.dumps(json_file)
    else:
        return "Wrong password"

#settings_json = dir(dir(os.path.dirname(__file__))) + os.sep + 'reports' + os.sep + "json_project.json"


@app.route("/recibe_informacion")
def recibe_info():
    pass 

#---------- Other functions ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x", type=int, help="the argument", required=True)
    args = vars(parser.parse_args())
    argument = args["x"]

    #argument =  input('Insert an argument to start the process')
    if argument == 8642:

        print("---------STARTING PROCESS---------")
        print(__file__)
    
        # Para ambos: os.sep
        settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
        print(settings_file)
        # Load json from file
        json_readed = read_json(fullpath=settings_file)
        
        # Load variables from jsons
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
    
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print('wrong password')

if __name__ == "__main__":
    main()
