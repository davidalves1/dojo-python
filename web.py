# -*- coding: utf-8 -*-		

# Documentaçao do BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import json
import requests
import sys
import time
from bs4 import BeautifulSoup

papers_list = ['PETR4', 'VALE5', 'OIBR4']

for search in papers_list:
	page = requests.get('https://app.tororadar.com.br/analise/%s/' % search)

	if page.status_code != 200:
		print('O papel %s não foi encontrado.' % search)
		time.sleep(2)
		pass

	soup = BeautifulSoup(page.content, 'html.parser')

	info = soup.find('div', class_='info')

	if info is None:
		print('Informações não encontradas para %s' % search)
		pass

	paper = info.h1.get_text()
	employee = info.h2.get_text()

	oscilation = soup.find('div', class_='oscilation')

	if oscilation is None:
		print('Informações não encontradas para %s' % search)
		pass

	values = oscilation.get_text().strip().split()

	analise = soup.find('div', class_='analise-description')

	if analise is None:
		print('Informações não encontradas para %s' % search)
		pass

	analise = analise.p.get_text()

	data = json.dumps({
		'acao': paper,
		'empresa': employee, 
		'valor': float(values[1]),
		'oscilacao': float(values[2][:-1])
		# 'analise': analise.strip()
	})

	print(data)

	f = open('log.txt', 'a')
	f.write(data + '\n')
	f.close()

	time.sleep(3)