import scrapy
from zara.items import Producto

class ZaraSpider(scrapy.Spider):
    # Nombre de la araña
    name = "zara"
    
    # Dominios permitidos
    allowed_domains = ['zara.com']
    
    # URLs para comenzar a rastrear
    start_urls = [
        'https://www.zara.com/es/es/abrigo-oversize-con-lana-p02268744.html?v1=99425057&v2=1712675',
        'https://www.zara.com/es/es/camiseta-b%C3%A1sica-medium-weight-p00381300.html?v1=86668649&v2=1720409',
	'https://www.zara.com/es/es/sudadera-capucha-cremalleras-p00761406.html?v1=99422974&v2=1720409',
        'https://www.zara.com/es/es/pantal%C3%B3n-chino-carrot-fit-p00706475.html?v1=89361432&v2=1717453',
        'https://www.zara.com/es/es/sandalia-plana-track-p13647710.html?v1=86083745&v2=1471790',
	'https://www.zara.com/es/es/polo-rayas-p09240419.html?v1=99423481&v2=1720387',
        'https://www.zara.com/es/es/mochila-t%C3%A9cnica-p13201720.html?v1=99425027&v2=1720458'
    ]
    
    def parse(self, response):
        producto = Producto()
        
        # Extraemos el nombre del producto, la descripcion y su precio
        producto['nombre'] = response.xpath('//h1[@class="product-detail-info__name"]/text()').extract_first()
        producto['precio'] = response.xpath('//span[@class="price__amount"]/text()').extract_first()
        producto['descripcion'] = response.xpath('//div[@class="expandable-text product-detail-info__description"]//text()').extract_first()
        
        yield producto
