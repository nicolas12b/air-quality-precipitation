import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.dates import DateFormatter
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df1 = pd.read_excel('data/01-01-2017 to 30-06-2017.xlsx',skiprows=3)
df2 = pd.read_excel('data/01-07-2017 to 01-12-2017.xlsx',skiprows=3)
df3 = pd.read_excel('data/02-12-2017 to 31-05-2018.xlsx',skiprows=3)
df4 = pd.read_excel('data/01-06-2018 to 29-11-2018.xlsx',skiprows=3)
df5 = pd.read_excel('data/30-11-2018 to 30-05-2019.xlsx',skiprows=3)   
df6 = pd.read_excel('data/31-05-2019 to 28-11-2019.xlsx',skiprows=3)
df7 = pd.read_excel('data/29-11-2019 to 31-12-2019.xlsx',skiprows=3)


#Remove last 11 elements
#remove columns 
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
                    'Temp_4m',
                    'PM10','PM10.1','PM10.2',
                    'Temperatura','Temperatura.1'
                   ],inplace = True))

frames = [df1,df2,df3,df4,df5,df6,df7]
#Put together all dataframes
df = pd.concat(frames)
df = df.dropna()

#Rename columns
(df.rename(columns = {
                        'Unnamed: 0':'Date',
                        'Precipitacion':'Precipitation (mm)',
                        'Precipitacion.1':'Precipitation.1 (mm)',
                        'Precipitacion.2':'Precipitation.2 (mm)',
                        'PM2.5' : 'PM2.5 (µg/m3)',
                        'PM2.5.1' : 'PM2.5 .1 (µg/m3)',
                        'PM2.5.2' : 'PM2.5 .2 (µg/m3)',
                        },inplace = True))

#df = df.set_index('Date')
df = df.replace('----',np.nan).dropna()

df['Date'] = df['Date'].str.replace(r' 24:00','')


#Plot

figure = plt.figure(figsize = (8,20)) 
plt.suptitle('Precipitation and Air Quality from 2017 to 2019 in Bogota, Colombia ')

plt.subplot(311,xlabel = 'PM2.5 (µg/m3)',ylabel = 'Precipitation (mm)')
plt.scatter(df['PM2.5 (µg/m3)'],df['Precipitation (mm)'],color  = 'r')
fig = plt.gca()
fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)

plt.subplot(312,xlabel = 'PM2.5 (µg/m3)',ylabel = 'Precipitation (mm)')
plt.scatter(df['PM2.5 .1 (µg/m3)'],df['Precipitation.1 (mm)'],color = 'g')
fig = plt.gca()
fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)

plt.subplot(313,xlabel = 'PM2.5 (µg/m3)',ylabel = 'Precipitation (mm)')
plt.scatter(df['PM2.5 .2 (µg/m3)'],df['Precipitation.2 (mm)'],color = 'orange')

fig = plt.gca()
fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)
names = ['Station 1','Station 2', 'Station 3']
figure.legend(names,loc = 'center right')
plt.show()
