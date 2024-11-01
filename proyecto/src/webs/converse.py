import pandas as pd
import requests
import os
from time import sleep
from random import randint
from bs4 import BeautifulSoup 


url_kids ='https://www.converse.com/es/products/converse/ni%C3%B1os/sneakers/todas-las-sneakers?lang=es_ES&pmid=AllOrderable-AllComingSoon-products-promotion&pmpt=PROMOTION_PRODUCT_TYPE_QUALIFYING&start=0&sz=16'
enlace = 'https://www.converse.com/es'

lista_num = list()
for i in range(75):
    lista_num.append(i)
       
lista_num.pop(0) #Posición 0, porque el primer dato de la lista acaba siendo 0.
lista_num_str = str(lista_num).replace('[', '').replace(']', '').replace(' ', '')
lista_num_str = lista_num_str.split(sep=',')

del i

lista_url= list()    
for i in lista_num_str:  
    lista_url.append(url_kids + i)
    

zapatillas_kids = list()
coste_kids = list()

for i in lista_url:

    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

#Zapatillas:
zp = soup.find_all('a', class_='name-link')

    
for i in zp:
      zapatillas_kids.append(i.text)  
       #sleep(randint(1,4)) 
        
ct = soup.find_all('div', class_='product-pricing')

for i in ct:    
    coste_kids.append(i.text)
     #sleep(randint(1,4))

url2_kids = list()
for i in lista_url:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

#Específicos enlaces
espcf = [link['href'] for link in soup.findAll("a", {"class": "name-link"})] #Captamos las referencias de cada producto.



#Hacemos el bucle para añadir las referencias al link original:
for i in espcf:
    url2_kids.append(enlace + i)

#Tallas por zapa
tallas_kids = list()   


for i in url2_kids: 
    page2 = requests.get(i) 
    soup2 = BeautifulSoup(page2.content, 'html.parser')   

    tl = soup2.find_all('div', class_="variations__container variations__container--dropdown toggle-box toggle-box--single set--themeable")

    for i in tl:
         #sleep(randint(1,4))
        tallas_kids.append(i.text)   
        
        
#Creación del csv:

df_kids = pd.DataFrame({'Marca': "converse",'Nombre': zapatillas_kids, 'Coste': coste_kids, 'Género': "Ninos",'Links': url2_kids, 'web_origen':'converse.com'})
df_kids.to_csv('zapas-converse_niños.csv', index = False, encoding='UTF-8')
df_kids['Coste']=df_kids['Coste'].replace(['\€'], '', regex=True)
df_tallas_kids = pd.DataFrame({'Tallas': tallas_kids})
df_tallas_kids.to_csv('tallas-converse_niños.csv', index = False, encoding='UTF-8')










url_hombre ='https://www.converse.com/es/products/converse/hombre/sneakers/todas-las-sneakers?lang=es_ES&pmid=AllOrderable-AllComingSoon-products-promotion&pmpt=PROMOTION_PRODUCT_TYPE_QUALIFYING&start=0&sz=16'
enlace_hombre = 'https://www.converse.com/es'

lista_num = list()
for i in range(75):
    lista_num.append(i)
       
lista_num.pop(0) #Posición 0, porque el primer dato de la lista acaba siendo 0.
lista_num_str = str(lista_num).replace('[', '').replace(']', '').replace(' ', '')
lista_num_str = lista_num_str.split(sep=',')

del i

lista_url= list()    
for i in lista_num_str:  
    lista_url.append(url_hombre + i)


zapatillas_hombre = list()
coste_hombre = list()

for i in lista_url:

    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

#Zapatillas:
zp = soup.find_all('a', class_='name-link')

    
for i in zp:
      zapatillas_hombre.append(i.text)  
       #sleep(randint(1,4)) 
        
ct = soup.find_all('div', class_='product-pricing')

for i in ct:    
    coste_hombre.append(i.text)
     #sleep(randint(1,4))

url2_hombre = list()
for i in lista_url:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

#Específicos enlaces
espcf = [link['href'] for link in soup.findAll("a", {"class": "name-link"})] #Captamos las referencias de cada producto.



