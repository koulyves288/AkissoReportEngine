import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('agg')
def generate_department_excel_chart(pivot_table,department):
    # Reset index to make 'Date' a regular column
    pivot_table.reset_index(inplace=True)
    plt.figure(figsize=(20, 10))
    # Plotting the data
    #pivot_table.plot(x='Date', y=['Sum of Retard', 'Sum of Depart anticipe'], kind='line')
    plt.xticks(fontsize=10)
    dates=pivot_table['Date'].values
    retard=pivot_table['Sum of Retard'].values
    depart=pivot_table['Sum of Depart anticipe'].values
    # Add labels and title
    plt.plot(dates,retard,'ro-',label='Sum of retard')
    plt.plot(dates,depart,'go-',label='Sum of depart anticipe')
    plt.xlabel('Dates',fontsize=20)
    plt.ylabel('Retard and depart anticipe',fontsize=20)
    plt.title(department+' Tendance de Retard and Depart anticipe',fontsize=20)
    plt.legend(["Sum of Retard", "Sum of Depart anticipe"], loc="upper left")
    
    # zip joins x and y coordinates in pairs
    for x,y in zip(dates,retard):

        label = "{:.1f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    for x,y in zip(dates,depart):

        label = "{:.1f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y-1), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    plt.xticks(np.arange(len(dates)),dates,rotation =45)
    #save fiile on pdf
    plt.savefig("reports/bydepartment/"+department+".pdf", format='pdf')
    # Show the plot
    #plt.show()
    # Close the plot
    plt.close()

def generate_department_employee_excel_chart(pivot_table,department):
    # Reset index to make 'Date' a regular column
    pivot_table.reset_index(inplace=True)

    plt.figure(figsize=(20, 12))
    
    # Plotting the data
    #plt.figure()
    #pivot_table.plot(x='Name', y=['Sum of Retard', 'Sum of Depart anticipe'], kind='line')
    plt.xticks(fontsize=10)
    names=pivot_table['Name'].values
    retard=pivot_table['Sum of Retard'].values
    depart=pivot_table['Sum of Depart anticipe'].values
    plt.bar(names, retard, color ='red', width = 0.2)
    plt.bar(names, depart, color ='green', width = 0.2)
    #plt.plot(names,retard,'ro-',label='Sum of retard')
    #plt.plot(names,depart,'go-',label='Sum of depart anticipe')
    plt.xlabel('Employees',fontsize=20)
    plt.ylabel('Retard and depart anticipe',fontsize=20)
    plt.title(department+' Retard and Depart anticipe Count Over Time',fontsize=20)
    plt.legend(["Sum of Retard", "Sum of Depart anticipe"], loc="upper left")
    # zip joins x and y coordinates in pairs
    for x,y in zip(names,retard):

        label = "{:.1f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y+1), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
    for x,y in zip(names,depart):

        label = "{:.1f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    #print(names)
    plt.xticks(np.arange(len(names)),names,rotation =45)
    #plt.yticks(np.arange(len(retard)+(len(retard)/2)))
    #axo.set_xlabel('x-axis', fontsize = 12) 
    # Add labels and title
    
   
  
    
    
   
    #save fiile on pdf
    plt.savefig("reports/byemployee/"+department+".pdf", format='pdf')
    # Show the plot
    #plt.show()
    # Close the plot
    plt.close()

def generate_department_retard_excel_chart(pivot_table,department):
    # Reset index to make 'Date' a regular column
    pivot_table.reset_index(inplace=True)
    plt.figure(figsize=(20, 10))
    # Plotting the data
    #pivot_table.plot(x='Date', y=['Sum of Retard', 'Sum of Depart anticipe'], kind='line')
    plt.xticks(fontsize=10)
    dates=pivot_table['Date'].values
    retard=pivot_table['Sum of Retard'].values
    #depart=pivot_table['Sum of Depart anticipe'].values
    # Add labels and title
    plt.plot(dates,retard,'ro-',label='Sum of retard')
    #plt.plot(dates,depart,'go-',label='Sum of depart anticipe')
    plt.xlabel('Dates',fontsize=20)
    plt.ylabel('Retard and depart anticipe',fontsize=20)
    plt.title(department+' Tendance de Retard',fontsize=20)
    plt.legend(["Sum of Retard"], loc="upper left")
    
    # zip joins x and y coordinates in pairs
    for x,y in zip(dates,retard):

        label = "{:.1f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
   
    plt.xticks(np.arange(len(dates)),dates,rotation =45)
    #save fiile on pdf
    plt.savefig("reports/department_retard/"+department+".pdf", format='pdf')
    # Show the plot
    #plt.show()
    # Close the plot
    plt.close()
def generate_department_depart_excel_chart(pivot_table,department):
    # Reset index to make 'Date' a regular column
    pivot_table.reset_index(inplace=True)
    plt.figure(figsize=(20, 10))
    # Plotting the data
    #pivot_table.plot(x='Date', y=['Sum of Retard', 'Sum of Depart anticipe'], kind='line')
    plt.xticks(fontsize=10)
    dates=pivot_table['Date'].values
    #retard=pivot_table['Sum of Retard'].values
    depart=pivot_table['Sum of Depart anticipe'].values
    # Add labels and title
    #plt.plot(dates,retard,'ro-',label='Sum of retard')
    plt.plot(dates,depart,'go-',label='Sum of depart anticipe')
    plt.xlabel('Dates',fontsize=20)
    plt.ylabel('Depart anticipe',fontsize=20)
    plt.title(department+' Tendance de Depart anticipe',fontsize=20)
    plt.legend(["Sum of Depart anticipe"], loc="upper left")
    
    # zip joins x and y coordinates in pairs
    for x,y in zip(dates,depart):

        label = "{:.1f}".format(y)

        plt.annotate(label, # this is the text
                    (x,y), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center
   
    plt.xticks(np.arange(len(dates)),dates,rotation =45)
    #save fiile on pdf
    plt.savefig("reports/department_depart/"+department+".pdf", format='pdf')
    # Show the plot
    #plt.show()
    # Close the plot
    plt.close()
  


