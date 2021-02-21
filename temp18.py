# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 00:20:52 2020

@author: Samit Patil
"""
"""import csv
import pandas as pd
df=pd.read_csv('Apps.csv')
print(df.iloc[0:3])
df["Installs"] = df["Installs"].str.replace("\,","")
df["Installs"] = df["Installs"].str.replace("+","")
df["Installs"] = pd.to_numeric(df["Installs"])
#print(df["Installs"])
sales=df.groupby(['Category'],as_index=False).agg({'Installs':'sum'})
print(sales)
l1=['A','B']
#l1.append(['e','f'])
#df=pd.DataFrame(l1,columns=['',''])
#df.to_csv('demo.csv', mode='a', header=True)
with open("demo.csv", "a", newline='') as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(l1)
"""
import pandas as pd 
import numpy as np
def uniqcat():
    df=pd.read_csv("Apps.csv")
    df=pd.DataFrame(df["Category"])
    #df1["Rev"]=df["Translated_Review"]
    #df1["Subj"]=df["Sentiment_Subjectivity"]
    #df1["Pol"]=pd.to_numeric(df1["Pol"])
    #df1["Subj"]=pd.to_numeric(df1["Subj"])
    #a=list()
    #print(df1)
    l=df['Category'].unique()
    return l
def uniqinstalls():
    df=pd.read_csv("Apps.csv")
    df=pd.DataFrame(df["Installs"])
        #df1["Rev"]=df["Translated_Review"]
        #df1["Subj"]=df["Sentiment_Subjectivity"]
        #df1["Pol"]=pd.to_numeric(df1["Pol"])
        #df1["Subj"]=pd.to_numeric(df1["Subj"])
        #a=list()
        #print(df1)
    l=df['Installs'].unique()
    return l
def uniqcontent_r():
    df=pd.read_csv("Apps.csv")
    df=pd.DataFrame(df["Content Rating"])
            #df1["Rev"]=df["Translated_Review"]
            #df1["Subj"]=df["Sentiment_Subjectivity"]
            #df1["Pol"]=pd.to_numeric(df1["Pol"])
            #df1["Subj"]=pd.to_numeric(df1["Subj"])
            #a=list()
            #print(df1)
    l=df['Content Rating'].unique()
    return l
    #print(l)
def uniq_genre():
    df=pd.read_csv("Apps.csv")
    df=pd.DataFrame(df["Genres"])
            #df1["Rev"]=df["Translated_Review"]
            #df1["Subj"]=df["Sentiment_Subjectivity"]
            #df1["Pol"]=pd.to_numeric(df1["Pol"])
            #df1["Subj"]=pd.to_numeric(df1["Subj"])
            #a=list()
            #print(df1)
    l=df['Genres'].unique()
    return l
#print(uniq_genre())