
import pandas as pd
import multiprocessing as mp
funclist = []
def task(df):
    return df.groupby([round(df.pickup_latitude,1),round(df.pickup_longitude,1)])
if __name__ == "__main__":
    reader = pd.read_csv("C:\\Users\\Abhay\\Documents\\taxi\\train.csv",chunksize=375000)       #data will be divided in equal parts and reference will be saved in list
    pool=mp.Pool(4)                     #Process poll has been created here
    for df in reader:
        f = pool.apply_async(task,[df])         #it will create seprate process which will apply task function will be applied to whole list
        funclist.append(f.get())        #result will be saved in funclist #here f.get() has been used to to get the result
    for df in funclist:
        print(df.apply(print))          #result sent by process will be printed but results are not combined 