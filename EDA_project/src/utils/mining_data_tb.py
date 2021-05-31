import pandas as pd 
import numpy as np

def to_dataframe(df, col):
    
    data = df.groupby('country')[col].max()
    data = pd.DataFrame(data)
    
    return data

x = 2












if __name__ == "__main__":
    print('Ejecutando como programa principal')
    to_dataframe(df, col)




