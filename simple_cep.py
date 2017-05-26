# -*- coding: utf-8 -*-		

import requests
from bs4 import BeautifulSoup

# page = requests.get('https://app.tororadar.com.br/analise/VALE5/')
page = requests.get('https://cep.guiamais.com.br/busca/sao+paulo-sp')
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

rows = soup.find_all('tr')

for row in rows:
	items = row.find_all('td')
	print(items)