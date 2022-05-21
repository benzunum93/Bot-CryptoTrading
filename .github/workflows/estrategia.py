##Robot final creado por Carlos Sebastian Zapata
##Aca se encuentra la estrategia y analisis de los datos.


import pandas as pd
import time#Para poner retardos en tiempo de 1 segundo
import ta #Para analisis de indicadores de trading
import numpy as np

import matplotlib.pyplot as plt #Para graficar
import matplotlib.animation as FuncAnimation
import configuracion
import sqlite3 #Para utilizar base de datos

def temporalidad_analisis(temporalidad):

    
    #Eligue que temporalidad usar segun lo que se obitiene de Main_bot
    conn = sqlite3.connect(temporalidad)
    rsi_indice=[0]
    High=[]
    Close=[]
    Low=[]
    i=0
    numeros_monedas=7# Total de monedas
    indicador_venta=[0]#Enumera la moneda para ver si analiza la salida de una posicion o entrada
    posicion_activo=[0] #indicador si la posicion esta en long 0 o short 1

    while i<numeros_monedas:
        #Indica con cero q la moneda esta vendida, y 1 si esta comprada
        indicador_venta.append(0)
        posicion_activo.append(0)
        i=i+1


    mac=[0]
        

    #Coge el ultimo valor del calculo de cada indicador
    def tratamiento_datos(datos): 
    
        longitud=len(datos)
        datos1=datos[longitud+32]
        datos1=float(datos1)
        
        return datos1 

    #Funcion para obtener los datos de cada Moneda

    def getminutedata(symbol):
        if symbol=='BTCUSDT':
            frame=conn.execute("SELECT * FROM BTCUSDT")
            
        if symbol=='ETHUSDT':
            frame=conn.execute("SELECT * FROM ETHUSDT")
            
        if symbol=='MANAUSDT':
            frame=conn.execute("SELECT * FROM MANAUSDT")    
            
        if symbol=='ROSEUSDT':
            frame=conn.execute("SELECT * FROM ROSEUSDT")
        if symbol=='ADAUSDT':
            frame=conn.execute("SELECT * FROM ADAUSDT")
        if symbol=='BNBUSDT':
            frame=conn.execute("SELECT * FROM BNBUSDT")
        if symbol=='DOGEUSDT':
                frame=conn.execute("SELECT * FROM DOGEUSDT")
        if symbol=='BAKEUSDT':
                frame=conn.execute("SELECT * FROM BAKEUSDT")
        frame = pd.DataFrame(frame)
        frame.columns=['Time','Open','High','Low','Close','Volume']
        
        return frame

    #Funcion para Calcular los indicadores

    def aplicartecnicals(df):    
        df['%K']=ta.momentum.stoch(df.High, df.Low, df.Close, window=14, smooth_window=3)
        df['%D']=df['%K'].rolling(3).mean()
        # Calculo RSI, se necesita 14 datos anteriores para que este haga un calculo
        df['rsi']=ta.momentum.rsi(df.Close, window=14)#, fillna=True) 
        #Calculo MACD se necesita 34 datos antes de que este haga un calculo
        df['macd']=ta.trend.macd_diff(df.Close)#,fillna=True) 
        #Para borrar los valores q no contengan Nada
        df.dropna(inplace=True) 
        
        return df


    def Monedas(symbol, contador):
        #Obtiene los datos de cada activo o cryto y los guarda como un frame en df
        df=getminutedata(symbol)
        
        #Aplica la estrategia con los datos guardados en df
        señal=aplicartecnicals(df)
        
        #Llama a funcion tratamiento_datos para tomar el ultimo calculo de cada indicador
        K_line=tratamiento_datos(señal['%K'])
        D_line=tratamiento_datos(señal['%D'])
        rsi_indice=tratamiento_datos(señal['rsi'])
        mac=tratamiento_datos(señal['macd'])        
        precio=tratamiento_datos(señal['Close'])   
        #print(symbol,',',K_line,',',D_line,',',rsi_indice,',',mac,',',precio)
        
        #Condiciones de compra y venta
        
        if indicador_venta[contador]==0:
            #Condicion de compra
            if (rsi_indice>50.0) and (80>K_line>20)and(80>D_line>20): 
                if mac>0.0:
                    print('LONG en  '+symbol)
                    posicion_activo[contador]=0
                    indicador_venta[contador]=1
                    print('Precio: ',precio)
            #Condicion de short                
            if (rsi_indice<50) and (80>K_line>20)and(80>D_line>20):
                if mac<0.0:
                    print('SHORT en '+symbol)
                    print('Precio: ',precio)
                    posicion_activo[contador]=1
                    indicador_venta[contador]=1
        #Cuando compre un activo y analiza cuando salir 
        
        else:
            if posicion_activo[contador]==0:
                if (rsi_indice<50) and (80>K_line>20)and(80>D_line>20):
                    if mac<0.0:
                        print('Salir de Long en '+symbol)
                        print('Salida: ',precio)
                        indicador_venta[contador]=0
            else:
                if (rsi_indice>50.0) and (80>K_line>20)and(80>D_line>20):
                    if mac>0.0:
                        print(' Salir de SHORT en '+symbol)
                        print('Salida: ',precio)
                        indicador_venta[contador]=0        
    
    def analisis():
    
        Monedas('BTCUSDT', 0)
        Monedas('ETHUSDT', 1)
        Monedas('MANAUSDT', 2)
        Monedas('ROSEUSDT',3)
        Monedas('ADAUSDT',4)
        Monedas('BNBUSDT',5)
        Monedas('DOGEUSDT',6)
        Monedas('BAKEUSDT',7)    

    analisis()
   
   
