'''
Created on Dec 4, 2017

@author: RAJ
'''
import pandas as pd
def hour(row):
    return row['pickup_datetime'].split(sep=" ")[1].split(sep=":")[0]  # hour of date will be sent

df = pd.read_csv("C:\\Users\\Abhay\\Documents\\taxi\\train.csv")
df['day'] = df.apply(hour,axis=1)       #seprate day column has been created here
grouped = df.groupby([round(df['dropoff_latitude'],2),round(df['pickup_longitude'],2),df['day']])['id'].count()   #count will be saved according grouped location of dropoff
print(grouped.sort_values())  #result will be sorted
 