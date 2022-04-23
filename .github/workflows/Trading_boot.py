##Crypto trading boot based in python, made for Carlos Sebastian Zapata
##Sent API request to binance to get some data that is used to
##analice Cryptocurrencies and send information if it's good to invest in short o long position
##For default the Cryto are 9,and can be more o less that nine, that depends on you, its as simple as calling the Funcion "Monesdas()"
##and pass the name of the Pair cryto, and a number that goes from 0 to etc.
##****For security you need to made you own "configuracion" file where you will storage you own Api keys to be call, because each user have it's own Api Keys.***

import Pidedatos
import estrategia
import numpy as np
import pandas as pd
import time
import sqlite3 #Para utilizar base de datos
from datetime import datetime
current_date = datetime.now().date()
current_date=str(current_date)
Pidedatos.Time_server()
#recoleta los datos desde 1 de enero del 2021 hasta hoy de las siguientes monedas
pide_datos_primera_vez=input('Primera vez pidiendo datos?')

if pide_datos_primera_vez=='si':
    Pidedatos.Monedas('BTCUSDT', 0)
    Pidedatos.Monedas('ETHUSDT', 1)
    Pidedatos.Monedas('MANAUSDT', 2)
    Pidedatos.Monedas('ROSEUSDT',3)
    Pidedatos.Monedas('ADAUSDT',4)
    Pidedatos.Monedas('BNBUSDT',5)
    Pidedatos.Monedas('DOGEUSDT',6)
    Pidedatos.Monedas('BAKEUSDT',7)

while True:
    conn = sqlite3.connect('Prueba.sqlite')
    frame=conn.execute("SELECT * FROM BTCUSDT")
    frame = pd.DataFrame(frame)
    frame.columns=['Time','Open','High','Low','Close','Volume']
    tamaño=len(frame['Time'])-1
        
    ultima_hora_tomada=frame['Time'][tamaño]
    ultima_hora_tomada=ultima_hora_tomada[:10] 

    
    if current_date==ultima_hora_tomada:
                
        estrategia.Monedas('BTCUSDT', 0)
        estrategia.Monedas('ETHUSDT', 1)
        estrategia.Monedas('MANAUSDT', 2)
        estrategia.Monedas('ROSEUSDT',3)
        estrategia.Monedas('ADAUSDT',4)
        estrategia.Monedas('BNBUSDT',5)
        estrategia.Monedas('DOGEUSDT',6)
        estrategia.Monedas('BAKEUSDT',7)
        time.sleep(60) #Espera 60 Segundos
    else:
        print('Pide mas datos')

        Pidedatos.Monedas('BTCUSDT', 0)
        Pidedatos.Monedas('ETHUSDT', 1)
        Pidedatos.Monedas('MANAUSDT', 2)
        Pidedatos.Monedas('ROSEUSDT',3)
        Pidedatos.Monedas('ADAUSDT',4)
        Pidedatos.Monedas('BNBUSDT',5)
        Pidedatos.Monedas('DOGEUSDT',6)
        Pidedatos.Monedas('BAKEUSDT',7)
        

