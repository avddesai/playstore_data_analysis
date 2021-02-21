import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def max_4():
    df=pd.read_csv('Apps.csv')
    df=df.groupby(["Category"],as_index=False)[['Rating']].mean()
    return np.max(df)

def q4():
    df=pd.read_csv('Apps.csv')    
    ck=df.groupby(["Category"])[['Rating']].mean()
    ck.plot(kind='bar',alpha=0.75, rot=90)
    plt.xlabel("Categories")
    return ck 


    #print(np.max(ck))
    #plt.bar(x=x, height=y)

    # You can make your x axis labels vertical using the rotation
    
    #return plt.bar(x=ck["Category"],height=ck["Rating"]).xticks(x, rotation=90)







