# -*- coding: utf-8 -*-
import pandas as pd
import requests
import numpy as np
import os

from bs4 import BeautifulSoup 
from subprocess import PIPE, Popen


sprinter = pd.read_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/sprinter/sprinter.csv')
intersport = pd.read_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/intersport.csv')
asics = pd.read_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/asics/asics.csv')


converse_hombres = pd.read_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/src/webs/zapas-converse_hombre.csv')
converse_kids = pd.read_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/src/webs/zapas-converse_niños.csv')

converse_hombres['Coste'] = converse_hombres['Coste'].str.replace('€', '',regex=True)
converse_kids['Coste'] = converse_kids['Coste'].str.replace('€', '',regex=True)


converse_hombres['Nombre'] = converse_hombres['Nombre'].replace('			            ', '',regex=True)
converse_kids['Nombre'] = converse_kids['Nombre'].replace('			            ', '',regex=True)

converse_hombres = converse_hombres.rename(columns={'Links': 'Url'})
converse_kids = converse_kids.rename(columns={'Links': 'Url'})

converse_hombres = converse_hombres[['Nombre', 'Marca', 'Coste', 'Género', 'Url']]
converse_kids = converse_kids[['Nombre', 'Marca', 'Coste', 'Género', 'Url']]

converse_hombres.insert(5, 'web_origen','converse.com')
converse_kids.insert(5, 'web_origen','converse.com')

converse = pd.merge(converse_hombres, converse_kids, how='outer')


df_final = pd.merge(sprinter, intersport, how='outer')
df_final = pd.merge(df_final, asics, how='outer')
df_final = pd.merge(df_final, converse, how='outer')


df_final.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/final/df_final.csv')
converse.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/converse/converse.csv')

hdfs_path = os.path.join(os.sep, 'user', '<clsadmin>', sprinter)
# put csv into hdfs
put = Popen(["hdfs", "dfs", "-put", sprinter, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()





