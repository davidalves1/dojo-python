# -*- coding: utf-8 -*-		

import requests
from bs4 import BeautifulSoup

# page = requests.get('https://app.tororadar.com.br/analise/VALE5/')
page = requests.get('http://beans.itcarlow.ie/prices.html')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# parent - itens acima do item atual
# children - itens abaixo do item atual
# sibling - itens abaixo do mesmo item pai e no mesmo nível

for item in list(soup.children):
	print(type(item))

print(list(soup.children))

price = soup.find('strong').get_text()
print('O preço encontrado foi %s' % price)