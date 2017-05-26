# -*- coding: utf-8 -*-		

# Documentaçao do BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
import sys
from bs4 import BeautifulSoup

page = requests.get('http://stackoverflow.com/questions/tagged/python?sort=frequent&pageSize=15/')
soup = BeautifulSoup(page.content, 'html.parser')

summaries = soup.find_all('div', class_='question-summary')

f = open('log.txt', 'w')

for summary in summaries:
	# Total de visualizações
	question = summary.find('a', class_='question-hyperlink')	
	if question is not None:
		question = question.get_text().encode(sys.stdout.encoding, errors='replace')
	else:
		question = 'Não informado'

	# Total de respostas
	answers = summary.find('div', class_='answered-accepted')

	if answers is None:
		continue

	total_answers = answers.find('strong')
	if total_answers is not None:
		total_answers = total_answers.get_text()
	else:
		total_answers = 'Não informado'

	# Total de visualizações
	total_views = summary.find('div', class_='views')	
	if total_views is not None:
		end = total_views.get_text().find('views'); # Neste caso utiliza o método find do python e não do bs4
		total_views = total_views.get_text()[:end].strip()
	else:
		total_views = 'Não informado'	

	data = 'Questão: %s \nRespostas: %s \nVisualizações: %s\n-----' % (question, total_answers, total_views)
	f.write(data + '\n')

print('Sucesso!')
f.close()