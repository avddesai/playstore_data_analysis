import matplotlib.pyplot as plt
import pandas as pd
def q2():
    df=pd.read_csv('Apps.csv')
    df["Installs"] = df["Installs"].str.replace(",","")
    df["Installs"] = df["Installs"].str.replace("+","")
    df["Installs"] = pd.to_numeric(df["Installs"])
    hist_plot=plt.hist(df["Installs"],bins=[10000,50000,150000,500000,5000000,10000000],rwidth=0.75,color='g')
    hist_plot=plt.title("Number of downloads")
    hist_plot=plt.xlabel("No of Installations")
    hist_plot=plt.ylabel("No of Apps")
    return hist_plot
    

