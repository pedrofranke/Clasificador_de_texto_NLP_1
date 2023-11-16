# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# vamos a ser lo mas prolijos posibles para hacer esto

class RegistryItem(scrapy.Item): #la clase que alojara los items
    url = scrapy.Field() # el campo para contener el valor de la url
    entity_class = scrapy.Field() # el campo para obtener el valor de la clase
    paragraph = scrapy.Field() # el campo para contener el valor de los parrafos
