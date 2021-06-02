#FUNCIONES DEL DASHBOARD
import streamlit as st
from PIL import Image
import pandas as pd
import os 
import requests
import json
path = os.path.dirname(__file__)
import utils.visualization_tb as vt


def configuracion():
    st.set_page_config(page_title='Global Vaccination Covid19', page_icon=':electric_plug:', layout="wide")

def menu_home():
    st.title('Exploratory Data Analysis Global Vaccination SARS-CoV-2 (Covid19)')
    st.write('The first time a person is infected with the virus that causes COVID-19,\
        it can take several days or weeks for his or her body to develop and use all  \
        the tools it needs to fight off the germs and overcome the infection.\
        After infection, the person''s immune system remembers what it learned about how to protect the body from disease.\
        COVID-19 vaccines help our body develop immunity to the virus that causes COVID-19 without us having to get the disease.')

def menu_data():    
    dir = os.path.dirname
    path = os.path.dirname(__file__)
    csv_path = dir(dir(path)) + os.sep + 'data' + os.sep+'country_vaccinations_cleaned.csv'
    df = pd.read_csv(csv_path)
    st.dataframe(df)

    
def menu_api(): 
    url= "http://localhost:6060/token_id?token_id=W51163571"
    json_api = requests.get(url).json()
    return {'Unnamed: 0': dict(json_api)['Unnamed: 0']}

def menu_graphs():
    
    csv_path = dir(dir(path)) + os.sep + 'data' + os.sep+'country_vaccinations_cleaned.csv'
    df = pd.read_csv(csv_path)
    st.pyplot(vis.serie_temporal(data))
