import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot
def qy_19():
    df=pd.read_csv("Apps.csv")

    df["Installs"]=df['Installs'].str.replace('\,',"") 
    df["Installs"]=df['Installs'].str.replace('+',"")

    df['Installs']=pd.to_numeric(df['Installs'])      
    x = df['Installs']
    y = df['Rating']
    graph=plt.title("Ratings vs Installations")
    graph=plt.xlabel("No of Installations")
    graph=plt.ylabel("Ratings")
    graph=plt.plot(x, y, 'o', color='blue')   
    return graph
#qy_19()
