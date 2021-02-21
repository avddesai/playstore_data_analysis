import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

def q9():
    df=pd.read_csv('Apps.csv')

    df_downloads_ratings=pd.DataFrame(df["Installs"])
    df_downloads_ratings["App"]=df["App"]
    df_downloads_ratings["Rating"]=df["Rating"]



    df_downloads_ratings['Installs']=df_downloads_ratings['Installs'].str.replace("\,","")
    df_downloads_ratings['Installs']=df_downloads_ratings['Installs'].str.replace("+","")
    df_downloads_ratings['Installs']=pd.to_numeric(df_downloads_ratings['Installs'])
    df_downloads_ratings['Rating']=pd.to_numeric(df_downloads_ratings['Rating'])
    
#    return df_downloads_ratings



#print(installs_ratings_convert_int())

#df1=df_downloads_ratings[df_downloads_ratings['Rating'].between(4.1,5.0,inclusive=True)].groupby(['Installs'])

    df1=df_downloads_ratings.loc[(df_downloads_ratings['Rating']>=4.1) & (df_downloads_ratings['Installs']>100000)]
    return df1
#print("We can conclude that the higher ratings for apps consequently leads to their higher downloads" )
 
#print(df1)