#Hacemos el bucle para añadir las referencias al link original:
for i in espcf:
    url2_hombre.append(enlace_hombre + i)
     #sleep(randint(1,4))
#Tallas por zapa
tallas_hombre = list()   


for i in url2_hombre: 
    page2 = requests.get(i) 
    soup2 = BeautifulSoup(page2.content, 'html.parser')   

    tl = soup2.find_all('div', class_="variations__container variations__container--dropdown toggle-box toggle-box--single set--themeable")

    for i in tl:
         #sleep(randint(1,4))
        tallas_hombre.append(i.text)   
        #print(tallas)
        
#Creación del csv:

df_hombre = pd.DataFrame({'Marca': "converse",'Nombre': zapatillas_hombre, 'Coste': coste_hombre, 'Género': "Mujer",'Links': url2_hombre, 'web_origen':'converse.com'})
df_hombre.to_csv('zapas-converse_hombre.csv', index = False, encoding='UTF-8')
df_hombre['Coste']=df_hombre['Coste'].replace(['\€'], '', regex=True)
df_tallas_hombre = pd.DataFrame({'Tallas': tallas_hombre})
df_tallas_hombre.to_csv('tallas-converse_hombre.csv', index = False, encoding='UTF-8')













url_mujeres ='https://www.converse.com/es/products/converse/mujer/sneakers/todas-las-sneakers?lang=es_ES&pmid=AllOrderable-AllComingSoon-products-promotion&pmpt=PROMOTION_PRODUCT_TYPE_QUALIFYING&start=0&sz=32'
enlace_mujeres = 'https://www.converse.com/es'

lista_num = list()
for i in range(75):
    lista_num.append(i)
       
lista_num.pop(0) #Posición 0, porque el primer dato de la lista acaba siendo 0.
lista_num_str = str(lista_num).replace('[', '').replace(']', '').replace(' ', '')
lista_num_str = lista_num_str.split(sep=',')

del i

lista_url= list()    
for i in lista_num_str:  
    lista_url.append(url_mujeres + i)


zapatillas_mujeres = list()
coste_mujeres = list()

for i in lista_url:

    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

#Zapatillas:
zp = soup.find_all('a', class_='name-link')

    
for i in zp:
      zapatillas_mujeres.append(i.text)  
       #sleep(randint(1,4))  
        
ct = soup.find_all('div', class_='product-pricing')

for i in ct:    
    coste_mujeres.append(i.text)
     #sleep(randint(1,4))

url2_mujeres = list()
for i in lista_url:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

#Específicos enlaces
espcf = [link['href'] for link in soup.findAll("a", {"class": "name-link"})] #Captamos las referencias de cada producto.



#Hacemos el bucle para añadir las referencias al link original:
for i in espcf:
    url2_mujeres.append(enlace + i)
    sleep(randint(1,4))
#Tallas por zapa
tallas_mujeres = list()   


for i in url2_mujeres: 
    page2 = requests.get(i) 
    soup2 = BeautifulSoup(page2.content, 'html.parser')   

    tl = soup2.find_all('div', class_="variations__container variations__container--dropdown toggle-box toggle-box--single set--themeable")

    for i in tl:
        #sleep(randint(1,4))
        tallas_mujeres.append(i.text)   
        #print(tallas)
        
#Creación del csv:

df_mujeres = pd.DataFrame({'Marca': "converse",'Nombre': zapatillas_mujeres, 'Coste': coste_mujeres, 'Género': "Hombre",'Links': url2_mujeres, 'web_origen':'converse.com'})
df_mujeres.to_csv('zapas-converse_mujeres.csv', index = False, encoding='UTF-8')
df_mujeres['Coste']=df_mujeres['Coste'].replace(['\€'], '', regex=True)
df_tallas_mujeres = pd.DataFrame({'Tallas': tallas_mujeres})
df_tallas_mujeres.to_csv('tallas-converse_mujeres.csv', index = False, encoding='UTF-8')



df_conver_muj_hom = pd.merge(df_mujeres, df_hombre, how='outer')
df_converse = pd.merge(df_conver_muj_hom, df_kids, how='outer')
df_converse.to_csv('Converse.csv', index = False)

df_converse['Coste']=df_converse['Coste'].replace(['\€'], '', regex=True)