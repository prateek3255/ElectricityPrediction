import pandas as pd
import numpy as np
df = pd.read_csv('household_power_consumption.txt',sep=';',dtype={'Global_active_power': 'float'})
print(pd.to_datetime(df['Date'][1]+ ' '+df['Time'][1]).timestamp())
df['Timestamp']=pd.to_datetime(df['Date']+ ' '+df['Time'])
df['ts'] = df.Timestamp.values.astype(np.int64)
print(df.head())
df.to_csv('final.csv')

