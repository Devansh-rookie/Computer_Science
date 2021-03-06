import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

df  = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

df['HL_Percent'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100

df['PCT_Change'] = (df['Adj. Open'] - df['Adj. Close'])/df['Adj. Close']*100

df  = [['PCT_Change','HL_Percent','Adj. Close','Adj. Volume']]

print(df.head())
