import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def qy_15():
    df=pd.read_csv("Sentiment.csv")
    ck=df.loc[df['App'] == '10 Best Foods for You']
    #print(ck)
    ck['Count']=1
    #print(ck)
    rev=ck.groupby(['Sentiment'],as_index=False).agg({'Count':'sum'})
    return rev


#sales=df.groupby(['Category']).agg({'Installs':'sum'})
#print(sales)
#sales_pct=sales.apply(lambda x:100*x/float(x.sum()))
#print(sales_pct)