import pandas as pd 
import numpy as np
def input12():
    df=pd.read_csv("Sentiment.csv")
    df1=pd.DataFrame(df["App"])
    df1["Sent"]=df["Sentiment"]
    
    return(df1)
#print(inputtwelfth())


pos=input12().loc[input12()['Sent']=='Positive']
    #print(pos)
#print (pos)
    #print("----App with maximum Positive sentiments----")
    #df2 = pos.groupby(['App','Sent']).size().groupby(level=0).idxmax().apply(lambda x: x[1]).reset_index(name='Sent')
def pos_12():
    #pos=input12().loc[input12()['Sent']=='Positive']
    #df2=df2.iloc[0]
    #pos=input12().loc[input12()['Sent']=='Positive']
    df2=pos.groupby('App').count().Sent.idxmax()
    #df2=pos.groupby(['App','Sent']).size()
    #df2=df2.loc(max(df2))
    return df2
#print (pos_12())
#print (pos_12())

#df2 = pos.groupby(['App'])['Sent'].apply(lambda x: x.value_counts().index[0]).reset_index()
#print(df2)

neg=input12().loc[input12()['Sent']=='Negative']
#print(neg)
def neg_12():
#df3=neg.groupby(['App','Sent']).size()
#print(df3)
#print("----App with maximum Negative sentiments----")
    
    #neg=input12().loc[input12()['Sent']=='Negative']
    df3=neg.groupby('App').count().Sent.idxmax()
    return df3
#posneg=inputtwelfth().loc[(inputtwelfth()['Sent']=='Positive') | (inputtwelfth()['Sent']=='Negative' )]
#print(posneg)
#print(posneg.groupby('App').count())

def eqposneg():
    p=pos.groupby('App').count()
    p.rename(columns = {'Sent':'P'}, inplace = True)
    #print(p)
    n=neg.groupby('App').count()
    n.rename(columns = {'Sent':'N'}, inplace = True)
    #print(n)
    df = pd.concat([p, n], axis=1,sort=False)
    #print(df)

    # check equality
    lst=[]
    for i in range(len(df)):
        if df.iloc[i]['P'] == df.iloc[i]['N']:
            #print(df.index[i], df.iloc[i]['P'])
            #df1=df.index[i]
            lst.append(df.index[i])
    df1=pd.DataFrame(lst)
    return df1

#df4=po.loc[]
#print(df3)
#df3 = neg.groupby(['App','Sent']).size().groupby(level=0).idxmax().apply(lambda x: x[1]).reset_index(name='Sent')
#df3=df3.iloc[0]
#print(df3)

