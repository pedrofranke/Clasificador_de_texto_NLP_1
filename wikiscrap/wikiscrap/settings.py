# Scrapy settings for wikiscrap project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "wikiscrap"

SPIDER_MODULES = ["wikiscrap.spiders"]
NEWSPIDER_MODULE = "wikiscrap.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'wikiscrap.pipelines.CsvExportPipeline': 300,
} # mencionamos que wikiscrap va a exportar en formato csv segun definido en el pipelinespy


FEEDS = {
    'output.csv': {
        'format': 'csv',
        'overwrite': True,
        'fields': ['url', 'entity_class', 'paragraph'],  # adjust this based on your Item structure
    },
} #detallamos el archivo donde se hara la exportacion, que se va a escribir sobre un archivo existente y la estructura de columnas inicial y orden a exportar

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
