# -*- coding: utf-8 -*-

import requests

page = requests.get('http://beans.itcarlow.ie/prices.html')

text = page.text
print(text)
begin = text.find('ong>$') + 4 # O valor encontrado se refere ao primeiro caractere da string consultada
end = text.find('</str')

price = text[begin:end]
print('O preço encontrado foi %s' % price)