import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
def q6():
    df=pd.read_csv('Apps.csv')
    df_year_d=pd.DataFrame(df["Last Updated"])
    df_year_d['Downloads']=df['Installs'].values
    df_year_d['Category']=df['Category'].values
#df_year_d['Years']=df['Last Updated'].values
    df_year_d['Downloads']=df_year_d['Downloads'].str.replace(",","")
    df_year_d['Downloads']=df_year_d['Downloads'].str.replace("+","")
    df_year_d['Downloads']=pd.to_numeric(df_year_d['Downloads'])

    df_year_d['Last Updated']=df_year_d['Last Updated'].str.rsplit(', ').str[-1]
    df_year_d['Last Updated']=pd.to_numeric(df_year_d['Last Updated'])
#df['Address'] = df['Address'].str.rsplit(',').str[-1]
#zoo.groupby('animal').mean()

#min_max_downloads = df_year_d[df_year_d['Last Updated'].between(2016, 2018, inclusive=True)].groupby('Last Updated').agg({'Downloads': [np.min, np.max]})
#df1 = df_year_d[df_year_d['Last Updated'].isin([2016,2017,2018])]
#print(df1)
#df1 = df_year_d.groupby(['Last Updated','Category'], as_index=False).sum()
#print(df1)

#df1 = df1.loc[df1.groupby('Last Updated')['Downloads'].agg(['idxmin','idxmax']).stack()]
#print(df1)
#df1.set_index("Last Updated", inplace=True)
#df1=df1.loc[['2016','2017','2018']]
#print(df1)
    df_year_d = df_year_d[df_year_d['Last Updated'].isin([2016,2017,2018])]
#print(df_year_d)
    df1 = df_year_d.groupby(['Last Updated','Category'], as_index=True).sum()
#print(df1)

    df1 = df1.loc[df1.groupby('Last Updated')['Downloads'].agg(['idxmin','idxmax']).stack()].reset_index()
    return df1

#print (q6())
#df1=df_year_d.groupby(['Last Updated','Category']).sum()
#print(df1)
#df1 = df_year_d[df_year_d['Last Updated'].isin([2016,2017,2018])]
#df1 = df_year_d.groupby(['Last Updated','Category'], as_index=False).sum()

#df1 = (df1.sort_values(['Last Updated','Downloads']).groupby('Last Updated', as_index=False).nth([0,-1]))
#print(min_max_downloads)
#(df.groupby(['cluster', 'org'], as_index=False).mean().groupby('cluster')['time'].mean())

#df.groupby(['org']).mean().groupby(['cluster']).mean()
#print(df_year_d)