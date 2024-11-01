# -*- coding: utf-8 -*-
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup 
from subprocess import PIPE, Popen

   
#Urls, horrible la programación de la página:          
url_lista_mujeres = ['https://www.intersport.es/mujer/zapatillas/adidas/?page=5','https://www.intersport.es/mujer/zapatillas/arena/','https://www.intersport.es/mujer/zapatillas/nike/?page=7',
             'https://www.intersport.es/mujer/zapatillas/asics/?page=2', 'https://www.intersport.es/mujer/zapatillas/babolat/', 'https://www.intersport.es/mujer/zapatillas/bestard/',
             'https://www.intersport.es/mujer/zapatillas/brooks/', 'https://www.intersport.es/mujer/zapatillas/chiruca/', 'https://www.intersport.es/mujer/zapatillas/columbia/',
             'https://www.intersport.es/mujer/zapatillas/converse/', 'https://www.intersport.es/mujer/zapatillas/energetics/', 'https://www.intersport.es/mujer/zapatillas/firefly/',
             'https://www.intersport.es/mujer/zapatillas/havaianas/', 'https://www.intersport.es/mujer/zapatillas/head/', 'https://www.intersport.es/mujer/zapatillas/hoka-one-one/',
             'https://www.intersport.es/mujer/zapatillas/joma/', 'https://www.intersport.es/mujer/zapatillas/merrell/', 'https://www.intersport.es/mujer/zapatillas/la-sportiva/',
             'https://www.intersport.es/mujer/zapatillas/mckinley/', 'https://www.intersport.es/mujer/zapatillas/mizuno/', 'https://www.intersport.es/mujer/zapatillas/munich/',
             'https://www.intersport.es/mujer/zapatillas/new-balance/?page=3', 'https://www.intersport.es/mujer/zapatillas/pro-touch/', 'https://www.intersport.es/mujer/zapatillas/puma/?page=3',
             'https://www.intersport.es/mujer/zapatillas/quiksilver/', 'https://www.intersport.es/mujer/zapatillas/reebok/?page=3', 'https://www.intersport.es/mujer/zapatillas/roxy/',
             'https://www.intersport.es/mujer/zapatillas/salomon/?page=2', 'https://www.intersport.es/mujer/zapatillas/saucony/', 'https://www.intersport.es/mujer/zapatillas/skechers/?page=3',
             'https://www.intersport.es/mujer/zapatillas/speedo/', 'https://www.intersport.es/mujer/zapatillas/tecnopro/', 'https://www.intersport.es/mujer/zapatillas/teva/',
             'https://www.intersport.es/mujer/zapatillas/the-north-face/', 'https://www.intersport.es/mujer/zapatillas/under-armour/', 'https://www.intersport.es/mujer/zapatillas/vans/' ]


url_lista_hombres =['https://www.intersport.es/hombre/zapatillas/adidas/?page=11', 'https://www.intersport.es/hombre/zapatillas/arena/', 'https://www.intersport.es/hombre/zapatillas/nike/?page=10', 
                    'https://www.intersport.es/hombre/zapatillas/aqua-sphere/', 'https://www.intersport.es/hombre/zapatillas/asics/?page=2', 'https://www.intersport.es/hombre/zapatillas/asolo/', 
                    'https://www.intersport.es/hombre/zapatillas/babolat/', 'https://www.intersport.es/hombre/zapatillas/bestard/', 'https://www.intersport.es/hombre/zapatillas/brooks/', 
                    'https://www.intersport.es/hombre/zapatillas/chiruca/', 'https://www.intersport.es/hombre/zapatillas/columbia/', 'https://www.intersport.es/hombre/zapatillas/converse/',
                    'https://www.intersport.es/hombre/zapatillas/energetics/', 'https://www.intersport.es/hombre/zapatillas/firefly/', 'https://www.intersport.es/hombre/zapatillas/havaianas/?page=2',
                    'https://www.intersport.es/hombre/zapatillas/hoka-one-one/', 'https://www.intersport.es/hombre/zapatillas/joma/', 'https://www.intersport.es/hombre/zapatillas/la-sportiva/',
                    'https://www.intersport.es/hombre/zapatillas/mckinley/', 'https://www.intersport.es/hombre/zapatillas/merrell/', 'https://www.intersport.es/hombre/zapatillas/mizuno/?page=3',
                    'https://www.intersport.es/hombre/zapatillas/munich/', 'https://www.intersport.es/hombre/zapatillas/new-balance/?page=4', 'https://www.intersport.es/hombre/zapatillas/pro-touch/',
                    'https://www.intersport.es/hombre/zapatillas/puma/?page=5', 'https://www.intersport.es/hombre/zapatillas/quiksilver/?page=2', 'https://www.intersport.es/hombre/zapatillas/reebok/?page=3',
                    'https://www.intersport.es/hombre/zapatillas/reef/', 'https://www.intersport.es/hombre/zapatillas/salomon/?page=3', 'https://www.intersport.es/hombre/zapatillas/saucony/',
                    'https://www.intersport.es/hombre/zapatillas/skechers/?page=2', 'https://www.intersport.es/hombre/zapatillas/speedo/', 'https://www.intersport.es/hombre/zapatillas/tecnopro/',
                    'https://www.intersport.es/hombre/zapatillas/teva/', 'https://www.intersport.es/hombre/zapatillas/the-north-face/', 'https://www.intersport.es/hombre/zapatillas/under-armour/',
                    'https://www.intersport.es/hombre/zapatillas/vans/']


