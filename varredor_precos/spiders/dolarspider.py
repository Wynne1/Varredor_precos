import scrapy
from datetime import datetime
from utils.email_sender import Emailer

class PriceScraperSpider(scrapy.Spider):
    #identidade
    name ='dolarpreco'

    #request
    def start_requests(self):
        urls = ['https://www.investing.com/currencies/usd-brl']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # response
    def parse(self, response):
        dolar = response.xpath("//span[@data-test='instrument-price-last']/text()")[0].get()

        if float(dolar) > 5.45:
            email = Emailer('seuemail@email.com', 'senha_token_do_email')
            lista_de_contatos = ['email_enviar1','email_enviar2']
            email.definir_conteudo('Dólar está subindo', 'seuemail@email.com', lista_de_contatos, f'O dolar está subindo para{dolar}, talvez seja uma boa hora para comprar dólar')

            email.enviar_email(10)
    