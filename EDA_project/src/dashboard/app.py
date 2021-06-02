import streamlit as st

import os, sys
print(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
print(sys.path)


import utils.dashboard_tb as ft

import pandas as pd
path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


csv_path = path + os.sep + 'data'+ os.sep + "country_vaccinations_cleaned.csv"

ft.configuracion()

menu = st.sidebar.selectbox('Menu:',
                            options=['Home','Data','API','Graphs'])

st.title("Country Vaccinations around the world")
df = pd.read_csv(csv_path)
if menu == 'Home':
    ft.menu_home()
elif menu == 'Data':
    ft.menu_data()
elif menu == 'API':
    mijson = ft.menu_api()
    st.write(mijson)
elif menu == 'Graphs':
    ft.menu_graphs()
    
    #ME FALTA PONER LAS FUNCIONES DE LOS GRAFICOS