url_lista_kids = ['https://www.intersport.es/ninos/zapatillas/adidas/?page=6', 'https://www.intersport.es/ninos/zapatillas/arena/', 'https://www.intersport.es/ninos/zapatillas/nike/?page=8',
                  'https://www.intersport.es/ninos/zapatillas/asics/', 'https://www.intersport.es/ninos/zapatillas/babolat/', 'https://www.intersport.es/ninos/zapatillas/chiruca/',
                  'https://www.intersport.es/ninos/zapatillas/converse/', 'https://www.intersport.es/ninos/zapatillas/energetics/', 'https://www.intersport.es/ninos/zapatillas/firefly/',
                  'https://www.intersport.es/ninos/zapatillas/havaianas/', 'https://www.intersport.es/ninos/zapatillas/joma/', 'https://www.intersport.es/ninos/zapatillas/mckinley/',
                  'https://www.intersport.es/ninos/zapatillas/merrell/', 'https://www.intersport.es/ninos/zapatillas/mizuno/', 'https://www.intersport.es/ninos/zapatillas/munich/',
                  'https://www.intersport.es/ninos/zapatillas/new-balance/?page=3', 'https://www.intersport.es/ninos/zapatillas/pro-touch/', 'https://www.intersport.es/ninos/zapatillas/puma/?page=4',
                  'https://www.intersport.es/ninos/zapatillas/quiksilver/', 'https://www.intersport.es/ninos/zapatillas/reebok/?page=2', 'https://www.intersport.es/ninos/zapatillas/salomon/',
                  'https://www.intersport.es/ninos/zapatillas/saucony/', 'https://www.intersport.es/ninos/zapatillas/skechers/?page=2', 'https://www.intersport.es/ninos/zapatillas/tecnopro/',
                  'https://www.intersport.es/ninos/zapatillas/vans/']


zapatillas_hombres = list()
zapatillas_mujeres = list()
zapatillas_kids = list()

precios_hombres = list()
precios_mujeres = list()
precios_kids = list()

url_especf_mujeres = list()
url_especf_hombres = list()
url_especf_kids = list()

tallas_mujeres = list()
tallas_hombres = list()
tallas_kids = list()

def zapatillas_listas():
    #Mujeres:
    for i in url_lista_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        zp_mj = soup1.find_all('a', class_='name-link')
        
        for i in zp_mj:
            zapatillas_mujeres.append(i.text) 
    #Hombres:    
    for i in url_lista_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        zp_hm = soup2.find_all('a', class_='name-link')
        
        for i in zp_hm:
            zapatillas_hombres.append(i.text)  
    #Kids:    
    for i in url_lista_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        zp_kd = soup3.find_all('a', class_='name-link')
        
        for i in zp_kd:
            zapatillas_kids.append(i.text)  

        
def precios_lista():
    #Mujeres:
    for i in url_lista_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        pr_mj = soup1.find_all('span', class_='price')
        
        for i in pr_mj:
            precios_mujeres.append(i.text) #Igual el IDE te dice error, pero en verdad no hay tu tranqui
    #Hombres:
    for i in url_lista_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        pr_hm = soup2.find_all('span', class_='price')
        
        for i in pr_hm:
            precios_hombres.append(i.text) #Igual el IDE te dice error, pero en verdad no hay tu tranqui
    #KIDS: 
    for i in url_lista_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        pr_kd = soup3.find_all('span', class_='price')
        
        for i in pr_kd:
            precios_kids.append(i.text) #Igual el IDE te dice error, pero en verdad no hay tu tranqui
       

#Arreglando los precios, debido a que la página tiene \n y es una caca
precio_mujeres_limpio = str(precios_mujeres).replace("'", '').replace('\\n', '').replace(']', '').replace('[', '').replace('\\n', '')
lista_precio_mujeres = list()
lista_precio_mujeres = precio_mujeres_limpio.split(', ') #Importante el ', ' con el espacio de despues de la coma

precio_hombres_limpio = str(precios_hombres).replace("'", '').replace('\\n', '').replace(']', '').replace('[', '').replace('\\n', '')
lista_precio_hombres = list()
lista_precio_hombres = precio_hombres_limpio.split(', ') #Importante el ', ' con el espacio de despues de la coma

