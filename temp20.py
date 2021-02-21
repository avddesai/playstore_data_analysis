import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def qy_20():
    df=pd.read_csv("Apps.csv")

    df_Size=pd.DataFrame(df["Reviews"])
    df_Size['Installs']=df['Installs'].values
    df_Size["Installs"]=df_Size['Installs'].str.replace('\,',"") 
    df_Size["Installs"]=df_Size['Installs'].str.replace('+',"")
    
    df_Size['Installs']=pd.to_numeric(df_Size['Installs'])

    #print(df_Size)
    hist_plot=plt.hist(df_Size["Installs"],bins=[10,100,800,3000],rwidth=0.95,color='g')
    hist_plot=plt.title("Number of reviews vs installs")
    hist_plot=plt.xlabel("Number of reviews")
    hist_plot=plt.ylabel("No. of installs")
    return hist_plot
#print(max(df_Size["Installs"].unique()))


#qy_20()