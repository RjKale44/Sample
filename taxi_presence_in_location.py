'''
Created on Dec 4, 2017

@author: RAJ
'''
import pandas as pd
df = pd.read_csv("C:\\Users\\Abhay\\Documents\\taxi\\train.csv")
def hour(row):
    return row['pickup_datetime'].split(sep=" ")[1].split(sep=":")[0]
def date(row):
    return row['pickup_datetime'].split(sep=" ")[0]
grouped = df.groupby([round(df['pickup_latitude'],2),round(df['pickup_longitude'],2),df.apply(date,axis=1),df.apply(hour,axis=1)])['id']  #according to pickup location & date_time groups will be created
print(grouped.count().sort_values(ascending=False))  #count will be sorted in  decending order
