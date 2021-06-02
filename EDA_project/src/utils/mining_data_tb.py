import pandas as pd 
import numpy as np

def to_dataframe(df, col):
    
    data = df.groupby('country')[col].max()
    data = pd.DataFrame(data)
    
    return data

x = 2

def formato_fecha(df):
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.strftime('%m-%d-%Y')
    return df['date']

print("funciona")

def sorted_row(df):
    df = df.sort_values(['date', 'country'], ascending=True)
    return df


def not_null(df):
    df = df.groupby('country').apply(lambda group: group.fillna(method='ffill'))
    df = df.groupby('country').apply(lambda group: group.fillna(0))
    return df

def five_countries(df):
    df2 = df[df['country'].isin(['Spain', 'Germany', 'France',"Italy","Portugal"])]
    df2 = df2.groupby(['country', 'date']).sum()
    df2.reset_index(inplace=True)
    return df2


if __name__ == "__main__":
    print('Ejecutando como programa principal')
    to_dataframe(df, col)