precio_kids_limpio = str(precios_kids).replace("'", '').replace('\\n', '').replace(']', '').replace('[', '').replace('\\n', '')
lista_precio_kids = list()
lista_precio_kids = precio_kids_limpio.split(', ') #Importante el ', ' con el espacio de despues de la coma


#Tallas:
def especificas_links():
    for i in url_lista_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        espcf = [link['href'] for link in soup1.findAll("a", {"class": "thumb-link"})] #Captamos las referencias de cada producto.
    
        for i in espcf:
            url_especf_mujeres.append(i)
    
    for i in url_lista_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        espcf2 = [link['href'] for link in soup2.findAll("a", {"class": "thumb-link"})] #Captamos las referencias de cada producto.
    
        for i in espcf2:
            url_especf_hombres.append(i)
    
    for i in url_lista_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        espcf3 = [link['href'] for link in soup3.findAll("a", {"class": "thumb-link"})] #Captamos las referencias de cada producto.
    
        for i in espcf3:
            url_especf_kids.append(i)


def tallas_lista():
    for i in url_especf_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        tl1 = soup1.find_all('a', class_='pdp-size-selector__grid__item__button')
    
        for i in tl1:
            tallas_mujeres.append(i.text)
            
    for i in url_especf_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        tl2 = soup2.find_all('a', class_='pdp-size-selector__grid__item__button')
    
        for i in tl2:
            tallas_hombres.append(i.text)
    
    for i in url_especf_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        tl3 = soup3.find_all('a', class_='pdp-size-selector__grid__item__button')
    
        for i in tl3:
            tallas_kids.append(i.text)


zapatillas_listas()    
precios_lista()
especificas_links()
tallas_lista()


df_mujeres = pd.DataFrame({'Nombre': zapatillas_mujeres, 'Coste': lista_precio_mujeres, 'Género': 'Mujer', 'Url': url_especf_mujeres, 'web_origen':'intersport.com'})
df_hombres = pd.DataFrame({'Nombre': zapatillas_hombres, 'Coste': lista_precio_hombres, 'Género': 'Hombre','Url': url_especf_hombres, 'web_origen':'intersport.com'})
df_kids = pd.DataFrame({'Nombre': zapatillas_kids, 'Coste': lista_precio_kids, 'Género': 'Ninos', 'Url': url_especf_kids,'web_origen':'intersport.com'})

df_intersport_prueba = pd.merge(df_mujeres, df_hombres, how='outer')
df_intersport = pd.merge(df_intersport_prueba, df_kids, how='outer')

df_intersport[['Marca','Nombre']] = df_intersport.Nombre.str.split(" · ",expand=True,)
df_intersport = df_intersport[['Nombre', 'Marca', 'Coste', 'Género', 'Url','web_origen']]

df_mujeres[['Marca','Nombre']] = df_mujeres.Nombre.str.split(" · ",expand=True,)
df_mujeres = df_mujeres[['Nombre', 'Marca', 'Coste', 'Género', 'Url','web_origen']]

df_hombres[['Marca','Nombre']] = df_hombres.Nombre.str.split(" · ",expand=True,)
df_hombres = df_hombres[['Nombre', 'Marca', 'Coste', 'Género', 'Url','web_origen']]

df_kids[['Marca','Nombre']] = df_kids.Nombre.str.split(" · ",expand=True,)
df_kids = df_kids[['Nombre', 'Marca', 'Coste', 'Género', 'Url','web_origen']]

df_intersport['Marca'] = df_intersport['Marca'].str.lower()
df_mujeres['Marca'] = df_mujeres['Marca'].str.lower()
df_hombres['Marca'] = df_hombres['Marca'].str.lower()
df_kids['Marca'] = df_kids['Marca'].str.lower()

df_mujeres['Coste'] = df_mujeres['Coste'].str.replace('€ ', '')
df_hombres['Coste'] = df_hombres['Coste'].str.replace('€ ', '')
df_kids['Coste'] = df_kids['Coste'].str.replace('€ ', '')
df_intersport['Coste'] = df_intersport['Coste'].str.replace('€ ', '')

df_intersport.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/intersport.csv', index = False)
df_mujeres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/df_mujeres.csv', index = False)
df_hombres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/df_hombres.csv', index = False)
df_kids.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/df_kids.csv', index = False)

df_tallas_mujeres = pd.DataFrame({'Tallas': tallas_mujeres})
df_tallas_hombres = pd.DataFrame({'Tallas': tallas_hombres})
df_tallas_kids = pd.DataFrame({'Tallas': tallas_kids})

df_tallas_mujeres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/df_tallas_mujeres.csv', index = False)
df_tallas_hombres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/df_tallas_hombres.csv', index = False)
df_tallas_kids.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/intersport/df_tallas_kids.csv', index = False)

#Borrando variables con no necesitamos al final:
del precios_mujeres; del precio_mujeres_limpio; del precios_hombres; del precio_hombres_limpio; del precios_kids; del precio_kids_limpio;
del df_intersport_prueba


