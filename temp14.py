import numpy as np
import pandas as pd 
import tkinter as tk
from tkinter import *
#import tkSimpleDialog
from tkinter import messagebox
def inputfourteen():
    df=pd.read_csv("Sentiment.csv")
    df1=pd.DataFrame(df["App"])
    df1["Sent"]=df["Sentiment"]
    df1["TR"]=df["Translated_Review"]
    
    return(df1)

def qy_14():
    a=inputfourteen()
    #df1 = a.groupby(['App','Sent']).sum()
    #df1=a.groupby(['App','Sent'])['TR'].unique()
    #print(df1)
    #print("No. of different apps",len(a))
    #df1=pd.DataFrame(df1).reset_index()
    return a
#print(qy_14())
#print(type(qy_14()))
def list_apps():
    df1=inputfourteen()
    #list_apps=df1['App'].unique()
    list_apps=df1['App']
    list_apps=df1.groupby('App')['Sent'].apply(lambda group_series: group_series.tolist()).reset_index()
    return list_apps

#print (list_apps())
#app=lambda app_name:df1.loc[df1['App']==app_name]
#print(app('Houzz Interior Design Ideas'))

"""root=Tk()
root.title("List of apps to select")
root.geometry("600x400+100+100")
def onFrameConfigure(canvas):
    
    canvas.configure(scrollregion=canvas.bbox("all"))
    
def populate(frame):
    for i in range(len(list_apps)):
        tk.Label(frame, text=list_apps[i], width='80',anchor=W,relief=GROOVE, height="4", font=("Calibri", 10, 'bold'), fg='black', bg='Green',wraplength=500).grid(row=i,column=0,sticky=W)
        #l2=Label(text="\n", bg='white')
        #l2.grid(row=i+1,column=0)
        tk.Button(frame, text='Select app', width='15', font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command="").grid(row=i,column=1,sticky=W)
    
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
frame = tk.Frame(canvas, background="#ffffff")
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
populate(frame)
#for i in range(len(list_apps)):
#    Label(root,text=list_apps[i],bg="black",fg="white").grid(row=i,column=0)

root.mainloop()
""" 