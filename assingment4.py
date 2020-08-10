
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl 
df1 = pd.read_excel('data/01-01-2017 to 30-06-2017.xlsx',skiprows=3)
df2 = pd.read_excel('data/01-07-2017 to 01-12-2017.xlsx',skiprows=3)
df3 = pd.read_excel('data/02-12-2017 to 31-05-2018.xlsx',skiprows=3)
df4 = pd.read_excel('data/01-06-2018 to 29-11-2018.xlsx',skiprows=3)
df5 = pd.read_excel('data/30-11-2018 to 30-05-2019.xlsx',skiprows=3)   
df6 = pd.read_excel('data/31-05-2019 to 28-11-2019.xlsx',skiprows=3)
df7 = pd.read_excel('data/29-11-2019 to 31-12-2019.xlsx',skiprows=3)

#Clean first data frame
#january_june_2017 = january_june_2017.drop(january_june_2017.tail(12).index)

for i in df1,df2,df3,df4,df5,df6,df7:
    i.drop(i.tail(11).index,inplace = True) 
    (i.drop(columns = [
                    'OZONO','OZONO.1','OZONO.2',
                    'CO','CO.1','CO.2',
                    'SO2','SO2.2','SO2.1',
                    'NO','NO.1','NO.2',
                    'NO2','NO2.1','NO2.2',
                    'NOX','NOX.1','NOX.2',
                    'HR','HR.1','HR.2',
                    'Rad Solar','Rad Solar.1',
                    'Presion Baro','Presion Baro.1',
                    'CO API',
                    'Vel Viento','Vel Viento.1','Vel Viento.2',
                    'Dir Viento', 'Dir Viento.1','Dir Viento.2',
                    'PM2.5 Flow','CO2',
                    'Temp_4m'
                   ],inplace = True))
    #print(i)
print(df1)