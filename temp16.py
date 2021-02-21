import pandas as pd
def qy_16():
    df=pd.read_csv("Apps.csv")
    df1=pd.DataFrame(df["Last Updated"])
    df["Installs"] = df["Installs"].str.replace(",","")
    df["Installs"] = df["Installs"].str.replace("+","")
    df["Installs"] = pd.to_numeric(df["Installs"])
    df1["Installs"]=df["Installs"]
    df1["Month"]=df["Last Updated"]
    df1["Month"]=df1["Month"].str.replace("\,","")
    df1["Month"]=df1["Month"].str.replace("\d+ \d+","")
    #print(df1['Month'])
    #d=df1.groupby(['Month'],as_index=False)
    #print(d)
    av=df1.groupby(['Month'],as_index=False).agg({'Installs':'sum'})
    #print(av)
    av=av.drop(4)
    return av.sort_values('Installs', ascending=False)
    
#print(qy_16())

