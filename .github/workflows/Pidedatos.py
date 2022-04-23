#Pide los datos de varias monedas en periodos de 1 hora desde el 1 de enero del 2021
#y son almacenados en una tabla SQL llamada Prueba.sqlite
import pandas as pd
import numpy as np
from binance.client import Client
from binance.websocket.websocket_client import BinanceWebsocketClient
import configuracion
import time
import sqlite3 #Para utilizar base de datos


conn = sqlite3.connect('Prueba.sqlite')


client= Client(configuracion.usuario,configuracion.contra) #Entra a binance


def getalldata(symbol,comando):
    
    datos=client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR, "1 Jan, 2021") #pide datos desde 1 jan 2021
    frame = pd.DataFrame(datos)
    frame= frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame=frame.astype(float)
    
    return frame

def Monedas(symbol, contador):
    #Pide datos para 4H de BTCUSDT
    datosdefecha=getalldata(symbol,0)

    #Crea una tabla llamda BTCUSDT con los datos administrados
    datosdefecha.to_sql(symbol, conn, if_exists="replace")

    conn.commit()
    
    

def Time_server():
    time_res = client.get_server_time()
    time_res=float(time_res['serverTime'])
    
    tiempo_segundos=time.time()
    
    
    tiempo_cadena = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    
    tiempo_cadena=tiempo_cadena[:10]
    return tiempo_cadena
