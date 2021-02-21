import pandas as pd
import seaborn as sns 
from plotly.offline import init_notebook_mode
import matplotlib.pyplot as plt
df_reviews = pd.read_csv("Sentiment.csv")
df_apps = pd.read_csv("Apps.csv")
df_apps["Installs"] = df_apps["Installs"].str.replace(",","")
df_apps["Installs"] = df_apps["Installs"].str.replace("+","")
df_apps["Installs"] = pd.to_numeric(df_apps["Installs"],errors='coerce')

def apps():
    #categories = list(df_apps["Category"].unique())
    #print("There are {0:.0f} categories".format(len(categories)-1))
    #print(categories)
    sales=df_apps.groupby(['Category'],as_index=False).agg({'Installs':'sum'})
    sales=sales.sort_values('Installs',ascending=False)
    return sales
def qy_8():
    #matplotlib inline
    init_notebook_mode(connected=True)
    
    
    plt.figure(figsize=(16, 9.5))
    genres = df_apps["Category"].value_counts()[:35]
    #ax = sns.barplot(x=genres.values, y=genres.index, palette="PuBuGn_d")
    ax = sns.barplot(x=genres.values, y=genres.index, palette="PuBuGn_d")
    return ax


#print(apps())
#corrmat=df_apps.corr()
#f,ax=plt.subplots(figsize=(9,8))
#sns.heatmap(corrmat,ax=ax,cmap="Blues",linewidths=0.1)
