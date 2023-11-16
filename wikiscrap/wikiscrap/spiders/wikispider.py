from typing import Iterable
import scrapy
from scrapy.http import Request
import pandas as pd
from wikiscrap.items import RegistryItem
# este es el archivo mas deficil de crear, es importante las importaciones iniciales ya que este archivo es un iterador a los demas

class WikispiderSpider(scrapy.Spider): # creacion del spider
    name = "wikispider" #nombre
    allowed_domains = ["wikipedia.org"] # tipo de dominio permitido
    
    def start_requests(self): #aca le contamos que las url a utilizar estan contenidas en un archivo csv
        df = pd.read_csv('C:/Users/pedro/OneDrive/Pedro/Aprender/Cursos/Programacion/Data Science/Proyectos/Integrador Personal/Datasets/conjunto_enlaces.csv')
        for index, row in df.iterrows(): #le decimos que vaya iterando sobre el archivo trabajando de la siguiente forma
    # abri el archivo, toma la primera url del dataframe y la primera clase, guardalos en variables, luego corre el scrapping y guarda la info para finalmente volver a iterar sobre el siguiente (por eso la salida es yield (un operador de iteracion))
            url = row['URL']
            entity_class = row['Type']
            yield scrapy.Request(url=url, callback=self.parse, meta={'class': entity_class})

    def parse(self, response):
        url = response.url #creas la response para cada caso
        entity_class = response.meta['class'] #tomas el valor del entity_class para crear el item
        
        for paragraph in response.css('p::text').getall(): #lo que haces aca es extraer el texto entre etiquetas <p></p> (parrafo) de todo el sitio e iterar sobre cada parrafo
            
            sentencias = paragraph.split('\n') #separo el parrafo en sentencias

            for sentencia in sentencias:
                if sentencia == '': #para evitar tener lineas vacias salteo el proceso cuando estan vacias
                    continue

                item = RegistryItem() #creo un item para exportar

                item['paragraph'] = sentencia #aca igualas el atributo paragraph del objeto item a la sentencia
                item['entity_class'] = entity_class #idem para la clase
                item['url'] = url #idem para la url

                yield item #como siempre usamos yield para retornar en modo iterador


