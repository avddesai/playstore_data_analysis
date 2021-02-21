import pandas as pd
def q1():
    df=pd.read_csv('Apps.csv')
    df["Installs"] = df["Installs"].str.replace("\,","")
    df["Installs"] = df["Installs"].str.replace("+","")
    df["Installs"] = pd.to_numeric(df["Installs"])
    #print(df["Installs"])
    sales=df.groupby(['Category'],as_index=True).agg({'Installs':'sum'})
    #print(sales)
    sales_pct=sales.apply(lambda x:100*x/float(x.sum())).reset_index()
    return sales_pct

