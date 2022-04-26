##Crypto trading boot based in python, made for Carlos Sebastian Zapata
##Sent API request to binance to get some data that is used to
##analice Cryptocurrencies and send information if it's good to invest in short o long position
##For default the Cryto are 9,and can be more o less that nine, that depends on you, its as simple as calling the Funcion "Monesdas()"
##and pass the name of the Pair cryto, and a number that goes from 0 to etc.
##****For security you need to made you own "configuracion" file where you will storage you own Api keys to be call, because each user have it's own Api Keys.***

import Pidedatos
import estrategia
import Datos5min
import numpy as np
import pandas as pd
import time
import sqlite3 #Para utilizar base de datos
from datetime import datetime

current_date = datetime.now().date()
current_date=str(current_date)
Pidedatos.Time_server()

#recoleta los datos desde 1 de enero del 2021 hasta hoy de las siguientes monedas
try:
    conn = sqlite3.connect('Prueba.sqlite')
    frame=conn.execute("SELECT Time FROM BTCUSDT")
    frame=pd.DataFrame(frame)
    frame=str(frame[0][0])

    if frame[:10]!='2021-01-01':# IF it diferent, we request data
        print('Ya hay una tabla creada pero no tiene datos')

        Pidedatos.pidedatosmonedas()
    else:
        print('Ya hay datos')    
    while True:
        
        
        frame=conn.execute("SELECT * FROM BTCUSDT")
        frame = pd.DataFrame(frame)
        frame.columns=['Time','Open','High','Low','Close','Volume']
        tamaño=len(frame['Time'])-1 #Calcula el numero de la ultima fila en la tabla
            
        ultima_hora_tomada=frame['Time'][tamaño]#Pide el ultimo valor de la columna 'Time'
        ultima_hora_tomada=ultima_hora_tomada[:10] #Acota el valor del tiempo para que tome solo la fecha sin la hora

        #Mira si el ultimo dato esta actualizado
        if current_date==ultima_hora_tomada:

            estrategia.analisis()        
            
            time.sleep(60) #Espera 60 Segundos
            Datos5min.tomardatosmonedas()#Pide datos de 5 min
        else:
            print('Actualiza los datos')
            
            Pidedatos.pidedatosmonedas()#Pide datos de 4H
        


except:
    print('No hay base de datos creada')
    Pidedatos.pidedatosmonedas()



