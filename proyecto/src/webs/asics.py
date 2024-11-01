import pandas as pd
import requests
import os
from bs4 import BeautifulSoup 
from time import sleep
from random import randint
from subprocess import PIPE, Popen


url_men = 'https://www.asics.com/es/es-es/mens-shoes/c/as10200000/?sz=96&start='
url_women = 'https://www.asics.com/es/es-es/womens-shoes/c/as20200000/?sz=96&start='
enlace = 'https://www.asics.com/es/es-es/'

sleep(randint(1,5))
lista_num_women = []
lista_url_women = []
lista_num_men = []
lista_url_men = []

def lista_enlaces_generos():
#MUJERES
    lista_num_women = [1,97,193,289,385,390]      
    lista_num_women_str = str(lista_num_women).replace('[', '').replace(']', '').replace(' ', '')
    lista_num_women_str = lista_num_women_str.split(sep=',')

    for i in lista_num_women_str:
        lista_url_women.append(url_women + i)
        
#HOMBRES
    lista_num_men = [1,97,193,289,385,390]        
    lista_num_men_str = str(lista_num_men).replace('[', '').replace(']', '').replace(' ', '')
    lista_num_men_str = lista_num_men_str.split(sep=',')
 
    for i in lista_num_men_str:
        lista_url_men.append(url_men + i)        
        

zapatillas_men = list()
zapatillas_women = list() 
coste_men = list()
coste_women = list() 
def zapatillas_lista():
#ZAPATILLAS_MEN
    for i in lista_url_men:       
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
    
        zp = soup1.find_all('div', class_='product-tile__text product-tile__text--large product-tile__text--underline')
        for i in zp:
            zapatillas_men.append(i.text)  
        
        ct = soup1.find_all('span', class_='price-sales')
        for i in ct:
            coste_men.append(i.text)
    
#ZAPATILLAS_WOMEN
    for i in lista_url_women:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
    
        zp = soup2.find_all('div', class_='product-tile__text product-tile__text--large product-tile__text--underline')
        for i in zp:
            zapatillas_women.append(i.text)  
        
        ct = soup2.find_all('span', class_='price-sales')
        for i in ct:
            coste_women.append(i.text)

url_esp_men = list()
url_esp_women = list() 
def especificas_links(): #Específicos enlaces         
#ENLACE_ESP_MEN   
    for i in lista_url_men:
        page1 = requests.get(i)
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        espcf = [link['href'] for link in soup1.findAll("a", {"class": "product-tile__link js-product-tile"})] #Captamos las referencias de cada producto.

        for i in espcf:
            url_esp_men.append(url_men + i)
            
#ENLACE_ESP_WOMEN      
    for i in lista_url_women:
        page2 = requests.get(i)
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        espcf = [link['href'] for link in soup2.findAll("a", {"class": "product-tile__link js-product-tile"})] #Captamos las referencias de cada producto.

        for i in espcf:
            url_esp_women.append(url_women + i)
        

tallas_men = list()  
tallas_women = list()           
def tallas_lista():                
#Url Especifica Men 
    for i in url_esp_men: 
        page1 = requests.get(i) 
        soup1 = BeautifulSoup(page1.content, 'html.parser')     
        
        tl_H = soup1.find_all('div', class_="variants variants--asics-eu js-variants")

        for i in tl_H:       
            tallas_men.append(i.text)   
            print(tallas_men)
                     
#Url Especifica Women     
    for i in url_esp_women: 
        page2 = requests.get(i) 
        soup2 = BeautifulSoup(page2.content, 'html.parser')   

        tl_W = soup2.find_all('div', class_="variants variants--asics-eu js-variants ")
  
        for i in tl_W:      
            tallas_women.append(i.text)   
            print(tallas_women)


lista_enlaces_generos()      
zapatillas_lista() 
especificas_links()
tallas_lista()

#pandas dataframe   
df_mujeres = pd.DataFrame({'Nombre': zapatillas_women, 'Marca': 'asics', 'Coste': coste_women, 'Género':'Mujer', 'Url': url_esp_women,
                           'web_origen': 'asics.com'})    
df_hombres = pd.DataFrame({'Nombre': zapatillas_men, 'Marca': 'asics', 'Coste': coste_men, 'Género':'Hombre', 'Url': url_esp_men,
                           'web_origen': 'asics.com'})  
           
df_mujeres['Coste'] = df_mujeres['Coste'].replace(['\€'],'', regex=True).replace(['Precio de venta'],'', regex=True).replace([' '],'', regex=True)
df_hombres['Coste'] = df_hombres['Coste'].replace(['\€'],'', regex=True).replace(['Precio de venta'],'', regex=True).replace([' '],'', regex=True)

df_final = pd.merge(df_mujeres, df_hombres, how='outer')

df_final.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/asics/asics.csv', index = False)
df_mujeres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/asics/df_mujeres.csv', index = False)
df_hombres.to_csv('C:/Users/jesus/Desktop/powers/Segundo-Curso/segundo-cuatrimestre/open-data/proyecto/data_output/asics/df_hombres.csv', index = False)
