# -*- coding: utf-8 -*-		

# Documentaçao do BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
import sys
from bs4 import BeautifulSoup

page = requests.get('https://app.tororadar.com.br/analise/PETR4/')
soup = BeautifulSoup(page.content, 'html.parser')

info = soup.find('div', class_='info')

if info is None:
	sys.exit('Informações não encontradas')


paper = info.h1.get_text()
employee = info.h2.get_text()

oscilation = soup.find('div', class_='oscilation')

if oscilation is None:
	sys.exit('Valor não encontradas')

data = 'Papel: %s | Empresa: %s | Valor: %s' % (paper, employee, oscilation.get_text().strip())
print(data)

f = open('log.txt', 'a')
f.write(data + '\n')
f.close()