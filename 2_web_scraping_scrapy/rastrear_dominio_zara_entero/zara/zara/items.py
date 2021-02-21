# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Producto(scrapy.Item):
    url = scrapy.Field()
    nombre = scrapy.Field()
    precio = scrapy.Field()
    descripcion = scrapy.Field()
    links = scrapy.Field()
    
