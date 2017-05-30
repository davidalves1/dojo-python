# -*- coding: utf-8 -*-		

import requests
from bs4 import BeautifulSoup

# page = requests.get('https://app.tororadar.com.br/analise/VALE5/')
page = requests.get('https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do')
soup = BeautifulSoup(page.content, 'html.parser')

columns = soup.find_all('td')

print('\n+----- Cotação do Dólar -----+')
print('Data: %s | Compra: %s | Venda: %s\n' % (columns[0].get_text(), columns[1].get_text(), columns[2].get_text()))