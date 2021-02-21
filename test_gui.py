from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import re, pymysql
from temp1 import q1
from temp2 import q2
from temp4 import q4
from pandastable import Table, TableModel
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from temp3 import max1,min1,avg1
from temp5 import q5
from temp6 import q6
from temp9 import q9
from temp13 import df_13,corr_13
from temp7 import n_varies, varies,per
from temp10 import q10a,q10b,q10c
from temp12 import pos_12,neg_12,eqposneg
from temp19 import qy_19
from temp20 import qy_20
from temp14 import list_apps,qy_14
from temp15 import qy_15
from temp8 import qy_8,apps
from temp16 import qy_16
import re
from temp17 import qy_17
#from datetime import datetime
from tkcalendar import Calendar, DateEntry
import csv
from temp18 import uniqcat,uniqinstalls,uniqcontent_r,uniq_genre
import tkinter.messagebox as tm
# This function is used for adjusting window size and making the necessary configuration on start of window
def adjustWindow(window):
    w = 800 # width for the window size
    h = 650 # height for the window size
    ws = screen.winfo_screenwidth() # width of the screen
    hs = screen.winfo_screenheight() # height of the screen
    x = (ws/3) - (w/3) # calculate x and y coordinates for the Tk window
    y = (hs/3) - (h/3)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed
    window.resizable(True, True) # disabling the resize option for the window
    window.configure(background="#adad85")


def closeWin(window):
    window.destroy()

