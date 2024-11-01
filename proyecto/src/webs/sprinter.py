# -*- coding: utf-8 -*-
import pandas as pd
import requests
import numpy as np
import os
from bs4 import BeautifulSoup 
from subprocess import PIPE, Popen


#url = 'https://www.sprintersports.com/zapatillas?serie=H,M,NA,NO,U&per_page=100&page='
url_kids = 'https://www.sprintersports.com/calzado-nino?per_page=100&page='
url_kids_n = 'https://www.sprintersports.com/calzado-nina?per_page=100&page='
url_mujeres = 'https://www.sprintersports.com/calzado-deportivo-mujer?per_page=100&page='
url_hombres = 'https://www.sprintersports.com/calzado-deportivo-hombre?per_page=100&page='
enlace = 'https://www.sprintersports.com'

lista_num_mujeres = list()
lista_num_hombres = list()
lista_num_kids = list()
lista_num_kids_n = list()

lista_url_mujeres = list()
lista_url_hombres = list()
lista_url_kids= list() 
lista_url_kids_n = list() 

def lista_enlaces_generos():
#MUJERES
    for i in range(43):
        lista_num_mujeres.append(i)        
    lista_num_mujeres.pop(0)
    lista_num_mujeres_str = str(lista_num_mujeres).replace('[', '').replace(']', '').replace(' ', '')
    lista_num_mujeres_str = lista_num_mujeres_str.split(sep=',')
    del i    
    for i in lista_num_mujeres_str:
        lista_url_mujeres.append(url_mujeres + i)
        
#HOMBRES
    for i in range(48):
        lista_num_hombres.append(i)        
    lista_num_hombres.pop(0)
    lista_num_hombres_str = str(lista_num_hombres).replace('[', '').replace(']', '').replace(' ', '')
    lista_num_hombres_str = lista_num_hombres_str.split(sep=',')
    del i    
    for i in lista_num_hombres_str:
        lista_url_hombres.append(url_hombres + i)        
        
#NIÑOS    
    for i in range(23):
        lista_num_kids.append(i)
    lista_num_kids.pop(0) #Posición 0, porque el primer dato de la lista acaba siendo 0.
    lista_num_kids_str = str(lista_num_kids).replace('[', '').replace(']', '').replace(' ', '')
    lista_num_kids_str = lista_num_kids_str.split(sep=',')    
    del i    
    for i in lista_num_kids_str:  
        lista_url_kids.append(url_kids + i)
        
#NIÑOS     
    for i in range(20):
        lista_num_kids_n.append(i)
    lista_num_kids_n.pop(0) #Posición 0, porque el primer dato de la lista acaba siendo 0.
    lista_num_kids_n_str = str(lista_num_kids_n).replace('[', '').replace(']', '').replace(' ', '')
    lista_num_kids_n_str = lista_num_kids_n_str.split(sep=',')    
    del i    
    for i in lista_num_kids_n_str:  
        lista_url_kids_n.append(url_kids_n + i) 

        
#Zapatillas/Coste
zapatillas_hombres = list()
zapatillas_mujeres = list()
zapatillas_kids = list()
zapatillas_kids_n = list()

def zapatillas_lista():   
#Mujeres:
    for i in lista_url_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        zp_mj = soup1.find_all('a', class_='product__name')
        
        for i in zp_mj:
            zapatillas_mujeres.append(i.text)  
        
#Hombres:    
    for i in lista_url_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        zp_hm = soup2.find_all('a', class_='product__name')
        
        for i in zp_hm:
            zapatillas_hombres.append(i.text)  
   
#Kids:    
    for i in lista_url_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        zp_kd = soup3.find_all('a', class_='product__name')
        
        for i in zp_kd:
            zapatillas_kids.append(i.text) 
            
#Kids Ninia:    
    for i in lista_url_kids_n:
        page4 = requests.get(i)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        
        zp_kd_n = soup4.find_all('a', class_='product__name')
        
        for i in zp_kd_n:
            zapatillas_kids_n.append(i.text) 


precios_hombres = list()
precios_mujeres = list()
precios_kids = list()
precios_kids_n = list()

def precios_lista():
#Mujeres:
    for i in lista_url_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        pr_mj = soup1.find_all('span', class_='product__price--actual')
        
        for i in pr_mj:
            precios_mujeres.append(i.text) #Igual el IDE te dice error, pero en verdad no hay tu tranqui
            
#Hombres:
    for i in lista_url_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        pr_hm = soup2.find_all('span', class_='product__price--actual')
        
        for i in pr_hm:
            precios_hombres.append(i.text) #Igual el IDE te dice error, pero en verdad no hay tu tranqui
            
#KIDS: 
    for i in lista_url_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        pr_kd = soup3.find_all('span', class_='product__price--actual')
        
        for i in pr_kd:
            precios_kids.append(i.text)
            
#KIDS ninias: 
    for i in lista_url_kids_n:
        page4 = requests.get(i)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        
        pr_kd_n = soup4.find_all('span', class_='product__price--actual')
        
        for i in pr_kd_n:
            precios_kids_n.append(i.text)


url_especf_mujeres = list()
url_especf_hombres = list()
url_especf_kids = list()
url_especf_kids_n = list()

#Específicos enlaces
def especificas_links():
#Mujeres
    for i in lista_url_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        espcf = [link['href'] for link in soup1.findAll("a", {"class": "product__name"})] #Captamos las referencias de cada producto.
    
        for i in espcf:
            url_especf_mujeres.append(enlace + i)

