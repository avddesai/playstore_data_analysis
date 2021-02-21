import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import re
import matplotlib.mlab as mlab
#%matplotlib inline
#a=pd.read_csv('C:\\Users\\Samit Patil\\Desktop\\PlaystoreStudy Project\\Apps.csv',delimiter = ',',names=['Category','Installs'],encoding="Latin-1",header=0)

#path="C:\\Users\\Samit Patil\\Desktop\\PlaystoreStudy Project\\Apps.csv"
#file=open(path,newline='',encoding="utf8")
#reader=csv.reader(file)
#header=next(reader)
#data=[row for row in reader]
#print(header)
#for i in len(data):
#    print(data[i])
def q5():
    df=pd.read_csv("Apps.csv")
#print(df.iloc[5,1])
#df_Size=pd.DataFrame(df["Size"])

    df_Size=pd.DataFrame(df["Size"])
    df_Size['Installs']=df['Installs'].values


#df["Size"]=df["Size"].str.replace("M","")
#df["Size"]=df["Size"].str.replace("Varies with device","0")
#df["Size"]=df["Size"].str.replace("k","")

    for i in df_Size:
        if(i.find("M") or i.find("k") or i.find("Varies with device") ):
            df_Size["Size"]=df_Size["Size"].str.replace("M","")
        
        #df_Size["Size"]=df_Size["Size"].str.replace("k","",-1)
            
        
            df_Size["Size"]=df_Size["Size"].str.replace("Varies with device","0")
    
    df_Size["Size"] = df_Size["Size"].convert_objects(convert_numeric=True)
    df_Size["Size"]=df_Size["Size"].replace(np.nan, 0)        
        
    #elif(i.find("k")):
     #   df_Size["Size"]=df_Size["Size"].str.replace("k","")
        #df["Size"]=pd.to_numeric(df["Size"])/1000
    #elif(i.find("Varies with device")):
     #   df_Size["Size"]=df_Size["Size"].str.replace("Varies with device","0")
        #df["Size"]=pd.to_numeric(df["Size"])
#df_Size["Size"]=pd.to_numeric(df_Size["Size"])
#print(df_Size["Size"])
#df_Size["Installs"] = df_Size["Installs"].astype(str)

#df_Size["Installs"]=df_Size["Installs"].str.replace({'\,':"","+":""},-1,regex=True)
    df_Size["Installs"]=df_Size['Installs'].str.replace('\,',"") 
    df_Size["Installs"]=df_Size['Installs'].str.replace('+',"")

    df_Size['Installs']=pd.to_numeric(df_Size['Installs'])
#df_Size['Installs'] = df_Size['Installs'].astype(int)


#print(df_Size)
#print(df_Size["Size"].unique())
    hist_plot=plt.hist(df_Size["Size"],bins=[10,20,30,100],rwidth=0.75,color='g')
    hist_plot=plt.title("Number of installs for app sizes")
    hist_plot=plt.xlabel("Sizes of apps")
    hist_plot=plt.ylabel("No. of installs")
    return hist_plot
    #print(max(df_Size["Size"].unique()))

#plt.hist(data, bins=[0, 10, 20, 30, 40, 50, 100])


#df["Size"]=pd.to_numeric(df["Size"])

#print(df["Size"])

#print(df["Installs"].unique())
#hist_plot=plt.hist(df["Installs"],bins=22)
#hist_plot=plt.title("Number of Apps installed")
#hist_plot=plt.xlabel("Range of installs")
#hist_plot=plt.ylabel("Frequency")
#plt.show()
