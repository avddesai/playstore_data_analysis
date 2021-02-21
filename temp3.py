import pandas as pd
import numpy as np
#from test_gui import qy3,adjustWindow
#from pandastable import Table, TableModel
df=pd.read_csv('Apps.csv')
df["Installs"] = df["Installs"].str.replace(",","")
df["Installs"] = df["Installs"].str.replace("+","")

#(df[pd.to_numeric(df.col, errors='coerce').isnull()])
df["Installs"] = pd.to_numeric(df["Installs"],errors='coerce')
downloads=df.groupby(['Category'],as_index=False).agg({'Installs':'sum'})
#print(downloads)


def min1():
    minimum=np.min(downloads['Installs'])
#print(downloads.loc[downloads['Installs']==minimum])


    return (downloads.loc[lambda downloads: downloads['Installs'] == minimum])
    #df.loc[lambda df: df['shield'] == 8]

def max1():
    maximum=np.max(downloads['Installs'])
    return (downloads.loc[lambda downloads:downloads['Installs']==maximum])
    
##average=np.avg(downloads)
##print(average)
def avg1():
    return (downloads.loc[lambda downloads:downloads['Installs']>250000])
    #return (category)
#print(minimum)
#df['Installs']=downloads.df['Installs']
#print(df['Installs'])
#print(min1())