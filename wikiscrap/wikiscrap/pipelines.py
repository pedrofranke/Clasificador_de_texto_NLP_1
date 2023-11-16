# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

class CsvExportPipeline: #dfinimos la exportacion a un csv
    def open_spider(self, spider): #al ejecutarse el spider se ejecuta esta funcion
        self.file = open('output.csv', 'w+b') #crear un archivo csv para hacer la exportacion
        self.exporter = CsvItemExporter(self.file) #creamos el exportador
        self.exporter.start_exporting() #empezamos a exportar bajo los criterios definidos en settings.py

    def close_spider(self, spider): #cerramos el spider
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider): #procesamos los items para exportarlos uno por uno al archivo creado en el inicio
        self.exporter.export_item(item)
        return item