def query(n):
    if(n==1):
        qy1=Toplevel(screen2)
        qy1.title("1st Query")
        adjustWindow(qy1)
        #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
        frame = tk.Frame(qy1)
        frame.pack(fill=BOTH,expand=1)
        
        pt = Table(frame, dataframe=q1(),showtoolbar=True, showstatusbar=True)
        pt.show()
        
        
        
    elif(n==2):

        f=Figure(figsize=(5,5),dpi=100)
        a=f.add_subplot(111)
        a.plot(q2())
        
        
        
    elif(n==3):
        qy3=Toplevel(screen2)
        qy3.title("3rd Query")
        adjustWindow(qy3)
        
        def max_3():
            qy3max=Toplevel(qy3)
            qy3max.title("Maximum Downloads")
            adjustWindow(qy3max)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            frame = tk.Frame(qy3max)
            frame.pack(fill=BOTH,expand=1)
            pt = Table(frame, dataframe=max1(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        def min_3():
            qy3min=Toplevel(qy3)
            qy3min.title("Maximum Downloads")
            adjustWindow(qy3min)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            frame = tk.Frame(qy3min)
            frame.pack(fill=BOTH,expand=1)
            pt = Table(frame, dataframe=min1(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        def avg_3():
            qy3min=Toplevel(qy3)
            qy3min.title("Maximum Downloads")
            adjustWindow(qy3min)
            frame = tk.Frame(qy3min)
            frame.pack(fill=BOTH,expand=1)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            
            pt = Table(frame, dataframe=avg1(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        Label(qy3, text="Select one option", width=15, height=1, font=("Calibri", 10, 'bold'), fg='white', bg='#d9660a').pack()
        Label(qy3, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy3, text='Category with Maximum Downloads',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=max_3,wraplength=150).pack()
        Label(qy3, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy3, text='Category with Minimum Downloads',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=min_3,wraplength=150).pack()
        Label(qy3, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy3, text='Category with Average 2,50,000 downloads',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=avg_3,wraplength=150).pack()
    
    elif(n==4):
        
        f1=Figure(figsize=(7,7),dpi=100).add_subplot(111).plot(q4())
        
    
    
    elif(n==5):
        
        f2=Figure(figsize=(5,5),dpi=100).add_subplot(111).plot(q5())
        
    elif(n==6):
            qy6=Toplevel(screen2)
            qy6.title("Categories with Most and Least downloads")
            adjustWindow(qy6)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            Label(qy6,text="Categories with most and least downloads for 2016,2017,2018",height=1, width=20, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=250).pack(side=TOP,expand=True,fill=tk.BOTH)
            frame = tk.Frame(qy6)
            frame.pack(fill=BOTH,expand=1)
            pt = Table(frame, dataframe=q6(),showtoolbar=True, showstatusbar=True)
            pt.show()
            
    elif(n==7):
            
            qy7=Toplevel(screen2)
            qy7.title("Perctage change in Downloads")
            adjustWindow(qy7)
            Label(qy7,text="Number of apps not varying with devices:",font=("Ariel",15),bg="Red",relief=GROOVE).grid(row=0,column=0)
            T=tk.Text(qy7,width=25,height=1,bg="#FFDBAC",font=("Ariel",15))
            T.grid(row=0,column=1,padx=20, pady=20)
            T.insert(tk.END, n_varies())
            Label(qy7,text="Number of apps varying with devices:",bg="Red",relief=GROOVE,font=("Ariel",15)).grid(row=1,column=0,sticky=W)
            T1=tk.Text(qy7,width=25,height=1,bg="#FFDBAC",font=("Ariel",15))
            T1.grid(row=1,column=1,padx=20, pady=20)
            T1.insert(tk.END, varies())
            
            Label(qy7,text="Percentage change in downloads ",bg="Red",relief=GROOVE,font=("Ariel",15)).grid(row=2,column=0,sticky=W)
            T1=tk.Text(qy7,width=25,height=1,bg="#FFDBAC",font=("Ariel",15))
            T1.grid(row=2,column=1,padx=20, pady=20)
            T1.insert(tk.END, per())
    


    elif(n==8):
            qy8=Toplevel(screen2)
            qy8.title("Findings")
            #qy8.geometry("300x250+650+375")
            adjustWindow(qy8)
            
            Label(qy8, text="Update into the categories and their downloads into database", fg="green", font=("calibri", 14), width='60',height=1, anchor=W, bg='white').pack() 
            def fig8():
                f=Figure(figsize=(5,5),dpi=100)
                a=f.add_subplot(111)
                a.plot(qy_8())
                return
            
            def update():
                category=apps()["Category"]
                installs=apps()["Installs"]
                
                connection = pymysql.connect(host="localhost", user="root", passwd="", database="apps") # database connection
                cursor = connection.cursor()
                for i in range(len(category)):
                    insert_query = "INSERT INTO applist (app,installs) VALUES('"+ str(category[i]) + "', '"+ str(installs[i]) + "' );" # queries for inserting values
                    cursor.execute(insert_query) # executing the queries
                connection.commit() # commiting the connection then closing it.
                connection.close() # closing the connection of the database"""
            def destroy():
                connection = pymysql.connect(host="localhost", user="root", passwd="", database="apps") # database connection
                cursor = connection.cursor()
                destroy_table="TRUNCATE TABLE applist;"
                cursor.execute(destroy_table) # executing the queries
            
                connection.commit() # commiting the connection then closing it.
                connection.close() # closing the connection of the database"""
            
            def showdf8():
                qy8dfshow=Toplevel(qy8)
                qy8dfshow.title("Updated data")
                adjustWindow(qy8dfshow)
                
                #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
                frame = tk.Frame(qy8dfshow)
                frame.pack(fill=BOTH,expand=1)
                pt = Table(frame, dataframe=apps(),showtoolbar=True, showstatusbar=True)
                pt.show()
                return
            
            Button(qy8, text="Stats of Findings", width=40, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=fig8).pack() 
            
            Label(qy8, text="", width=15, height=1, fg='white', bg='white').pack()
            Button(qy8, text='Update into XAMPP and Show updated data', width=40, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=lambda:[showdf8(),update()]).pack() 
            
            
            Label(qy8, text="", width=15, height=1, fg='white', bg='white').pack()
            
            Button(qy8, text="Close window", width=40, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=lambda:[destroy(),closeWin(qy8)]).pack() 
            
            
            
    elif(n==9):
            qy9=Toplevel(screen2)
            qy9.title("Apps with more than 100,000 downloads and 4.1+ ratings")
            adjustWindow(qy9)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            Label(qy9,text="Below is the list of apps",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=120).pack(side=TOP,expand=True,fill=tk.BOTH)
            frame = tk.Frame(qy9)
            frame.pack(fill=BOTH,expand=1)
            Label(qy9,text="We can conclude that the higher ratings for apps consequently leads to their higher downloads",height=1, width=200, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=500).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            pt = Table(frame, dataframe=q9(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        
        
        
    elif(n==10):
        qy10=Toplevel(screen2)
        qy10.title("Query 10")
        adjustWindow(qy10)
            
        def max10():
            qy_10=Toplevel(qy10)
            qy_10.title("Month with max downloads each category")
            adjustWindow(qy_10)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            Label(qy_10,text="Months with max downloads in each category",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=250).pack(side=TOP,expand=True,fill=tk.BOTH)
            
            frame = tk.Frame(qy_10)
            frame.pack(fill=BOTH,expand=1)
            pt = Table(frame, dataframe=q10c(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        def df10():
            qy_10=Toplevel(qy10)
            qy_10.title("Sum of downloads of Mature 17+ vs Teen")
            adjustWindow(qy_10)
            Label(qy_10,text="",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=120).pack(side=TOP,expand=True,fill=tk.BOTH)
            
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            frame = tk.Frame(qy_10)
            frame.pack(fill=BOTH,expand=1)
            Label(qy_10,text="Ratio of teen vs Mature 17+ =",height=1, width=200, font=("Open Sans", 13, 'bold'),wraplength=500).pack(side=TOP,expand=True,fill=tk.BOTH)
            
            Label(qy_10,text=q10b(),height=1, width=200, font=("Open Sans", 13, 'bold'),wraplength=500).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            
            pt = Table(frame, dataframe=q10a(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        
        Label(qy10, text="Select one option", width=15, height=1, font=("Calibri", 10, 'bold'), fg='white', bg='#d9660a').pack()
        Label(qy10, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy10, text='Months with max downloads for each caegory',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=max10,wraplength=150).pack()
        Label(qy10, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy10, text='Ratio of downloads of Teen vs Mature 17+ ',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=df10,wraplength=150).pack()
    


    elif(n==12):
        qy12=Toplevel(screen2)
        qy12.title("12th Query")
        adjustWindow(qy12)
        
        def pos12():
            qy_12=Toplevel(qy12)
            qy_12.title("Most positive sentiments")
            adjustWindow(qy_12)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            Label(qy_12,text="App with most positive sentiments",height=2,width=100,relief=GROOVE,bg='Orange', font=("Open Sans", 13, 'italic'),wraplength=200).pack(side=TOP,fill=tk.BOTH)
            
            T = tk.Text(qy_12, height=1, width=15,bg="#FFDBAC")
            T.pack()
            T.insert(tk.END, pos_12())
            
            
            return
        
        def neg12():
            qy_12=Toplevel(qy12)
            qy_12.title("Most negative sentiments")
            adjustWindow(qy_12)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            Label(qy_12,text="App with most negative sentiments",height=2, width=100,relief=GROOVE, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=200).pack(side=TOP,fill=tk.BOTH)
            T = tk.Text(qy_12, height=1, width=25,bg="#FFDBAC")
            T.pack()
            T.insert(tk.END, neg_12())
            
        def eq_12():
            qy_12=Toplevel(qy12)
            qy_12.title("Apps with equal ratio of positive and negative sentiments")
            adjustWindow(qy_12)
            Label(qy_12,text="",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=120).pack(side=TOP,expand=True,fill=tk.BOTH)
            
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            frame = tk.Frame(qy_12)
            frame.pack(fill=BOTH,expand=1)
            Label(qy_12,text="",height=1, width=200, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=500).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            
            pt = Table(frame, dataframe=eqposneg(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        
        Label(qy12, text="Select one option", width=15, height=1, font=("Calibri", 10, 'bold'), fg='white', bg='#d9660a').pack()
        Label(qy12, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy12, text='App which has managed to generate the most positive sentiments',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=pos12,wraplength=200).pack()
        Label(qy12, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy12, text='App which has managed to generate the most negative sentiments',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=neg12,wraplength=200).pack()
        Label(qy12, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy12, text='Apps which have managed to generate the same ratio of positive and negative sentiments',height=5, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=eq_12,wraplength=200).pack()
        
        
            
    elif(n==13):
        qy13=Toplevel(screen2)
        qy13.title("13th Query")
        adjustWindow(qy13)
        
        def corr13():
            qy_13=Toplevel(qy13)
            qy_13.title("Relation")
            adjustWindow(qy_13)
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            Label(qy_13,text="Correlation Dataframe",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=120).pack(side=TOP,expand=True,fill=tk.BOTH)
            S = tk.Scrollbar(qy_13)
            T = tk.Text((qy_13), height=4, width=150)
            
            frame = tk.Frame(qy_13)
            frame.pack(fill=BOTH,expand=1)
            S.pack(side=tk.RIGHT, fill=tk.Y)
            T.pack(side=tk.LEFT, fill=tk.Y,expand=True)
            S.config(command=T.yview)
            T.config(yscrollcommand=S.set)
            quote = """For this kind of data, we generally consider correlations above 0.4 to be relatively strong; correlations between 0.2 and 0.4 are moderate, and those below 0.2 are considered weak. The positive correlation means there is a positive relationship between the variables; as one variable increases or decreases, the other tends to increase or decrease with it. The negative correlation means that as one of the variables increases, the other tends to decrease, and vice versa. The Pearson correlation coefficient, r, can take a range of values from +1 to -1. A value of 0 indicates that there is no association between the two variables. A value greater than 0 indicates a positive association; that is, as the value of one variable increases, so does the value of the other variable. In statistics, the Pearson correlation coefficient, also referred to as Pearson's r, the Pearson product-moment correlation coefficient or the bivariate correlation, is a measure of the linear correlation between two variables X and Y. A Pearson correlation is a number between -1 and 1 that indicates the extent to which two variables are linearly related. The Pearson correlation is also known as the Product moment correlation coefficient (PMCC) or simply Correlation"""
            T.insert(tk.END, quote)
            pt = Table(frame, dataframe=corr_13(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        def df13():
            qy_13=Toplevel(qy13)
            qy_13.title("Sentiment subjectivity for a sentiment polarity of 0.4")
            adjustWindow(qy_13)
            Label(qy_13,text="",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=120).pack(side=TOP,expand=True,fill=tk.BOTH)
            
            #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
            frame = tk.Frame(qy_13)
            frame.pack(fill=BOTH,expand=1)
            Label(qy_13,text="",height=1, width=200, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=500).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            
            pt = Table(frame, dataframe=df_13(),showtoolbar=True, showstatusbar=True)
            pt.show()
            return
        
        Label(qy13, text="Select one option", width=15, height=1, font=("Calibri", 10, 'bold'), fg='white', bg='#d9660a').pack()
        Label(qy13, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy13, text='Relation between Sentiment Subjectivity and Polarity',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=corr13,wraplength=150).pack()
        Label(qy13, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy13, text='Sentiment subjectivity for a sentiment polarity of 0.4',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=df13,wraplength=150).pack()
    

    elif(n==14):
        qy14 = Toplevel(screen2)
        qy14.title("Apps with sentiments")
        adjustWindow(qy14) # configuring the window
        #l1=list_apps()
        #print (l1)
        #def appc(n):
            #for n in l1:
        Label(qy14,text="",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=120).pack(side=TOP,expand=True,fill=tk.BOTH)
            
        #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
        frame = tk.Frame(qy14)
        frame.pack(fill=BOTH,expand=1)
        Label(qy14,text="",height=1, width=200, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=500).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            
        pt = Table(frame, dataframe=qy_14(),showtoolbar=True, showstatusbar=True)
        pt.show()
        return

    elif(n==15):
        qy15=Toplevel(screen2)
        qy15.title("About the app: 10 Best foods for you")
        adjustWindow(qy15)
        #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
        Label(qy15,text="Below is the stats for the app: 10 Best foods for you",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=200).pack(side=TOP,expand=True,fill=tk.BOTH)
        S = tk.Scrollbar(qy15)
        T = tk.Text((qy15), height=4, width=150)
            
        frame = tk.Frame(qy15)
        frame.pack(fill=BOTH,expand=1)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y,expand=True)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = """From the above stats for the app: '10 Best foods for you', We come to know that the app has got more positive reviews than negative and neutral ones. So we can conclude that the app is surely advisable to launch an app like '10 Best foods for you' as it has high chances of being successful """
        T.insert(tk.END, quote)
        #Label(qy_13,text="For this kind of data, we generally consider correlations above 0.4 to be relatively strong; correlations between 0.2 and 0.4 are moderate, and those below 0.2 are considered weak. The positive correlation means there is a positive relationship between the variables; as one variable increases or decreases, the other tends to increase or decrease with it. The negative correlation means that as one of the variables increases, the other tends to decrease, and vice versa. The Pearson correlation coefficient, r, can take a range of values from +1 to -1. A value of 0 indicates that there is no association between the two variables. A value greater than 0 indicates a positive association; that is, as the value of one variable increases, so does the value of the other variable. In statistics, the Pearson correlation coefficient, also referred to as Pearson's r, the Pearson product-moment correlation coefficient or the bivariate correlation, is a measure of the linear correlation between two variables X and Y. A Pearson correlation is a number between -1 and 1 that indicates the extent to which two variables are linearly related. The Pearson correlation is also known as the Product moment correlation coefficient (PMCC) or simply Correlation",height=1, width=300, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=700).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            
        #df = TableModel.q1()
        #df=TableModel.q1()
        pt = Table(frame, dataframe=qy_15(),showtoolbar=True, showstatusbar=True)
        pt.show()
        return
     
    elif(n==16):
        qy16=Toplevel(screen2)
        qy16.title("About the app: 10 Best foods for you")
        adjustWindow(qy16)
        #canvas = tk.Canvas(qy1, borderwidth=0, background="#ffffff")
        Label(qy16,text="Below is the stats for the apps w.r.t. Months and Installs occured in them",height=1, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white',wraplength=200).pack(side=TOP,expand=True,fill=tk.BOTH)
        S = tk.Scrollbar(qy16)
        T = tk.Text((qy16), height=4, width=150)
            
        frame = tk.Frame(qy16)
        frame.pack(fill=BOTH,expand=1)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y,expand=True)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = """From the above stats for the apps: JULY is the month with highest Installs, so it is the best indicator to the month in which average downloads that an app will generate over the entire year """
        T.insert(tk.END, quote)
        #Label(qy_13,text="For this kind of data, we generally consider correlations above 0.4 to be relatively strong; correlations between 0.2 and 0.4 are moderate, and those below 0.2 are considered weak. The positive correlation means there is a positive relationship between the variables; as one variable increases or decreases, the other tends to increase or decrease with it. The negative correlation means that as one of the variables increases, the other tends to decrease, and vice versa. The Pearson correlation coefficient, r, can take a range of values from +1 to -1. A value of 0 indicates that there is no association between the two variables. A value greater than 0 indicates a positive association; that is, as the value of one variable increases, so does the value of the other variable. In statistics, the Pearson correlation coefficient, also referred to as Pearson's r, the Pearson product-moment correlation coefficient or the bivariate correlation, is a measure of the linear correlation between two variables X and Y. A Pearson correlation is a number between -1 and 1 that indicates the extent to which two variables are linearly related. The Pearson correlation is also known as the Product moment correlation coefficient (PMCC) or simply Correlation",height=1, width=300, font=("Open Sans", 13, 'bold'), bg='Green', fg='white',wraplength=700).pack(side=BOTTOM,expand=True,fill=tk.BOTH)
            
        #df = TableModel.q1()
        #df=TableModel.q1()
        pt = Table(frame, dataframe=qy_16(),showtoolbar=True, showstatusbar=True)
        pt.show()
        return
    elif(n==17):
        
        f2=Figure(figsize=(5,5),dpi=100).add_subplot(111).plot(qy_17())        
    
    elif(n==18):
        qy18=Toplevel(screen2)
        qy18.title("Update")
        adjustWindow(qy18)

        def addApps():
            qy18apps=Toplevel(qy18)
            global pric
            qy18apps.title("Update app dataset")
            adjustWindow(qy18apps)
            def onFrameConfigure(canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))
            canvas = tk.Canvas(qy18apps, borderwidth=0, background="#ffffff")
            frame = tk.Frame(canvas, background="#adad85")
            vsb = tk.Scrollbar(qy18apps, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=vsb.set)
    
            vsb.pack(side="right", fill="y")
            vsb = tk.Scrollbar(qy18apps, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=vsb.set)
    
            vsb.pack(side="bottom", fill="x")

            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((8,12), window=frame, anchor="nw")
    
            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
            
            def enterdb():
                l1=[str(appname.get()),str(category.get()),str(ratings.get()),str(n_review.get()),str(sizes1.get()+sizes2.get()),str(installs.get()),str(types.get()),str("0"+price.get()+"$"),str(c_rating.get()),str(genres.get()),str(T.get("1.0",'end-1c')),str(curr_ver.get()),str(and_ver.get())]
                #print(l1)
                with open("Apps.csv", "a", newline='') as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(l1)
                messagebox.showinfo("Congratulation", "Entry Succesfull",parent=qy18apps) # displaying message for successful entry
                qy18apps.destroy()
            """
            def enter_new_record(entryField):
                found = 0
                for student in entryField:
                    for field in student:
                        if(field.get() == ""): # validating all fields entered or not
                            found = 1
                            break
                if found == 0:
                        for fields in entryField:
                            l1=[str(fields[0].get()),str(fields[1].get()),str(fields[2].get()),str(fields[3].get()),str(fields[4].get()),str(fields[5].get()),str(fields[6].get()),str(fields[7].get()),str(fields[8].get()),str(fields[9].get()),str(fields[10].get()),str(fields[11].get()),str(fields[12].get())]
                            #print(l1)
                            with open("Apps.csv", "a", newline='') as fp:
                                wr = csv.writer(fp, dialect='excel')
                                wr.writerow(l1)
                        messagebox.showinfo("Congratulation", "Entry Succesfull",parent=qy18apps) # displaying message for successful entry
                        qy18apps.destroy()
                else:
                    messagebox.showerror("Error", "Please fill all the details", parent=qy18apps) # displaying message for invalid details
            """
            
            def validate(event , input):
             if( input == "App name"):
                 a = appname.get()
                 if all (x.isalnum() or x.isspace() for x in a) and (len(a)> 0):
                     #tm.showerror("Invalidate!" ,"Registration number has to alphanumeric havinglength between 5 and 20.")
                     #s1.config(state='disabled')
                     #tm.showerror("Correct")
                     droplistCat.configure(state="normal")
                     droplistCat.focus_set()
                     
                 else:
                     appn.delete(0, "end")
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="App name has to alphanumeric and cannot be empty")
            # elif(input=="")
                
                
             elif(input=="Cat"):
                 cat=category.get()
                 if(cat=="" or cat=="--Select a category--"):
                     
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Select a Category name")
                 else:
                     rat.focus_set()
                     rat.configure(state="normal")
             elif(input=="Rating"):
                 r=ratings.get()
                 
                 if re.match('(\d+(\.\d+)?)|(\.?\d+)',r) and len(r) > 0 :
                     #'[+-]?[0-9]+\.[0-9]+'
                     #(\d+(\.\d+)?)|(\.?\d+)
                     #tm.showerror("Invalidate!" ,"Registration number has to alphanumeric havinglength between 5 and 20.")
                     #s1.config(state='disabled')
                     #tm.showerror("Correct")
                     nReview.configure(state="normal")
                     nReview.focus_set()
                 elif (r==""):
                     r="NaN"
                     nReview.configure(state="normal")
                     nReview.focus_set()
                     
                 else:
                     rat.delete(0, "end")
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Ratings can only be int or float, and cannot be empty")
             elif(input=="n_review"):
                 nR=n_review.get()
                 if re.match("^[0-9]*$",nR) and (len(nR)>=0):
                     droplistS.configure(state="normal")
                     droplistS.focus_set()
                 else:
                     nReview.delete(0, "end")
                     #n_review=None
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="No. of reviews can only be int, and cannot be empty")
                
             elif(input=="Size2"):
                  sizeType=sizes2.get()
                  if(sizeType=="M" or sizeType=="k"):
                      s1.config(state="normal")
                      s1.focus_set()
                  elif(sizeType=="Varies with devices"):
                      droplistInstall.config(state="normal")
                      droplistInstall.focus_set()
                  elif(sizeType=="" or sizeType=="--Select the size type--"):
                     
                      tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Select a size type")
                      
                  
             elif(input=="Size1"):
                 size1=sizes1.get()
                 if (size1.isdigit()) and (len(size1)> 0):
                     droplistInstall.configure(state="normal")
                     droplistInstall.focus_set()
                 else:
                    
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Must be digit")
             elif(input=="Paid"):
                  paid.config(state="normal")
             elif(input=="Free"):
                  pric="0"
                  paid.delete(0, "end")
                  paid.config(state="disabled")
                  droplistCR.config(state="normal")
                  droplistCR.focus_set()
             elif(input=="Price"):
                 p=price.get()
                 
                 if re.match('^([0-9]*[1-9][0-9]*(\.[0-9]+)?|[0]+\.[0-9]*[1-9][0-9]*)$',p) and len(p) > 0 :
                     #pric=price.get()+"$"
                     droplistCR.config(state="normal")
                     droplistCR.focus_set()
                 elif (p=="" or p=="0"):
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Cant keep empty or zero")
                     paid.delete(0, "end")
             elif(input=="CR"):
                 cr=c_rating.get()
                 if(cr=="" or cr=='--Select a ContentRating--'):
                     
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message='Select a ContentRating')
                 else:
                     droplistG.focus_set()
                     droplistG.configure(state="normal")
             elif(input=="Genres"):
                 g=genres.get()
                 if(g=="" or g=='--Select the genre--'):
                     
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message='Select Genres')
                 else:
                     date_b.focus_set()
                     date_b.configure(state="normal")
             elif(input=="cver"):
                 c=curr_ver.get()
                 if re.match('(\d+(?:\.\d+)*)',c) and len(c)>0:
                     an_ver.config(state="normal")
                     an_ver.focus_set()
                 elif (c=="" or c=="0"):
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Cant keep empty or zero")
                     curr_ver.delete(0, "end")
                 else:
                     tm.showerror(parent=qy18apps,title="Invalid" ,message="Invalid Input enter only numbers ")
                     curr_ver.delete(0, "end")
                     

             elif(input=="anver"):
                 a=an_ver.get()
                 if re.match('(\d+(?:\.\d+)*)',a) and len(a)>0:
                     #an_ver.config(state="normal")
                     b1.focus_set()
                 elif (a=="" or a=="0"):
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Cant keep empty or zero")
                     an_ver.delete(0, "end")
                 else:
                     tm.showerror(parent=qy18apps,title="Invalid" ,message="Invalid Input enter only numbers ")
                     an_ver.delete(0, "end")
                     
             elif(input=="Installs"):
                 inst=installs.get()
                 if(inst=="" or inst=="--Select installs--"):
                     
                     tm.showerror(parent=qy18apps,title="Invalidate!" ,message="Select installs")
                 else:
                     rf.focus_set()
                     rf.configure(state="normal")
                     rp.configure(state="normal")
             
                 
              
            
                     #s1.config(state='normal')
            global appname,category,sizes1,sizes2, ratings,n_review, installs, types,genres,c_rating,and_ver,curr_ver,price,dates # making all entry field variable global
            pric=StringVar()
            appname = StringVar()
            ratings = StringVar()
            installs = StringVar()
            genres = StringVar()
            c_rating=StringVar()
            sizes1=StringVar()
            sizes2=StringVar()
            dates = StringVar()
            n_review = StringVar()
            types = StringVar()
            category = StringVar()
            price=StringVar()
            curr_ver=StringVar()
            and_ver=StringVar()
            Label(frame,text="Update your own data into Apps csv Dataset",height=3, width=75, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white').grid(row=0,column=0)
            Label(frame, text="", bg="#adad85", width='60', height=2).grid(row=1,column=0)
            #Label(frame, text="", bg='white').pack()
            Label(frame, text="App Name", font=("Open Sans", 12, 'bold'), fg='black',bg='white').grid(row=2,column=0,sticky=W)
            Label(frame, text="Category", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=3,column=0,sticky=W)
            droplistCat = OptionMenu(frame, category, *uniqcat())
            droplistCat.config(width=18)
            category.set('--Select a category--')
            droplistCat.place(x=300,y=120)
            droplistCat.bind("<Return>", lambda event: validate(event, "Cat"))
            #droplistCat.bind("<Tab>", lambda event: validate(event, "Cat"))
            droplistCat.configure(state="disabled")
            droplistCR = OptionMenu(frame, c_rating, *uniqcontent_r())
            droplistCR.config(width=18)
            c_rating.set('--Select a ContentRating--')
            droplistCR.place(x=300,y=310)
            droplistCR.bind("<Return>", lambda event: validate(event, "CR"))
            droplistCR.bind("<Tab>", lambda event: validate(event, "CR"))
            droplistCR.configure(state="disabled")
            droplistInstall = OptionMenu(frame, installs, *uniqinstalls())
            droplistInstall.config(width=18)
            installs.set('--Select installs--')
            droplistInstall.place(x=300,y=233)
            droplistInstall.bind("<Return>", lambda event: validate(event, "Installs"))
            droplistInstall.bind("<Tab>", lambda event: validate(event, "Installs"))
            droplistInstall.configure(state="disabled")
            droplistG = OptionMenu(frame, genres, *uniq_genre())
            droplistG.config(width=18)
            genres.set('--Select the genre--')
            droplistG.place(x=300,y=340)
            droplistG.bind("<Return>", lambda event: validate(event, "Genres"))
            droplistG.bind("<Tab>", lambda event: validate(event, "Genres"))
            droplistG.configure(state="disabled")
            sizeList=['M','k','Varies with devices']
            rf=Radiobutton(frame, text="Free", variable=types, value="Free")
            rf.place(x=300,y=265)
            rf.configure(state="disabled")
            rf.bind("<Button-1>", lambda event: validate(event, "Free"))
            rp=Radiobutton(frame, text="Paid", variable=types, value="Paid")
            rp.place(x=360,y=265)
            rp.bind("<Button-1>", lambda event: validate(event, "Paid"))
            rp.configure(state="disabled")
            
            appn=Entry(frame, textvar=appname)
            appn.place(x=300,y=95)
            appn.bind("<Return>", lambda event: validate(event, "App name"))
            appn.bind("<Tab>", lambda event: validate(event, "App name"))
            appn.focus_set()
            droplistS = OptionMenu(frame, sizes2, *sizeList)
            droplistS.config(width=18)
            sizes2.set('--Select the size type--')
            droplistS.place(x=300,y=200)
            droplistS.bind("<Return>", lambda event: validate(event, "Size2"))
            droplistS.bind("<Tab>", lambda event: validate(event, "Size2"))
            droplistS.configure(state="disabled")
            s1=Entry(frame, textvar=sizes1)
            s1.place(x=475,y=200)
            s1.bind("<Return>", lambda event: validate(event, "Size1"))
            s1.bind("<Tab>", lambda event: validate(event, "Size1"))
            s1.configure(state="disabled")
            
            #if ((sizes2=='M') | (sizes2=='k')):
            
            
            nReview=Entry(frame, textvar=n_review)
            nReview.place(x=300,y=177)
            nReview.configure(state="disabled")
            nReview.bind("<Return>", lambda event: validate(event, "n_review"))
            nReview.bind("<Tab>", lambda event: validate(event, "n_review"))
            rat=Entry(frame, textvar=ratings)
            rat.place(x=300,y=155)
            #rat.grid(row=4,column=1,sticky=W)
            rat.bind("<Return>", lambda event: validate(event, "Rating"))
            rat.bind("<Tab>", lambda event: validate(event, "Rating"))
            rat.configure(state="disabled")
            #quote=""
        #cal.see(datetime.date(year=2016, month=2, day=5))
            def datebox1():
                def print_sel():
                    quote=(cal.selection_get())
                    s = datetime.datetime.strptime(str(quote), "%Y-%m-%d")
                    T.delete('1.0', END)
                    #T.insert(tk.END, "")
                    quote1=s.strftime('%B %d, %Y')
                    T.insert(tk.END, quote1)
                    #return quote1
                    
                dateb = tk.Toplevel(qy18apps)
    
                import datetime
                today = datetime.date.today()
    
                mindate = datetime.date(year=1950, month=1, day=1)
                maxdate = today + datetime.timedelta(days=10000)
        #print(mindate, maxdate)
    
                cal = Calendar(dateb, font="Arial 14", selectmode='day', locale='en_US',mindate=mindate, maxdate=maxdate, disabledforeground='red',cursor="hand1", year=2020, month=1, day=17)
                cal.pack(fill="both", expand=True)
                ttk.Button(dateb, text="Select date", command=print_sel).pack()
            #quote=datebox.print_sel()
                #return print_sel()
                #command=lambda:[print_sel(),closeWin(dateb)]
            date_b=Button(frame,text="Enter date",command=datebox1)
            date_b.place(x=300,y=375)
            date_b.bind("<Return>", lambda event: validate(event, "date"))
            date_b.bind("<Tab>", lambda event: validate(event, "date"))
            date_b.configure(state="disabled")
            T=Text(frame,height=1,width=15)
            T.place(x=500,y=375)
            
            #Entry(frame, textvar=dates).grid(row=12,column=1)
            c_ver=Entry(frame, textvar=curr_ver)
            c_ver.place(x=300,y=400)
            c_ver.bind("<Return>", lambda event: validate(event, "cver"))
            c_ver.bind("<Tab>", lambda event: validate(event, "cver"))
            #c_ver.configure(state="disabled")
            an_ver=Entry(frame, textvar=and_ver)
            an_ver.place(x=300,y=435)
            an_ver.bind("<Return>", lambda event: validate(event, "anver"))
            an_ver.bind("<Tab>", lambda event: validate(event, "anver"))
            an_ver.configure(state="disabled")
            paid=Entry(frame, textvar=price)
            paid.place(x=300,y=290)
            paid.config(state='disabled')
            paid.bind("<Return>", lambda event: validate(event, "Price"))
            paid.bind("<Tab>", lambda event: validate(event, "Price"))
            Label(frame, text="Ratings", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=4,column=0,sticky=W)
            Label(frame, text="  Number of reviews  ", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=5,column=0,sticky=W)
            Label(frame, text="Size in M/k", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=6,column=0,sticky=W)
            Label(frame, text="Installs", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=7,column=0,sticky=W)
            Label(frame, text="Type", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=8,column=0,sticky=W)
            Label(frame, text="Price", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=9,column=0,sticky=W)
            Label(frame, text="Content Rating", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=10,column=0,sticky=W)
            Label(frame, text="Genres", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=11,column=0,sticky=W)
            Label(frame, text="Last Updated", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=13,column=0,sticky=W)
            Label(frame, text="Current Version", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=14,column=0,sticky=W)
            Label(frame, text="Android Version", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=15,column=0,sticky=W)
            #Label(frame, text="Hello", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=14,column=3,sticky=W)
            
            #entryField = list()
            #temp = list()
            """
            if (types.get()==1):
                types='Free'
            elif (types.get()==2):
                types='Paid'
            """
            #print("a")
            """
            for j in range(13):
                e = Entry(frame, width=14)
                e.grid(row=3,column=j, padx=(5,0), pady=(0,25))
                temp.append(e)
            entryField.append(temp)
            #print(temp)
            """
            b1=Button(frame, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=enterdb)
            b1.grid(row=18,column=0,sticky=W)
        #command=lambda: enter_new_record(entryField)
            #s1.config(state='disabled')
            return
        
        def addSentiments():
            qy18sent=Toplevel(qy18)
            global n
            qy18sent.title("Update Sentiments dataset")
            adjustWindow(qy18sent)
            def onFrameConfigure(canvas):
                canvas.configure(scrollregion=canvas.bbox("all"))
            canvas = tk.Canvas(qy18sent, borderwidth=0, background="#ffffff")
            frame = tk.Frame(canvas, background="#ffffff")
            vsb = tk.Scrollbar(qy18sent, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=vsb.set)
    
            vsb.pack(side="bottom", fill="x")
            canvas.pack(side="left", fill="both", expand=True)
            canvas.create_window((4,4), window=frame, anchor="n")
    
            frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
            
            def enterdb():
                l1=[str(appsent.get()),str(trev.get()),str(sents.get()),str(sentP.get()),str(sentS.get())]
                #print(l1)
                with open("Sentiment.csv", "a", newline='') as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(l1)
                messagebox.showinfo("Congratulation", "Entry Succesfull",parent=qy18sent) # displaying message for successful entry
                qy18sent.destroy()
            
            
            
            
            def validate(event , input):
                if( input == "App name"):
                     a = appsent.get()
                     if all (x.isalnum() or x.isspace() for x in a) and (len(a)> 0):
                         t_review.configure(state="normal")
                         t_review.focus_set()
                         
                     else:
                         appS.delete(0, "end")
                         tm.showerror(parent=qy18sent,title="Invalidate!" ,message="App name has to alphanumeric and cannot be empty")
                elif(input=="TReview"):
                     t = trev.get()
                     if all (x.isalnum() or x.isspace() for x in t) and (len(t)> 0):
                         #tm.showerror("Invalidate!" ,"Registration number has to alphanumeric havinglength between 5 and 20.")
                         #s1.config(state='disabled')
                         #tm.showerror("Correct")
                         sent.configure(state="normal")
                         sent.focus_set()
                         
                     else:
                         t_review.delete(0, "end")
                         tm.showerror(parent=qy18sent,title="Invalidate!" ,message="Translated Review has to alphanumeric and cannot be empty")
                elif(input=="Sent"):
                    s=sents.get()
                    if(s=="Positive" or s=="Negative" or s=="Neutral" or s=="nan"):
                        if s=="Neutral":
                            #val=0
                            #print(val)
                            sentPol.configure(state="normal")
                            sentPol.delete(0,"end")
                            sentPol.insert(0,"0")
                            #sentP.get()="0"
                            
                        
                            
                            sentSubj.focus_set()
                            sentSubj.configure(state="normal")
                            
                        elif s=="Negative":
                            sentPol.configure(state="normal")
                            sentPol.insert(0,-1)         
                            
                        else:
                            sentPol.focus_set()
                            sentPol.configure(state="normal")
                            
                    elif(s=="" or s=="--Select the sentiment type--"):
                        
                        
                        tm.showerror(parent=qy18sent,title="Invalidate!" ,message="Select something")
                elif(input=="SentSubj"):
                    sS=sentS.get()
                    if(sS.isdigit()):
                        submitButton.focus_set()
                    elif(sS==""):
                        sentSubj.delete(0, "end")
                        tm.showerror(parent=qy18sent,title="Invalidate!" ,message="Type numeric value !")
                
                    else:
                        sentSubj.delete(0, "end")
                        tm.showerror(parent=qy18sent,title="Invalidate!" ,message="Type numeric value !")
                elif(input=="SentPol"):
                    sP=sentP.get()
                    if(sP.isdigit()):
                        sentSubj.focus_set()
                        sentSubj.configure(state="normal")
                    elif(sP==""):
                        sS.delete(0, "end")
                        tm.showerror(parent=qy18sent,title="Invalidate!" ,message="Type numeric value !")
                    else:
                        sS.delete(0, "end")
                        tm.showerror(parent=qy18sent,title="Invalidate!" ,message="Type a number")
                            
                            
                    
                        
                     
                        
                        
                
            
            global appsent,trev,sents,sentP, sentS 
           
            appsent=StringVar()
            trev=StringVar()
            sents=StringVar()
            sentP=StringVar()
            sentS=StringVar()
            SentList={"Positive","Negative","Neutral"}
            
            Label(frame,text="Update your own data into Sentiment csv Dataset",height=3, width=100, font=("Open Sans", 13, 'italic'), bg='Orange', fg='white').grid(row=0, sticky=W, columnspan=4)
            Label(frame, text="", bg='white', width='60', height='18').place(x=0, y=127)
            Label(frame, text="", bg='white').grid(row=1,column=0)
            Label(frame, text="App Name", font=("Open Sans", 12, 'bold'), fg='black',bg='white').grid(row=2,column=0, pady=(5,5))
            Label(frame, text="Translated Review", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=2,column=1, pady=(5,5))
            Label(frame, text="Sentiments", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=2,column=2, pady=(5,5))
            Label(frame, text="  Sentiment Polarity  ", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=4,column=0, pady=(5,5))
            Label(frame, text="Sentiment Subjectivity", font=("Open Sans", 12, 'bold'), fg='black', bg='white').grid(row=4,column=1,padx=(5,5), pady=(5,5))
#            entryField = list()
#            temp = list()
#            for j in range(5):
#                e = Entry(frame, width=14)
#                e.grid(row=3,column=j, padx=(5,0), pady=(0,25))
#                temp.append(e)
#            entryField.append(temp)
#            print(temp)
            appS = Entry(frame, width=14,textvar=appsent)
            appS.grid(row=3,column=0, padx=(1,0), pady=(0,25))
            appS.bind("<Return>", lambda event: validate(event, "App name"))
            appS.bind("<Tab>", lambda event: validate(event, "App name"))
            #appS.configure(state="disabled")
            t_review = Entry(frame, width=14,textvar=trev)
            t_review.grid(row=3,column=1, padx=(1,0), pady=(0,25))
            t_review.bind("<Return>", lambda event: validate(event, "TReview"))
            t_review.bind("<Tab>", lambda event: validate(event, "TReview"))
            t_review.configure(state="disabled")
            sent = OptionMenu(frame, sents, *SentList)
            sent.config(width=22)
            sents.set('--Select the sentiment type--')
            sent.grid(row=3,column=2, padx=(1,0), pady=(0,25))
            sent.bind("<Return>", lambda event: validate(event, "Sent"))
            sent.bind("<Tab>", lambda event: validate(event, "Sent"))
            sent.configure(state="disabled")
            sentPol = Entry(frame, width=14,textvar=sentP)
            sentPol.grid(row=5,column=0, padx=(1,0), pady=(0,25))
            sentPol.bind("<Return>", lambda event: validate(event, "SentPol"))
            sentPol.bind("<Tab>", lambda event: validate(event, "SentPol"))
            sentPol.configure(state="disabled")
            sentSubj = Entry(frame, width=14,textvar=sentS)
            sentSubj.grid(row=5,column=1, padx=(1,0), pady=(0,25))
            sentSubj.bind("<Return>", lambda event: validate(event, "SentSubj"))
            sentSubj.bind("<Tab>", lambda event: validate(event, "SentSubj"))
            sentSubj.configure(state="disabled")
            
            
            submitButton=Button(frame, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=enterdb)
        #command=lambda: enter_new_record(entryField)
            submitButton.grid(row=7,columnspan=1,column=0, pady=(15,0))
            return
        Label(qy18, text="Select one option", width=15, height=1, font=("Calibri", 10, 'bold'), fg='white', bg='#d9660a').pack()
        Label(qy18, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy18, text='Update Apps dataset',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=addApps,wraplength=150).pack()
        Label(qy18, text="", width=15, height=1, fg='white', bg='white').pack()
        Button(qy18, text='Update sentiments dataset',height=4, width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=addSentiments,wraplength=150).pack()
        
    
    elif(n==19):
        f=Figure(figsize=(5,5),dpi=100)
        a=f.add_subplot(111)
        a.plot(qy_19())
        
        
    elif(n==20):
        
        f=Figure(figsize=(5,5),dpi=100)
        a=f.add_subplot(111)
        a.plot(qy_20())
        
        


def home_screen():
    global screen2
    query_list=["1. What is the percentage download in each category on the playstore.","2. How many apps have managed to get the following number of downloads","3. Which category of apps have managed to get the most,least and an average of 2,50,000 downloads atleast.","4.Which category of apps have managed to get the highest maximum average ratings from the users.Display the result using suaitable visualization tool(s) ","5. What is the number of installs for the following app sizes.","6. For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads","7. All those apps , whose android version is not an issue and can work with varying devices ,what is the percentage increase or decrease in the downloads.","8. Amongst sports, entertainment,social media,news,events,travel and games,which is the category of app that is most likely to be downloaded in the coming years, kindly make a prediction and back it with suitable findings","9. All apps with over 1,00,000 downloads and an average rating of 4.1 and above? And co-relation to the number of downloads and the ratings received.","10.In all the years which month has the maximum downloads for each of the category. What is the ratio of downloads for the app teen versus mature17+","11.Which quarter of which year has generated the highest number of install for each app?","12.Which of all the apps given have managed to generate the most positive and negative sentiments.Also figure out the app which has generated approximately the same ratio for positive and negative sentiments.","13.Study and find out the relation between the Sentiment-polarity and sentiment-subjectivity of all the apps. What is the sentiment subjectivity for a sentiment polarity of 0.4.","14.Generate an interface where the client can see the reviews categorized as positive.negative and neutral ,once they have selected the app from a list of apps available for the study.","15.Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these apps?","16.Which month(s) of the year , is the best indicator to the avarage downloads that an app will generate over the entire year?","17.Does the size of the App influence the number of installs that it gets ? if,yes the trend is positive or negative with the increase in the app size.","18.Provide an interface to add new data to both the datasets provided.The data needs to be added to the excel sheets.","19. Visualization of app ratings vs their number of downloads ","20. Find out Number of installs of apps w.r.t. their number of reviews"]
    screen2 = Toplevel(screen)
    screen2.title("Select one query")
    adjustWindow(screen2) # configuring the window
    def onFrameConfigure(canvas):
    
        canvas.configure(scrollregion=canvas.bbox("all"))
    
    def populate(frame):
        for i in range(len(query_list)):
            tk.Label(frame, text=query_list[i], width='80',anchor=W,relief=GROOVE, height="4", font=("Calibri", 10, 'bold'), fg='black', bg='Orange',wraplength=500).grid(row=i,column=0,sticky=W)
            #l2=Label(text="\n", bg='white')
            #l2.grid(row=i+1,column=0)
            tk.Button(frame, text='Select query', width='15', font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=lambda c=i:query(c+1)).grid(row=i,column=1,sticky=W)
        #tk.Button(frame,Text="Go back",width=10,font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command="").grid(row=i+1,column=1,sticky=w)

    canvas = tk.Canvas(screen2, borderwidth=0, background="#ffffff")
    frame = tk.Frame(canvas, background="#adad85")
    vsb = tk.Scrollbar(screen2, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")
    
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    
    populate(frame)
    
def register():
    global screen1, fullname, email, password, repassword, university, gender, tnc # making all entry field variable global
    fullname = StringVar()
    email = StringVar()
    password = StringVar()
    repassword = StringVar()
    university = StringVar()
    gender = IntVar()
    tnc = IntVar()
    screen1 = Toplevel(screen)
    screen1.title("Registration")
    adjustWindow(screen1) # configuring the window
    Label(screen1, text="Enter your Registration details ", width='32', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='Green').place(x=0, y=0)
    Label(screen1, text="", bg='#174873', width='100', height='17').place(x=45, y=120)
    Label(screen1, text="Full Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=150, y=160)
    Entry(screen1, textvar=fullname).place(x=300, y=160)
    Label(screen1, text="Email ID:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=150, y=210)
    Entry(screen1, textvar=email).place(x=300, y=210)
    Label(screen1, text="Gender:",width=50, font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=150, y=260)
    Radiobutton(screen1, text="Male", variable=gender, value=1).place(x=300, y=260)
    Radiobutton(screen1, text="Female", variable=gender, value=2).place(x=370, y=260)
    Label(screen1, text="University:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=150, y=310)
    list1 = ['Mumbai University', 'Savitribai Phule Pune Univeristy','Gujarat Technological University', 'JNTU Kakinada', 'University of Delhi', 'Anna University']
    droplist = OptionMenu(screen1, university, *list1)
    droplist.config(width=17)
    university.set('--select your university--')
    droplist.place(x=300, y=305)
    Label(screen1, text="Password:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=150, y=360)
    Entry(screen1, textvar=password, show="*").place(x=300, y=360)
    Label(screen1, text="",width=78,height=5, font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=45, y=380)
    
    Label(screen1, text="Re-Password:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=150, y=410)
    entry_4 = Entry(screen1, textvar=repassword, show="*")
    entry_4.place(x=300, y=410)
    Checkbutton(screen1, text="I accept all terms and conditions", variable=tnc, bg='#174873', font=("Open Sans", 9, 'bold'), fg='brown').place(x=175, y=450)
    Button(screen1, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white', command=register_user).place(x=170, y=490)

def register_user():
    if fullname.get() and email.get() and password.get() and repassword.get() and gender.get(): # checking for all empty values in entry field
        if university.get() == "--select your university--": # checking for selection of university
            Label(screen1, text="Please select your university", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570)
            return
        else:
            if tnc.get(): # checking for acceptance of agreement
                if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email.get()): # validating the email
                    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password.get()):
                        if password.get() == repassword.get(): # checking both password match or not
                            # if u enter in this block everything is fine just enter the values in database
                            gender_value = 'male'
                            if gender.get() == 2:
                                gender_value = 'female'
                            connection = pymysql.connect(host="localhost", user="root", passwd="", database="playstore") # database connection
                            cursor = connection.cursor()
                            insert_query = "INSERT INTO registerdetails (fullname, email, password, gender, university) VALUES('"+ fullname.get() + "', '"+ email.get() + "', '"+ password.get() + "', '"+ gender_value + "', '"+ university.get() + "' );" # queries for inserting values
                            cursor.execute(insert_query) # executing the queries
                            connection.commit() # commiting the connection then closing it.
                            connection.close() # closing the connection of the database
                            Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=400, y=500) # printing successful registration message
                            Button(screen1, text='Proceed to Login ->', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen1.destroy).place(x=570, y=500) # button to navigate back to login page
                        else:
                            global L1
                            L1=Label(screen1, text="Password does not match", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white')
                            L1.place(x=500, y=500)
                            
                            return
                    else:
                        global LP
                        LP=Label(screen1, text="Password must contain: At least 8 characters, Must be restricted to 1 uppercase letters: A-Z, Lowercase letters: a-z, Numbers: 0-9 and Any of the special characters: @#$%^&+=", fg="red", font=("calibri", 11),height=3, width=80,wraplength=600, anchor=W, bg='green')
                        LP.place(x=0, y=570)
                        L1.destroy()
                        
                        return
                else:
                    global L2
                    L2=Label(screen1,text="Please enter valid email id", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white')
                    L2.place(x=500, y=500)
                    LP.destroy()
                    return
                    #Password must contain:1. At least 8 characters Must be restricted to 1 uppercase letters: A-Z, lowercase letters: a-z, numbers: 0-9, any of the special characters: @#$%^&+=
            else:
                global L3
                L3=Label(screen1, text="Please accept the agreement", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white')
                L3.place(x=500, y=500)
                LP.destroy()
                return
    else:
        global L4
        L4=Label(screen1, text="Please fill all the details", fg="red",font=("calibri", 11), width='30', anchor=W, bg='white')
        L4.place(x=500, y=500)
        LP.destroy()
        return


def login_verify():
    global studentID
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="playstore") # database connection
    cursor = connection.cursor()
    select_query = "SELECT * FROM registerdetails where email = '" + username_verify.get() + "' AND password = '" + password_verify.get() + "';" # queries for retrieving values
    cursor.execute(select_query) # executing the queries
    student_info = cursor.fetchall()
    connection.commit() # commiting the connection then closing it.
    connection.close() # closing the connection of the database
    if student_info:
        messagebox.showinfo("Congratulation", "Login Succesfull") # displaying message for successful login
        #studentID = student_info[0][0]
        #home_screen(student_info) # opening welcome window
        home_screen()
    else:
        messagebox.showerror("Error", "Invalid Username or Password") # displaying message for invalid details


def main_screen():
    global screen, username_verify, password_verify
    screen = Tk() # initializing the tkinter window
    username_verify = StringVar()
    password_verify = StringVar()
    screen.title("GOOGLE PLAYSTORE APPS STUDY ") # mentioning title of the window
    adjustWindow(screen) # configuring the window
    Label(screen, text="PLAYSTORE APP ANALYTICS", width="500", height="2", font=("Calibri", 22, 'bold'), fg='white', bg='green').pack()
    Label(text="", bg='white').pack() # for leaving a space in between
    Label(screen, text="", bg='#174873',width='150', height='17').place(x=0, y=120) # blue background in middle of window
    Label(screen, text="Please enter login credentials", bg='#174873', fg='white').pack()
    Label(screen, text="", bg='#174873').pack() # for leaving a space in between
    Label(screen, text="USERNAME * ", font=("Open Sans", 10, 'bold'), bg='#174873', fg='white').pack()
    Entry(screen, textvar=username_verify).pack()
    Label(screen, text="", bg='#174873').pack() # for leaving a space in between
    Label(screen, text="PASSWORD * ", font=("Open Sans", 10, 'bold'), bg='#174873', fg='white').pack()
    Entry(screen, textvar=password_verify, show="*").pack()
    Label(screen, text="", bg='#174873').pack() # for leaving a space in between
    Button(screen, text="LOGIN", bg="#e79700", width=15, height=1, font=("Open Sans", 13, 'bold'), fg='white', command=login_verify).pack()
    Label(screen, text="", bg='#174873').pack() # for leaving a space in between
    Button(screen, text="New User? Register Here", height="2", width="30", bg='#e79700', font=("Open Sans", 10, 'bold'), fg='white', command=register).pack()
    screen.mainloop()
main_screen()