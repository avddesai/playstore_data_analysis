import pandas as pd
import numpy as np
df=pd.read_csv('Apps.csv')
df["Installs"] = df["Installs"].str.replace("\,","")
df["Installs"] = df["Installs"].str.replace("+","")
df["Installs"] = pd.to_numeric(df["Installs"],errors='coerce')

def varies():
    ck=df.loc[df['Android Ver'] == 'Varies with device']
    sum1=ck['Installs'].sum()
    return sum1

def n_varies():
    dk=df.loc[df['Android Ver'] != 'Varies with device']
    sum2=dk['Installs'].sum()
    return sum2

def per():
    #print("The increase in percentage downloads is:")
    return ((varies()-n_varies())*100/(varies()))

#print (per())



