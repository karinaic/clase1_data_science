import seaborn as sns
import matplotlib.pyplot as plt 
import os, sys
from quickda.explore_data import *
from quickda.clean_data import *
from quickda.explore_numeric import *
from quickda.explore_categoric import *
from quickda.explore_numeric_categoric import *
from quickda.explore_time_series import *


def numerical_features(data):
    return eda_num(data)


def outliers_total_vacunnation(data):
    return eda_num(data[['total_vaccinations']])


def outliers_people_vaccinated(data):
    return eda_num(data[['people_vaccinated']])


def outliers_people_fully_vaccinated(data):
    return eda_num(data[['people_fully_vaccinated']])

def vaccines_brand(data):
    conteo = data['vaccines'].value_counts()
    plt.figure(figsize=(20,30))
    plt.hlines(y = conteo.index,
    xmin=140,
    xmax=conteo,
    color= 'skyblue')
    plt.plot(conteo, conteo.index, "o")
    plt.title("Brand of vaccines more used by the countries")
    plt.savefig('../resources/Brand_vaccines.png')

def five_countries(df2):
    
    plt.figure(figsize=(40,10))
    sns.lineplot(data = df2,
    x = 'date',
    y = 'daily_vaccinations',
    hue = 'country',
    linewidth = 3)
    plt.title("Five countries in Europe")
    plt.savefig('../resources/five_countries.png')


def data_correlacion(df):
    f, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(df.corr(),
    vmin = -1,
    vmax = 1,
    annot = True,
    linewidths = .5)
    plt.title("Correlation Matrix")
    plt.savefig('../resources/correlation.png')

def serie_temporal(data):
    eda_timeseries(data, x= "date" , y = "total_vaccinations_per_hundred")


def spent_time ():
    time = pd.DataFrame({'Time': [0.60, 0.10 , 0.15, 0.05, 0.05, 0.05 ],
    'Task': ['Data Sourcing', 'Data wrangling', 'Exploratory Data Analysis', 'Flask', 'Streamlit','Presentation']})
    plot = time.plot.pie(y='Time', autopct='%1.2f%%',shadow=True, figsize=(5, 5))
    labels = 'Data Sourcing', 'Data wranling', 'Exploratory Data Analysis', 'Flask', 'Streamlit','Presentation'
    plt.legend(labels, bbox_to_anchor=(1,0), loc="lower right",
    bbox_transform=plt.gcf().transFigure)