#Hombres    
    for i in lista_url_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        espcf2 = [link['href'] for link in soup2.findAll("a", {"class": "product__name"})] #Captamos las referencias de cada producto.
    
        for i in espcf2:
            url_especf_hombres.append(enlace + i)

#Kids    
    for i in lista_url_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        espcf3 = [link['href'] for link in soup3.findAll("a", {"class": "product__name"})] #Captamos las referencias de cada producto.
    
        for i in espcf3:
            url_especf_kids.append(enlace + i)

#Kids ninia            
    for i in lista_url_kids_n:
        page4 = requests.get(i)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        
        espcf4 = [link['href'] for link in soup4.findAll("a", {"class": "product__name"})] #Captamos las referencias de cada producto.
    
        for i in espcf4:
            url_especf_kids_n.append(enlace + i)        

            
tallas_mujeres = list()
tallas_hombres = list()
tallas_kids = list()
tallas_kids_n = list()          
            
def tallas_lista():
#Mujeres
    for i in url_especf_mujeres:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        
        tl1 = soup1.find_all('div', class_="sheet-data-size square")
    
        for i in tl1:
            tallas_mujeres.append(i.text)

#Hombres            
    for i in url_especf_hombres:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        
        tl2 = soup2.find_all('div', class_="sheet-data-size square")
    
        for i in tl2:
            tallas_hombres.append(i.text)

#Kids    
    for i in url_especf_kids:
        page3 = requests.get(i)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        
        tl3 = soup3.find_all('div', class_="sheet-data-size square")
    
        for i in tl3:
            tallas_kids.append(i.text)            

#Kids ninia        
    for i in url_especf_kids_n:
        page4 = requests.get(i)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        
        tl4 = soup4.find_all('div', class_="sheet-data-size square")
    
        for i in tl4:
            tallas_kids_n.append(i.text)
            
#Funciones:
lista_enlaces_generos()
zapatillas_lista()
precios_lista()
especificas_links()
tallas_lista()

#Aunque dé error no pasa nada, dá supuestamente error porque elminas las variables después
del lista_num_hombres; del lista_num_mujeres; del lista_num_kids_n; del lista_num_kids; del url_hombres; del url_kids; 
del url_mujeres; del url_kids_n  

#Creación del csv:
df_mujeres = pd.DataFrame({'Nombre': zapatillas_mujeres, 'Coste': precios_mujeres, 'Género': 'Mujer', 'Url': url_especf_mujeres,'web_origen':'sprinter.com'})
df_hombres = pd.DataFrame({'Nombre': zapatillas_hombres, 'Coste': precios_hombres, 'Género': 'Hombre', 'Url': url_especf_hombres,'web_origen':'sprinter.com'})

df_kids_nino = pd.DataFrame({'Nombre': zapatillas_kids, 'Coste': precios_kids, 'Género': 'Ninos', 'Url': url_especf_kids,'web_origen':'sprinter.com'})
df_kids_n = pd.DataFrame({'Nombre': zapatillas_kids_n, 'Coste': precios_kids_n, 'Género': 'Ninos', 'Url': url_especf_kids_n, 'web_origen':'sprinter.com'})
df_kids = pd.merge(df_kids_nino, df_kids_n, how='outer')

del df_kids_n; del df_kids_nino;

df_mujeres[['Marca','Nombre']] = df_mujeres.Nombre.str.split(" ",expand=True,n=1)
df_hombres[['Marca','Nombre']] = df_hombres.Nombre.str.split(" ",expand=True,n=1)
df_kids[['Marca','Nombre']] = df_kids.Nombre.str.split(" ",expand=True,n=1)

df_mujeres = df_mujeres[['Nombre', 'Marca', 'Coste', 'Género', 'Url', 'web_origen']]
df_hombres = df_hombres[['Nombre', 'Marca', 'Coste', 'Género', 'Url','web_origen']]
df_kids = df_kids[['Nombre', 'Marca', 'Coste', 'Género', 'Url','web_origen']]

df_mujeres['Marca'] = df_mujeres['Marca'].str.lower()
df_hombres['Marca'] = df_hombres['Marca'].str.lower()
df_kids['Marca'] = df_kids['Marca'].str.lower()


df_mujeres['Coste'] = df_mujeres['Coste'].str.replace('€', '')
df_hombres['Coste'] = df_hombres['Coste'].str.replace('€', '')
df_kids['Coste'] = df_kids['Coste'].str.replace('€', '')

df_prueba = pd.merge(df_mujeres, df_hombres, how='outer')
df_sprinter = pd.merge(df_prueba, df_kids, how='outer')
del df_prueba;

df_sprinter.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/sprinter/sprinter.csv', index = False)
df_mujeres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/sprinter/df_mujeres.csv', index = False)
df_hombres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/sprinter/df_hombres.csv', index = False)
df_kids.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/sprinter/df_kids.csv', index = False)



path_sprinter = 'C:\\Users\\jesus\\Desktop\\powers\\Segundo-Curso\\segundo-cuatrimestre\\open-data\\proyecto\\data_output\\sprinter\\sprinter.csv'
hdfs_path = os.path.join(os.sep, 'user', '<jesus>', df_sprinter)

put = Popen(["hadoop", "fs", "-put", 'C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/sprinter/sprinter.csv', '/user/clsadmin/sprinter'], 
            stdin=PIPE, bufsize=-1)
put.communicate()