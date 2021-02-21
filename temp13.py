import pandas as pd 
import numpy as np
def inputthirteen():
    df=pd.read_csv("Sentiment.csv")
    df1=pd.DataFrame(df["App"])
    df1["Pol"]=df["Sentiment_Polarity"]
    df1["Subj"]=df["Sentiment_Subjectivity"]
    df1["Pol"]=pd.to_numeric(df1["Pol"])
    df1["Subj"]=pd.to_numeric(df1["Subj"])
    
    return(df1)
#print(inputthirteen())
def df_13():
    df2=inputthirteen().loc[inputthirteen()["Pol"]==0.4]
    return df2

def corr_13():
    data = inputthirteen()[['Subj','Pol']]
    correlation = data.corr(method='pearson')
    return correlation
# For this kind of data, we generally consider correlations above 0.4 to be relatively strong; correlations between 0.2 and 0.4 are moderate, and those below 0.2 are considered weak.
#The positive correlation means there is a positive relationship between the variables; as one variable increases or decreases, the other tends to increase or decrease with it. The negative correlation means that as one of the variables increases, the other tends to decrease, and vice versa.
#The Pearson correlation coefficient, r, can take a range of values from +1 to -1. A value of 0 indicates that there is no association between the two variables. A value greater than 0 indicates a positive association; that is, as the value of one variable increases, so does the value of the other variable.
#In statistics, the Pearson correlation coefficient, also referred to as Pearson's r, the Pearson product-moment correlation coefficient or the bivariate correlation, is a measure of the linear correlation between two variables X and Y.
#A Pearson correlation is a number between -1 and 1 that indicates the extent to which two variables are linearly related. The Pearson correlation is also known as the “product moment correlation coefficient” (PMCC) or simply “correlation”
