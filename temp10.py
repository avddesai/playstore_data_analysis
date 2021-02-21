import matplotlib.pyplot as py
import pandas as pd
import numpy as np
from fractions import Fraction

def input_tenth():
    df=pd.read_csv("Apps.csv")
    df1=pd.DataFrame(df["Installs"])
    df1["CR"]=df["Content Rating"]
    df1["Month"]=df["Last Updated"]
    df1["Month"]=df1["Month"].str.replace("\,","")
    df1["Month"]=df1["Month"].str.replace("\d+ \d+","")
    #df1["Year"]=df["Last Updated"]
    df1["Year"]=df["Last Updated"].str.replace(r"([a-zA-Z]+) (\d+)","")
    df1["Year"]=df1["Year"].str.replace("\,","")
    df1["Year"]=pd.to_numeric(df1["Year"])
    df1['Installs']=df1['Installs'].str.replace("\,","")
    df1['Installs']=df1['Installs'].str.replace("+","")
    df1['Installs']=pd.to_numeric(df1['Installs'])
    df1['Category']=df['Category']

    return(df1)
#print(input_tenth())
def q10a():
    df2=input_tenth().loc[(input_tenth()["CR"]=='Teen') | (input_tenth()["CR"]=='Mature 17+')]
    #print(df2)
    sum1=df2.groupby(['CR'],as_index=False).agg({'Installs':'sum'})
    sum1['Installs']=pd.to_numeric(sum1['Installs'])
    return sum1


#ratio=(sum1.iloc[1,1])/(sum1.iloc[0,1])
#print(ratio)
def q10b():
    f=Fraction((q10a().iloc[1,1]),(q10a().iloc[0,1])).limit_denominator()
    return f
#sales_pct=sales.apply(lambda x:100*x/float(x.sum()))
#df1 = input_tenth().loc[input_tenth().groupby('Last Updated')['Downloads'].agg(['idxmin','idxmax']).stack()].reset_index()
#print(df1)
def q10c():
    f3=input_tenth()
    f3=f3.loc[f3.groupby('Category')['Installs'].agg(['idxmax']).stack()].reset_index()
    return f3