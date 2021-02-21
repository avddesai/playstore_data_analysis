import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def qy_17():
    df=pd.read_csv("Apps.csv")
    df_Size=pd.DataFrame(df["Size"])
    df_Size['Installs']=df['Installs'].values
    for i in df_Size:
        if(i.find("M") or i.find("k") or i.find("Varies with device") ):
            df_Size["Size"]=df_Size["Size"].str.replace("M","")
            df_Size["Size"]=df_Size["Size"].str.replace("k","")
            df_Size["Size"]=df_Size["Size"].str.replace("Varies with device","0")
    df_Size["Size"] = pd.to_numeric(df_Size["Size"])   
    df_Size["Size"]=df_Size["Size"].replace(np.nan, 0)        
    df_Size["Installs"]=df_Size['Installs'].str.replace('\,',"") 
    df_Size["Installs"]=df_Size['Installs'].str.replace('+',"")
    df_Size['Installs']=pd.to_numeric(df_Size['Installs'])      
    hist_plot=plt.hist(df_Size["Size"],bins=[25,50,75,100],rwidth=0.95,color='g')
    hist_plot=plt.title("Number of installs for size")
    hist_plot=plt.xlabel("Size")
    hist_plot=plt.ylabel("No of installs")
    return hist_plot