'''
Created on Dec 4, 2017

@author: RAJ
'''
import pandas as pd
def hour(row):
    return row['pickup_datetime'].split(sep=" ")[1].split(sep=":")[0]       #this function will send the hour of day

df = pd.read_csv("C:\\Users\\Abhay\\Documents\\taxi\\train.csv")
df['day'] = df.apply(hour,axis=1)               #seprate day column has been created here
grouped = df.groupby([round(df['pickup_latitude'],2),round(df['pickup_longitude'],2),df['day']])['id'].count() #groups will be created according to pickup location & there count according to id will be saved
print(grouped.sort_values())    # values has been sorted here
