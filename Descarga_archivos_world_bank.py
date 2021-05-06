# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Instalo librerías por consola
#pip install wbpy
#pip install wbdata


#Importo librerías

import os.path
import wbdata
import pandas as pd
import datetime

import wbpy
import requests
import json
import functools


# Seteo variables necesarias para generar dataframes

pais = ['ARG']
data_date = datetime.datetime(1990, 1, 1), datetime.datetime(2019, 1, 1)                                                                                             
indicador_consolidado = {'IT.NET.USER.ZS':'uso_de_internet' , 'IT.NET.BBND':'Banda_ancha_fija', 'IT.CEL.SETS.P2' : 'Telefonia_Movil'} #Uso de Internet
indicador_internet = {'IT.NET.USER.ZS':'uso_de_internet'}
indicador_banda_ancha = {'IT.NET.BBND':'Banda_ancha_fija'}
indicador_movil = {'IT.CEL.SETS.P2' : 'Telefonia_Movil'}


# Genero dataframes usando librería wbdata

df_consolidado = wbdata.get_dataframe(indicador_consolidado, country=pais, data_date = data_date) #convert_date=False
df_internet = wbdata.get_dataframe(indicador_internet, country=pais, data_date = data_date)
df_banda_ancha = wbdata.get_dataframe(indicador_banda_ancha, country=pais, data_date = data_date)
df_movil = wbdata.get_dataframe(indicador_movil, country=pais, data_date = data_date)


# Ordeno físicamente los dataframes en función del año

df_consolidado = df_consolidado.sort_index()
df_internet = df_internet.sort_index()
df_banda_ancha = df_banda_ancha.sort_index()
df_movil= df_movil.sort_index()


# Chequeo dataframes generados

df_consolidado.head(30)
df_internet.head(30)
df_banda_ancha.head(30)
df_movil.head(30)


# Verifico columnas de los dataframes

df_consolidado.columns
df_internet.columns
df_banda_ancha.columns
df_movil.columns


# Creo directorio donse se almacenarán archivos TXT con info de indicadores 

dir_path = 'C:\Z_Interbanking_Desafio'
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)


# Genero TXT para cada uno de los dataframes

df_consolidado.to_csv(os.path.join(dir_path,'csv_consolidado.txt'), sep='|', index = True)
df_internet.to_csv(os.path.join(dir_path,'csv_internet.txt'), sep='|', index = True)
df_banda_ancha.to_csv(os.path.join(dir_path,'csv_banda_ancha.txt'), sep='|', index = True)
df_movil.to_csv(os.path.join(dir_path,'csv_movil.txt'), sep='|', index = True)



# Vuelvo a generar dataset de "uso de internet" con libreria wbpy
# Esta librería me facilita pasar el dataset generado a diccionario
# Por último paso el diccionario a formato json con la librería json

api = wbpy.IndicatorAPI()
dataset = api.get_dataset('IT.NET.USER.ZS', pais, date="2017:2017")

diccionario = dataset.as_dict()


json_object = json.dumps(diccionario) #, indent = 4


# Genero archivo jason para indicador de uso de internet
# Este .json alimentará la API del desafío Nivel 2

with open(os.path.join(dir_path,"internet_ult_anio.json"), "w") as outfile:
    outfile.write(json_object)






