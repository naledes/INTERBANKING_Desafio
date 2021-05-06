# -*- coding: utf-8 -*-
"""
Created on Wed May  5 01:17:06 2021

@author: naled
"""

# De ser necesario, instalo librería sklearn por consola con siguiente comando
# pip install sklearn


# Import librerías

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# Genero dataframe con info de uso de internet

df = pd.read_csv('c:\z_interbanking_desafio\csv_internet.txt', sep='|')


# Chequeo dataframe generado y borro valores nulos o con ceros

df.head(30)

df.dropna(inplace = True)

df.head(30)

df.drop( df[ df['uso_de_internet'] == 0 ].index , inplace=True)

df.head(30)


# Seteo variables de entrada (X) y de salida (y) que alimentarán el modelo

X = pd.DataFrame(df['date']).values.reshape(-1, 1)
y = df['uso_de_internet'].values.reshape(-1, 1)


# Instancio el modelo

model = LinearRegression()


# Entreno el modelo

model.fit(X,y)


# Genero variable con predicciones

predictions = model.predict(X)


# Genero variable con predicción para el 2025 e imprimo resultado

valor_predecido = model.predict([[2025]])


print('Porcentaje de uso de internet para el 2025: {}%'.format(valor_predecido[0][0]))


