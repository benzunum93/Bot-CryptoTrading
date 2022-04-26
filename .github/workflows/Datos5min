##Pide datos de graficas de 5 min
from binance.client import Client
from binance.websocket.websocket_client import BinanceWebsocketClient
import configuracion
import time
import sqlite3 #Para utilizar base de datos
import pandas as pd
import numpy as np



client= Client(configuracion.usuario,configuracion.contra) #Entra a binance

#Pide datos de velas de 5 min desde un periodo especifico    
def getminutedata(symbol,comando):
    datos=client.get_historical_klines(symbol, Client.KLINE_INTERVAL_5MINUTE, "10 Apr, 2022") #pide datos desde 1 jan 2021
    frame = pd.DataFrame(datos)
    frame= frame.iloc[:,:6]
    frame.columns=['Time','Open','High','Low','Close','Volume']
    frame=frame.set_index('Time')
    frame.index=pd.to_datetime(frame.index, unit='ms')
    frame=frame.astype(float)
    return frame

def creatabla5min(symbol, contador):
    conn = sqlite3.connect('datos5min.sqlite')
    datos5min=getminutedata(symbol,0)

    datos5min.to_sql(symbol,conn, if_exists="replace")
    conn.commit()
    conn.close()
#Elige de que pares de monedas se van adquirir los datos
def tomardatosmonedas():
    creatabla5min('BTCUSDT',0)
    creatabla5min('ETHUSDT', 1)
    creatabla5min('MANAUSDT', 2)
    creatabla5min('ROSEUSDT',3)
    creatabla5min('ADAUSDT',4)
    creatabla5min('BNBUSDT',5)
    creatabla5min('DOGEUSDT',6)
    creatabla5min('BAKEUSDT',7)
    
      





